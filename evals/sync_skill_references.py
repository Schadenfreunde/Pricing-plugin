#!/usr/bin/env python3
"""Bundle maintained source notes into independently installable skill folders."""

from pathlib import Path
from shutil import copyfile

from check_package import KNOWLEDGE_PATHS, KNOWLEDGE_SKILLS, REPORT_SKILLS, SKILLS


def sync(root):
    root = Path(root)
    for name in KNOWLEDGE_SKILLS:
        for relative in KNOWLEDGE_PATHS:
            destination = root / "skills" / name / "references/knowledge" / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            copyfile(root / "knowledge" / relative, destination)
    source = root / "skills/pricing-analyze/references/html-reporting.md"
    for name in REPORT_SKILLS:
        if name != "pricing-analyze":
            copyfile(source, root / "skills" / name / "references/html-reporting.md")
    for name in SKILLS:
        copyfile(root / "LICENSE", root / "skills" / name / "LICENSE")


if __name__ == "__main__":
    sync(Path(__file__).resolve().parents[1])
    print("Bundled knowledge, report guidance, and MIT notices into skill folders.")
