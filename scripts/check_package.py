#!/usr/bin/env python3
"""Validate the plugin package and its public documentation links.

The package is everything under skills/ plus ROOT_FILES; nothing else ships.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = (
    "plugin.json", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", "LICENSE",
)
# Public documentation: link-checked but not shipped.
DOCS = ("README.md", "INSTALL.md", "PRICING_SYSTEM.md")
DOC_DIRS = ("examples",)
SHARED_RULES = "../references/shared-rules.md"  # as linked from skills/<name>/SKILL.md
MANIFEST_FIELDS = ("name", "version", "description", "author", "repository", "keywords", "license")
SEMVER = r"\d+\.\d+\.\d+(?:-[\w.-]+)?(?:\+[\w.-]+)?"


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
    """Raise on a broken local link; return the other files this file links to."""
    linked = set()
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
        if resolved != path:
            linked.add(resolved)
    return linked


def package_files(root):
    """Every shipped file: ROOT_FILES plus all non-hidden files under skills/."""
    skills = root / "skills"
    return [root / name for name in ROOT_FILES] + sorted(
        path for path in skills.rglob("*")
        if path.is_file() and not any(part.startswith(".") for part in path.relative_to(skills).parts)
    )


def check_files(root, files):
    skills = root / "skills"
    if skills.is_symlink() or any(path.is_symlink() for path in skills.rglob("*")):
        raise ValueError("Symlink under skills/")
    for path in files:
        if not path.is_file():
            raise ValueError(f"Missing package file: {path.relative_to(root)}")


def check_manifests(root):
    manifest = json.loads((root / "plugin.json").read_text())
    if manifest.get("name") != "pricing-plugin" or not re.fullmatch(SEMVER, manifest.get("version", "")):
        raise ValueError("plugin.json must name pricing-plugin with a semantic version")
    if manifest.get("license") != "MIT":
        raise ValueError("plugin.json must declare the MIT license")
    claude_manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
    for field in MANIFEST_FIELDS:
        if claude_manifest.get(field) != manifest.get(field):
            raise ValueError(f".claude-plugin/plugin.json differs from plugin.json: {field}")
    return manifest["version"]


def check_skills(root):
    folders = sorted(path.parent for path in (root / "skills").glob("*/SKILL.md"))
    if not folders:
        raise ValueError("No skills found under skills/")
    for folder in folders:
        source = (folder / "SKILL.md").read_text()
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", source, re.DOTALL)
        if not frontmatter:
            raise ValueError(f"Missing frontmatter: {folder.name}")
        fields = dict(re.findall(r"^([\w-]+):[ \t]*(.*)$", frontmatter[1], re.MULTILINE))
        if fields.get("name", "").strip("\'\"") != folder.name:
            raise ValueError(f"Frontmatter name does not match folder: {folder.name}")
        if not fields.get("description", "").strip().strip("\'\""):
            raise ValueError(f"Missing description: {folder.name}")
        # The shared rules must be linked before the skill's first step.
        intro = re.split(r"^(?:## |1\. )", prose(source[frontmatter.end():]), maxsplit=1, flags=re.M)[0]
        if SHARED_RULES not in set(link_targets(intro)):
            raise ValueError(f"{folder.name} must link the shared rules before its first step")
    return len(folders)


def check_package_links(root, files):
    """Links stay inside the package, and every supporting file is linked from somewhere."""
    allowed = set(files)
    linked = set()
    for path in files:
        if path.suffix != ".md":
            continue
        body = prose(path.read_text())
        if re.search(r"/(?:Users|home|private|tmp)/|[A-Za-z]:\\", body):
            raise ValueError(f"Absolute developer path in {path.relative_to(root)}")
        if "references/curriculum-repository" in body:
            raise ValueError(f"Ignored curriculum dependency in {path.relative_to(root)}")
        linked |= check_links(path, root, allowed)
    orphans = [path.relative_to(root) for path in files
               if path.is_relative_to(root / "skills") and path.name != "SKILL.md" and path not in linked]
    if orphans:
        raise ValueError(f"Nothing links to these files under skills/: {sorted(map(str, orphans))}")


def check_docs(root):
    paths = [root / name for name in DOCS]
    for directory in DOC_DIRS:
        paths.extend(sorted((root / directory).rglob("*.md")))
    for path in paths:
        check_links(path, root)
    return len(paths)


def check_package(root=ROOT):
    root = Path(root).resolve()
    files = package_files(root)
    check_files(root, files)
    version = check_manifests(root)
    skills = check_skills(root)
    check_package_links(root, files)
    docs = check_docs(root)
    return f"PASS: {skills} skills, version {version}, {len(files)} package files, {docs} docs"


if __name__ == "__main__":
    try:
        print(check_package())
    except (ValueError, OSError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
