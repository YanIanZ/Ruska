#!/usr/bin/env python3
"""Validate local Markdown links and JSON schemas. Not a full markdown linter."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def main():
    missing = []
    files = list(ROOT.rglob("*.md"))
    # Markdown normal inline links; ignore remote destinations, anchors and code interpolation.
    for file in files:
        content = file.read_text(encoding="utf-8")
        for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
            target = link.split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            dest = (file.parent / unquote(target)).resolve()
            if not dest.exists():
                missing.append(f"{file.relative_to(ROOT)} -> {target}")
    schemas = list((ROOT / "schemas").glob("*.json"))
    for schema in schemas:
        obj = json.loads(schema.read_text(encoding="utf-8"))
        assert isinstance(obj, dict) and obj.get("type") == "object", schema.name
    if missing:
        print("Broken local links:\n" + "\n".join(missing), file=sys.stderr)
        return 1
    print(f"PASS: {len(files)} Markdown files and {len(schemas)} JSON schemas checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
