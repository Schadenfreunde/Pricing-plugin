"""Validate the complete plugin and its shared resources as shipped."""

import shutil
import tempfile
import unittest
from pathlib import Path

from check_package import SKILLS, check_package, check_skill


ROOT = Path(__file__).resolve().parents[1]


class SkillPackagingTests(unittest.TestCase):
    def checkout(self, root):
        shutil.copytree(ROOT / "skills", root / "skills")
        shutil.copytree(ROOT / "examples", root / "examples")
        shutil.copytree(ROOT / "evals/cases", root / "evals/cases")
        shutil.copyfile(ROOT / "evals/README.md", root / "evals/README.md")
        for name in ("plugin.json", "README.md", "INSTALL.md", "LICENSE"):
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
