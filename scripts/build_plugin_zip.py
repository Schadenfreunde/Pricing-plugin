"""Build the Claude upload ZIP: the manifests, license and skills/ in one pricing-plugin/ folder."""

import argparse
import zipfile
from pathlib import Path

from check_package import ROOT, check_package, package_files


def build_plugin_zip(root, destination):
    root = Path(root).resolve()
    destination = Path(destination).resolve()
    check_package(root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in package_files(root):
            archive.write(path, f"pricing-plugin/{path.relative_to(root).as_posix()}")
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output/pricing-plugin-claude.zip")
    args = parser.parse_args()
    print(build_plugin_zip(ROOT, args.output))
