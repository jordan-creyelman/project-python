"""Count nonempty lines in a UTF-8 text file."""

from __future__ import annotations

import argparse
from pathlib import Path


def count_nonempty_lines(path: Path) -> int:
    """Return the number of nonempty lines in a text file."""
    return sum(bool(line.strip()) for line in path.read_text(encoding="utf-8").splitlines())


def main() -> int:
    """Read a file path from the CLI and print the nonempty line count."""
    parser = argparse.ArgumentParser(description="Count nonempty text lines.")
    parser.add_argument("path", type=Path, help="UTF-8 text file to inspect")
    args = parser.parse_args()
    try:
        count = count_nonempty_lines(args.path)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print(count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
