#!/usr/bin/env python3
"""Check the development checkout's runtime inventory; does not test model behavior."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKILLS = (
    "pricing-intake", "pricing-analyze", "pricing-scan", "pricing-recommend",
    "pricing-design", "pricing-execute", "pricing-triage",
)
RUNTIME_PATHS = (
    "plugin.json", "README.md", "LICENSE",
    *(f"skills/{name}/SKILL.md" for name in SKILLS),
    "skills/pricing-intake/references/context-outline.md",
    "skills/pricing-analyze/references/html-reporting.md",
    "knowledge/index.md", "knowledge/metric-verification.md",
    "knowledge/margin-drivers.md", "knowledge/price-waterfall.md",
    *(f"knowledge/methods/{name}.md" for name in (
        "value-estimation", "segmentation", "peer-comparisons",
        "price-realization", "discount-governance", "price-change-economics",
    )),
)


def prose(markdown):
    """Omit fenced code, including tilde fences and longer closing fences."""
    lines = []
    fence_char, fence_length = None, 0
    for line in markdown.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence_char:
            if (marker and marker[1][0] == fence_char
                    and len(marker[1]) >= fence_length and not marker[2].strip()):
                fence_char = None
            continue
        if marker:
            fence_char, fence_length = marker[1][0], len(marker[1])
        else:
            lines.append(line)
    return "\n".join(lines)


def link_targets(markdown):
    # Inline links/images plus reference definitions. Titles are not paths.
    destination = r'(<[^>]+>|[^\s)]+)'
    yield from (match[1].strip("<>") for match in re.finditer(
        r'!?\[[^\]]*\]\(\s*' + destination + r'(?:\s+[\'\"][^\n]*?[\'\"])?\s*\)',
        markdown,
    ))
    yield from (match[1].strip("<>") for match in re.finditer(
        r'^ {0,3}\[[^\]]+\]:\s*' + destination, markdown, re.MULTILINE,
    ))


def check_package(root):
    root = Path(root).resolve()
    manifest = json.loads((root / "plugin.json").read_text())
    if manifest.get("name") != "pricing-plugin" or manifest.get("version") != "0.2.0":
        raise ValueError("Manifest must name pricing-plugin at version 0.2.0 "
                         f"(found {manifest.get('name')} / {manifest.get('version')})")

    if manifest.get("license") != "MIT":
        raise ValueError("Manifest must declare the MIT license")

    actual_skills = {path.parent.name for path in (root / "skills").glob("*/SKILL.md")}
    if actual_skills != set(SKILLS):
        raise ValueError(f"Expected exactly seven skill names; found {sorted(actual_skills)}")
    for name in SKILLS:
        source = (root / "skills" / name / "SKILL.md").read_text()
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", source, re.DOTALL)
        if not frontmatter:
            raise ValueError(f"Missing frontmatter: {name}")
        fields = dict(re.findall(r"^([\w-]+):[ \t]*(.*)$", frontmatter[1], re.MULTILINE))
        if fields.get("name", "").strip("\'\"") != name:
            raise ValueError(f"Frontmatter name does not match folder: {name}")
        if not fields.get("description", "").strip().strip("\'\""):
            raise ValueError(f"Missing description: {name}")

    if len(RUNTIME_PATHS) != 22 or len(set(RUNTIME_PATHS)) != 22:
        raise ValueError("Runtime inventory must contain 22 distinct paths")
    allowed = {root / path for path in RUNTIME_PATHS}
    for relative in RUNTIME_PATHS:
        path = root / relative
        if not path.is_file() or path.resolve() != path:
            raise ValueError(f"Missing runtime file or symlink outside inventory: {relative}")

    checked = 0
    for relative in RUNTIME_PATHS:
        if not relative.startswith(("skills/", "knowledge/")) or not relative.endswith(".md"):
            continue
        path = root / relative
        body = prose(path.read_text())
        if re.search(r"/(?:Users|home|private|tmp)/|[A-Za-z]:\\", body):
            raise ValueError(f"Absolute developer path in {relative}")
        if "references/curriculum-repository" in body:
            raise ValueError(f"Ignored curriculum dependency in {relative}")
        for target in link_targets(body):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            decoded = unquote(parsed.path)
            if Path(decoded).is_absolute():
                raise ValueError(f"Absolute reference in {relative}: {target}")
            resolved = (path.parent / decoded).resolve()
            if resolved not in allowed or not resolved.is_file():
                raise ValueError(f"Reference outside runtime inventory in {relative}: {target}")
        checked += 1
    return f"PASS: seven skills, version 0.2.0, 22 runtime files, {checked} Markdown reference closures"


if __name__ == "__main__":
    try:
        print(check_package(Path(__file__).resolve().parents[1]))
    except (ValueError, OSError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
