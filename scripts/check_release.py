"""Validate a versioned documentation release and extract its notes."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
ENTRY_RE = re.compile(
    r"^## \[(?P<version>\d+\.\d+\.\d+)\] - (?P<date>\d{4}-\d{2}-\d{2})\s*$",
    re.MULTILINE,
)


def validate_release(root: Path, expected: str | None = None) -> tuple[str, str]:
    """Return the declared version and nonempty changelog notes for that version."""
    version_file = root / "VERSION"
    changelog_file = root / "CHANGELOG.md"
    if not version_file.is_file() or not changelog_file.is_file():
        raise ValueError("VERSION and CHANGELOG.md must both exist.")

    version = version_file.read_text(encoding="utf-8").strip()
    if not VERSION_RE.fullmatch(version):
        raise ValueError(f"VERSION is not MAJOR.MINOR.PATCH: {version!r}.")
    if expected is not None and expected != version:
        raise ValueError(f"Requested version {expected!r} != VERSION {version!r}.")

    changelog = changelog_file.read_text(encoding="utf-8")
    matches = list(ENTRY_RE.finditer(changelog))
    entries = [entry for entry in matches if entry.group("version") == version]
    if len(entries) != 1:
        raise ValueError(f"Expected one changelog entry for [{version}].")

    entry = entries[0]
    try:
        date.fromisoformat(entry.group("date"))
    except ValueError as exc:
        raise ValueError(f"Invalid release date for [{version}].") from exc

    section_end = changelog.find("\n## ", entry.end())
    notes = changelog[entry.end() : section_end if section_end >= 0 else None].strip()
    if not notes or not re.search(r"(?m)^\s*[-*] \S", notes):
        raise ValueError(f"Changelog entry [{version}] has no substantive notes.")
    return version, notes


def main(argv: list[str] | None = None) -> int:
    """Validate metadata without publishing a tag or GitHub Release."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, default=Path("."))
    parser.add_argument("--version", help="Expected version, without the v prefix.")
    parser.add_argument(
        "--notes-file", type=Path, help="Write validated release notes."
    )
    args = parser.parse_args(argv)
    try:
        version, notes = validate_release(args.path, args.version)
        if args.notes_file is not None:
            args.notes_file.write_text(notes + "\n", encoding="utf-8")
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Version v{version}: validated changelog ({len(notes)} characters).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
