#!/usr/bin/env python3
"""Validate the complete plugin's shared resources and local documentation links."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKILLS = (
    "pricing-intake", "pricing-analyze", "pricing-scan", "pricing-recommend",
    "pricing-design", "pricing-execute", "pricing-triage",
)
KNOWLEDGE_PATHS = (
    "index.md", "metric-verification.md", "margin-drivers.md", "price-waterfall.md",
    *(f"methods/{name}.md" for name in (
        "value-estimation", "segmentation", "peer-comparisons", "price-realization",
        "discount-governance", "price-change-economics", "evidence-ranking",
    )),
)
RUNTIME_PATHS = (
    "plugin.json", "README.md", "INSTALL.md", "LICENSE",
    ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
    *(f"skills/{name}/SKILL.md" for name in SKILLS),
    *(f"skills/knowledge/{path}" for path in KNOWLEDGE_PATHS),
    "skills/pricing-intake/references/context-outline.md",
    *(f"skills/references/{name}.md" for name in ("html-reporting", "pdf-export", "handoff")),
)


def prose(markdown):
    """Omit fenced examples, including tilde fences and longer closing fences."""
    lines = []
    fence_char, fence_length = None, 0
    for line in markdown.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence_char:
            if (marker and marker[1][0] == fence_char
                    and len(marker[1]) >= fence_length and not marker[2].strip()):
                fence_char = None
        elif marker:
            fence_char, fence_length = marker[1][0], len(marker[1])
        else:
            lines.append(line)
    return "\n".join(lines)


def link_targets(markdown):
    destination = r'(<[^>]+>|[^\s)]+)'
    yield from (match[1].strip("<>") for match in re.finditer(
        r'!?\[[^\]]*\]\(\s*' + destination + r'(?:\s+[\'\"][^\n]*?[\'\"])?\s*\)',
        markdown,
    ))
    yield from (match[1].strip("<>") for match in re.finditer(
        r'^ {0,3}\[[^\]]+\]:\s*' + destination, markdown, re.MULTILINE,
    ))


def anchors(path):
    body = prose(path.read_text())
    result = set(re.findall(r'\b(?:id|name)=["\']([^"\']+)["\']', body))
    counts = {}
    if path.suffix == ".md":
        for title in re.findall(r"^ {0,3}#{1,6}\s+(.+?)\s*#*$", body, re.MULTILINE):
            slug = re.sub(r"[^\w\s-]", "", title.lower()).replace(" ", "-")
            count = counts.get(slug, 0)
            counts[slug] = count + 1
            result.add(f"{slug}-{count}" if count else slug)
    return result


def check_links(path, root, allowed=None):
    for target in link_targets(prose(path.read_text())):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        decoded = unquote(parsed.path)
        resolved = (path.parent / decoded).resolve() if decoded else path
        if (Path(decoded).is_absolute() or not resolved.is_relative_to(root)
                or not resolved.is_file() or (allowed is not None and resolved not in allowed)):
            raise ValueError(f"Missing or unsupported reference in {path.relative_to(root)}: {target}")
        if parsed.fragment and unquote(parsed.fragment) not in anchors(resolved):
            raise ValueError(f"Missing anchor in {path.relative_to(root)}: {target}")


def check_layout(root):
    if len(set(RUNTIME_PATHS)) != len(RUNTIME_PATHS):
        raise ValueError("Duplicate runtime inventory path")
    skills = root / "skills"
    if skills.is_symlink() or any(path.is_symlink() for path in skills.rglob("*")):
        raise ValueError("Symlink in plugin resources")
    allowed = {root / path for path in RUNTIME_PATHS}
    for path in allowed:
        if not path.is_file() or path.resolve() != path:
            raise ValueError(f"Missing complete-plugin resource: {path.relative_to(root)}")
    expected = {path for path in allowed if path.is_relative_to(skills)}
    actual = {path for path in skills.rglob("*") if path.is_file()}
    if actual != expected:
        raise ValueError("Skill inventory mismatch; unexpected: "
                         f"{sorted(str(p.relative_to(root)) for p in actual - expected)}")
    return allowed


def check_runtime_links(root, allowed):
    checked = 0
    for path in sorted(allowed):
        if not path.is_relative_to(root / "skills") or path.suffix != ".md":
            continue
        body = prose(path.read_text())
        if re.search(r"/(?:Users|home|private|tmp)/|[A-Za-z]:\\", body):
            raise ValueError(f"Absolute developer path in {path.relative_to(root)}")
        if "references/curriculum-repository" in body:
            raise ValueError(f"Ignored curriculum dependency in {path.relative_to(root)}")
        check_links(path, root, allowed)
        checked += 1
    return checked


def check_skill(folder):
    """Validate a skill in its complete installation, without repairing its source."""
    folder = Path(folder).resolve()
    if folder.name not in SKILLS or folder.parent.name != "skills":
        raise ValueError("Install the complete plugin with all seven skills and shared resources")
    root = folder.parent.parent
    return check_runtime_links(root, check_layout(root))


def check_documentation(root):
    paths = [root / "README.md", root / "INSTALL.md"]
    for directory in ("examples", "assets", "SEO"):
        paths.extend(sorted((root / directory).glob("*.md")))
    for path in paths:
        check_links(path, root)
    return len(paths)


def check_package(root):
    root = Path(root).resolve()
    allowed = check_layout(root)
    manifest = json.loads((root / "plugin.json").read_text())
    version = manifest.get("version", "")
    if manifest.get("name") != "pricing-plugin" or not re.fullmatch(
            r"\d+\.\d+\.\d+(?:-[\w.-]+)?(?:\+[\w.-]+)?", version):
        raise ValueError("Manifest must name pricing-plugin with a semantic version")
    if manifest.get("license") != "MIT":
        raise ValueError("Manifest must declare the MIT license")
    claude_manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
    for field in ("name", "version", "description", "author", "repository", "keywords", "license"):
        if claude_manifest.get(field) != manifest.get(field):
            raise ValueError(f"Claude manifest must match portable manifest: {field}")
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
    checked = check_runtime_links(root, allowed)
    docs = check_documentation(root)
    return (f"PASS: {len(SKILLS)} interdependent skills, version {version}, "
            f"{len(RUNTIME_PATHS)} runtime files, {checked} runtime Markdown files, "
            f"{docs} documentation files")


if __name__ == "__main__":
    try:
        print(check_package(Path(__file__).resolve().parents[1]))
    except (ValueError, OSError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
