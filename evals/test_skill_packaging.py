"""Validate the complete plugin and its shared resources as shipped."""

import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from check_package import SKILLS, check_package, check_runtime_links, check_skill


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_plugin_zip import build_plugin_zip


class SkillPackagingTests(unittest.TestCase):
    def checkout(self, root):
        shutil.copytree(ROOT / "skills", root / "skills")
        shutil.copytree(ROOT / "examples", root / "examples")
        shutil.copytree(ROOT / "evals/cases", root / "evals/cases")
        shutil.copyfile(ROOT / "evals/README.md", root / "evals/README.md")
        for name in ("plugin.json", "README.md", "INSTALL.md", "PRICING_SYSTEM.md", "LICENSE",
                     ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, root / name)
        return root

    def test_complete_plugin_loads_unmodified_sources(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            self.assertTrue(check_package(root).startswith("PASS:"))
            for name in SKILLS:
                with self.subTest(skill=name):
                    installed = root / "skills" / name
                    self.assertEqual((installed / "SKILL.md").read_bytes(),
                                     (ROOT / "skills" / name / "SKILL.md").read_bytes())
                    self.assertGreater(check_skill(installed), 0)

    def test_knowledge_has_one_location(self):
        copies = list((ROOT / "skills").glob("pricing-*/references/knowledge"))
        self.assertEqual(copies, [], "Pricing knowledge belongs only in skills/knowledge")

    def test_claude_manifest_version_drift_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            path = root / ".claude-plugin/plugin.json"
            manifest = json.loads(path.read_text())
            manifest["version"] = "99.0.0"
            path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, "Claude manifest.*version"):
                check_package(root)

    def test_claude_zip_keeps_shared_resources_and_excludes_local_data(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp) / "source")
            (root / ".pricing").mkdir()
            (root / ".pricing/context.md").write_text("Private company context")
            archive = Path(temp) / "pricing-plugin.zip"
            build_plugin_zip(root, archive)
            installed = Path(temp) / "installed"
            with zipfile.ZipFile(archive) as bundle:
                bundle.extractall(installed)
            plugin = (installed / "pricing-plugin").resolve()
            self.assertTrue((plugin / ".claude-plugin/plugin.json").is_file())
            self.assertTrue((plugin / "LICENSE").is_file())
            self.assertFalse((plugin / ".pricing").exists())
            self.assertFalse((plugin / "evals").exists())
            self.assertEqual({p.parent.name for p in (plugin / "skills").glob("*/SKILL.md")},
                             set(SKILLS))
            for source in (root / "skills").rglob("*"):
                if source.is_file():
                    self.assertEqual(source.read_bytes(),
                                     (plugin / source.relative_to(root)).read_bytes())
            files = {p for p in plugin.rglob("*") if p.is_file()}
            self.assertGreater(check_runtime_links(plugin, files), 0)

    def test_individual_skill_is_not_a_complete_installation(self):
        for name in SKILLS:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as temp:
                installed = Path(temp) / "skills" / name
                shutil.copytree(ROOT / "skills" / name, installed)
                with self.assertRaises(ValueError):
                    check_skill(installed)

    def test_missing_sibling_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            shutil.rmtree(root / "skills/pricing-intake")
            with self.assertRaises(ValueError):
                check_skill(root / "skills/pricing-analyze")

    def test_missing_shared_card_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            (root / "skills/knowledge/metric-verification.md").unlink()
            for name in SKILLS:
                with self.subTest(skill=name), self.assertRaises(ValueError):
                    check_skill(root / "skills" / name)

    def test_legacy_analyze_reference_is_rejected_without_repair(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            entry = root / "skills/pricing-analyze/SKILL.md"
            self.assertIn("../knowledge/", entry.read_text())
            entry.write_text(entry.read_text().replace("../knowledge/", "references/knowledge/"))
            with self.assertRaises(ValueError):
                check_skill(entry.parent)

    def test_reference_outside_declared_resources_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            (root / "external.md").write_text("Undeclared resource")
            entry = root / "skills/pricing-intake/SKILL.md"
            with entry.open("a") as source:
                source.write("\n[External](../../external.md)\n")
            with self.assertRaisesRegex(ValueError, "reference|Reference"):
                check_skill(entry.parent)

    def test_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            card = root / "skills/knowledge/metric-verification.md"
            outside = root / "external.md"
            outside.write_bytes(card.read_bytes())
            card.unlink()
            card.symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "[Ss]ymlink"):
                check_package(root)

    def test_duplicate_knowledge_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            copy = root / "skills/pricing-scan/references/knowledge/metric-verification.md"
            copy.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / "skills/knowledge/metric-verification.md", copy)
            with self.assertRaisesRegex(ValueError, "inventory|[Dd]uplicate"):
                check_package(root)

    def test_canonical_edit_needs_no_sync(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            with (root / "skills/knowledge/metric-verification.md").open("a") as source:
                source.write("\nA canonical edit has no copies to synchronize.\n")
            self.assertTrue(check_package(root).startswith("PASS:"))

    def test_documentation_file_and_heading_links_are_checked(self):
        for target in ("missing.md", "README.md#missing-heading"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as temp:
                root = self.checkout(Path(temp))
                example = root / "examples/README.md"
                example.parent.mkdir(exist_ok=True)
                example.write_text(f"[Broken](../{target})\n")
                with self.assertRaisesRegex(ValueError, "link|[Rr]eference|[Aa]nchor"):
                    check_package(root)

    def test_encoded_reference_and_fenced_example_are_supported(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.checkout(Path(temp))
            entry = root / "skills/pricing-intake/SKILL.md"
            with entry.open("a") as source:
                source.write("\n[Waterfall](../knowledge/%70rice-waterfall.md)\n"
                             "```text\n[Example](missing.md)\n```\n")
            self.assertGreater(check_skill(entry.parent), 0)


if __name__ == "__main__":
    unittest.main()
