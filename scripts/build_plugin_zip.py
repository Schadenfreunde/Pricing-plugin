"""Build a complete Claude upload bundle without local data or evaluation files."""

import argparse
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from check_package import RUNTIME_PATHS, check_package


def build_plugin_zip(root, destination):
    root = Path(root).resolve()
    destination = Path(destination).resolve()
    check_package(root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in RUNTIME_PATHS:
            # Installation docs link to development fixtures; keep them in the repository.
            if relative not in ("README.md", "INSTALL.md"):
                archive.write(root / relative, f"pricing-plugin/{relative}")
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output/pricing-plugin-claude.zip")
    args = parser.parse_args()
    print(build_plugin_zip(ROOT, args.output))
