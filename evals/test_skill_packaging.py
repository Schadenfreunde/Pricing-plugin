"""Verify independent installs and reject missing or external skill dependencies."""

import shutil
import tempfile
import unittest
from pathlib import Path

from check_package import SKILLS, check_package, check_skill


ROOT = Path(__file__).resolve().parents[1]


class SkillPackagingTests(unittest.TestCase):
    def test_each_skill_installs_without_repository_or_siblings(self):
        for name in SKILLS:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as temp:
                installed = Path(temp) / name
                shutil.copytree(ROOT / "skills" / name, installed)
                self.assertGreater(check_skill(installed), 0)
                self.assertEqual((installed / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())

    def test_existing_file_outside_skill_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            installed = Path(temp) / "pricing-intake"
            shutil.copytree(ROOT / "skills/pricing-intake", installed)
            (Path(temp) / "external.md").write_text("External dependency")
            with (installed / "SKILL.md").open("a") as source:
                source.write("\n[External](../external.md)\n")
            with self.assertRaisesRegex(ValueError, "outside standalone skill"):
                check_skill(installed)

    def test_missing_bundled_card_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            installed = Path(temp) / "pricing-analyze"
            shutil.copytree(ROOT / "skills/pricing-analyze", installed)
            (installed / "references/knowledge/metric-verification.md").unlink()
            with self.assertRaisesRegex(ValueError, "outside standalone skill"):
                check_skill(installed)

    def test_symlink_outside_skill_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            installed = Path(temp) / "pricing-intake"
            shutil.copytree(ROOT / "skills/pricing-intake", installed)
            outside = Path(temp) / "external.md"
            outside.write_text("External dependency")
            (installed / "external.md").symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "Symlink in standalone skill"):
                check_skill(installed)

    def test_unsynchronized_knowledge_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            checkout = Path(temp)
            for folder in ("skills", "knowledge"):
                shutil.copytree(ROOT / folder, checkout / folder)
            for name in ("plugin.json", "README.md", "LICENSE"):
                shutil.copyfile(ROOT / name, checkout / name)
            with (checkout / "knowledge/metric-verification.md").open("a") as source:
                source.write("\nChanged canonical note.\n")
            with self.assertRaisesRegex(ValueError, "Stale bundled knowledge"):
                check_package(checkout)


if __name__ == "__main__":
    unittest.main()
