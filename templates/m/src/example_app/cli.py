"""Offer a small command-line interface for the task service."""

from __future__ import annotations

import argparse
from pathlib import Path

from example_app.service import add_task


def main() -> int:
    """Add a task to the selected JSON file."""
    parser = argparse.ArgumentParser(description="Add a task to a JSON file.")
    parser.add_argument("title", help="Task title")
    parser.add_argument("--file", type=Path, required=True, help="Task JSON file")
    args = parser.parse_args()
    try:
        tasks = add_task(args.file, args.title)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Stored {len(tasks)} task(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
