"""Validate Markdown links, YAML, TOML, and Python syntax in this repository."""

from __future__ import annotations

import re
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

LINK_RE = re.compile(r'!?\[[^\]\n]+\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)')
FENCE_RE = re.compile(r"^\s*('''|\x60{3,}|~{3,})")


def strip_fenced_blocks(markdown: str) -> str:
    """Remove fenced code blocks before searching for Markdown links."""
    lines: list[str] = []
    marker: str | None = None
    for line in markdown.splitlines():
        fence = FENCE_RE.match(line)
        if fence:
            current = fence.group(1)
            if marker is None:
                marker = current
            elif current[0] == marker[0] and len(current) >= len(marker):
                marker = None
            continue
        if marker is None:
            lines.append(line)
    return "\n".join(lines)


def check_links(root: Path) -> list[str]:
    """Report links leaving the repository or targeting absent local files."""
    errors: list[str] = []
    for markdown in sorted(root.rglob("*.md")):
        if any(part in {".venv", ".git", ".pytest_cache"} for part in markdown.parts):
            continue
        body = strip_fenced_blocks(markdown.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(body):
            raw = match.group(1).strip("<>")
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc or raw.startswith("#") or not parsed.path:
                continue
            target = (markdown.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f"{markdown.relative_to(root)}: broken link {raw}")
    return errors


def check_syntax(root: Path) -> list[str]:
    """Parse YAML and TOML and compile Python source without executing it."""
    errors: list[str] = []
    for path in sorted([*root.rglob("*.yml"), *root.rglob("*.yaml")]):
        try:
            mapping = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
            if not isinstance(mapping, dict):
                raise ValueError("expected a mapping")
        except (yaml.YAMLError, ValueError) as exc:
            errors.append(f"{path.relative_to(root)}: YAML error: {exc}")
    for path in sorted(root.rglob("pyproject.toml")):
        try:
            tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"{path.relative_to(root)}: TOML error: {exc}")
    for path in sorted(root.rglob("*.py")):
        if any(part in {".venv", ".git"} for part in path.parts):
            continue
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            errors.append(f"{path.relative_to(root)}: Python error: {exc}")
    return errors


def main() -> int:
    """Validate the repository and return a process-friendly exit status."""
    root = Path(__file__).resolve().parents[1]
    errors = check_links(root) + check_syntax(root)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"Validation failed: {len(errors)} issue(s).")
        return 1
    print("Markdown links, YAML, TOML, and Python syntax: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
