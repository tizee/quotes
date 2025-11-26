#!/usr/bin/env python3
"""
Append quotes from one or more JSON files into a base quotes JSON file.

Usage:
    python scripts/merge_quotes.py base.json add1.json [add2.json ...]

Notes:
- The first path is modified in place.
- Each input file must contain a top-level \"quotes\" array.
- The script preserves other top-level fields (e.g., \"$schema\", \"name\").
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List


def load_quotes(path: Path) -> dict:
    """Load a quotes JSON file and validate it has a quotes array."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - thin CLI
        raise SystemExit(f"[error] Failed to read {path}: {exc}")

    if "quotes" not in data or not isinstance(data["quotes"], list):
        raise SystemExit(f"[error] {path} does not contain a top-level 'quotes' array")
    return data


def merge(base_path: Path, additions: List[Path]) -> None:
    base_data = load_quotes(base_path)
    base_quotes = base_data["quotes"]
    before = len(base_quotes)

    for extra_path in additions:
        extra_data = load_quotes(extra_path)
        base_quotes.extend(extra_data["quotes"])

    after = len(base_quotes)
    base_path.write_text(json.dumps(base_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[ok] Merged {len(additions)} file(s) into {base_path}")
    print(f"[ok] Quotes: {before} -> {after}")


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge quotes JSON files.")
    parser.add_argument(
        "files",
        nargs="+",
        type=Path,
        help="Files to merge: first is the base file to update; the rest are appended.",
    )
    return parser.parse_args(argv)


def main(argv: List[str]) -> None:
    args = parse_args(argv)
    if len(args.files) < 2:
        raise SystemExit("[error] Provide at least two files: base.json new.json [...]")

    base, *rest = args.files
    merge(base, rest)


if __name__ == "__main__":
    main(sys.argv[1:])
