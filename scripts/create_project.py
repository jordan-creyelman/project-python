"""Generate a Python XS, S, or M starter from the project-python templates."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if __package__:
    from .check_project import check_project
else:
    from check_project import check_project

NAME_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
SIZES = ("xs", "s", "m")
STANDARDS_VERSION = "0.2.0"
SOURCE_ROOT = Path(__file__).resolve().parents[1]


def _readme(name: str, size: str) -> str:
    """Generate a self-contained README without links to parent templates."""
    if size == "xs":
        instructions = f"""uv run main.py example.txt
uv run python -m unittest discover -s tests -v"""
        purpose = "Standalone Python script to count nonempty lines in a UTF-8 text file."
    elif size == "s":
        instructions = f"""uv sync --locked
uv run --locked {name} 5 0.02
uv run --locked python -m pytest -q
uv run --locked ruff check .
uv run --locked ruff format --check .
uv build"""
        purpose = "Small, packaged Python CLI with pure calculation logic."
    else:
        instructions = f"""uv sync --locked
uv run --locked {name} --file tasks.json "Review schematic"
uv run --locked python -m pytest -q
uv run --locked ruff check .
uv run --locked ruff format --check .
uv build"""
        purpose = "Modular task application separating domain, service, and storage."

    return f"""# {name}

{purpose}

Generated from [project-python](https://github.com/jordan-creyelman/project-python)
standards v{STANDARDS_VERSION} (size {size.upper()}).

## Run

Install [uv](https://docs.astral.sh/uv/getting-started/installation/),
then run:

\`\`\`bash
{instructions}
\`\`\`

## Conventions

- Python docstrings and Git commit messages: English.
- Choose maintained libraries with an active community; standard library first.
- Keep changes small, add meaningful tests, and use conventional commits.
- With CI enabled, run \`python scripts/check_project.py --path . --strict\`.
- \`uv.lock\` is committed for reproducible installations in S/M projects.

See the [standard reference](https://github.com/jordan-creyelman/project-python/blob/main/docs/STANDARDS_INDEX.md).
"""


def _rewrite_names(root: Path, size: str, name: str) -> None:
    """Rename example packages and update project metadata and imports."""
    if size == "xs":
        return
    previous_name = "example-cli" if size == "s" else "example-app"
    previous_module = "example_cli" if size == "s" else "example_app"
    module = name.replace("-", "_")
    source = root / "src" / previous_module
    if not source.is_dir():
        raise FileNotFoundError(f"Missing template package: {source}")
    source.rename(root / "src" / module)

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in (".py", ".toml", ".md"):
            continue
        original = path.read_text(encoding="utf-8")
        updated = original.replace(previous_module, module).replace(previous_name, name)
        if updated != original:
            path.write_text(updated, encoding="utf-8")


def create_project(
    name: str,
    size: str,
    parent: Path,
    *,
    ci: bool = True,
    lock: bool = True,
) -> Path:
    """Create a project atomically, refusing unsafe names and existing paths.

    For S/M, lock dependencies with uv before enabling the generated CI.
    A failed lock or failed standards check leaves no partial project.
    """
    if not NAME_RE.fullmatch(name):
        raise ValueError(
            "Use a lowercase project name such as sensor-cli "
            "(letters, digits, and single hyphens)."
        )
    if size not in SIZES:
        raise ValueError("Size must be xs, s, or m.")

    parent = parent.expanduser().resolve()
    if not parent.is_dir():
        raise ValueError(f"Parent directory does not exist: {parent}")
    destination = parent / name
    if destination.exists():
        raise FileExistsError(f"Destination already exists: {destination}")

    if size == "xs":
        ci = False
        lock = False
    elif ci and not lock:
        raise ValueError("CI requires a committed uv.lock; omit --no-lock.")
    elif lock and shutil.which("uv") is None:
        raise RuntimeError(
            "uv is required to generate uv.lock. Install it from "
            "https://docs.astral.sh/uv/ or pass --no-ci --no-lock."
        )

    template = SOURCE_ROOT / "templates" / size
    with tempfile.TemporaryDirectory(prefix=f".{name}-", dir=parent) as temp:
        staging = Path(temp) / name
        shutil.copytree(
            template,
            staging,
            ignore=shutil.ignore_patterns(
                ".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "uv.lock"
            ),
        )
        _rewrite_names(staging, size, name)
        (staging / "README.md").write_text(_readme(name, size), encoding="utf-8")
        (staging / ".project-python.toml").write_text(
            f'[project-python]\nsize = "{size}"\nstandards-version = "{STANDARDS_VERSION}"\n',
            encoding="utf-8",
        )

        if size != "xs":
            portable_checker = staging / "scripts" / "check_project.py"
            portable_checker.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(SOURCE_ROOT / "scripts" / "check_project.py", portable_checker)

            if ci:
                workflow = staging / ".github" / "workflows" / "python-ci.yml"
                workflow.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(
                    SOURCE_ROOT / "templates" / "github" / "workflows" / "python-ci.yml",
                    workflow,
                )
            if lock:
                try:
                    subprocess.run(
                        ["uv", "lock"],
                        cwd=staging,
                        check=True,
                        capture_output=True,
                        text=True,
                    )
                except subprocess.CalledProcessError as exc:
                    raise RuntimeError(f"uv lock failed:\n{exc.stderr}") from exc

        findings = check_project(staging)
        errors = [finding.message for finding in findings if finding.level == "error"]
        if errors and not (size == "m" and not ci and not lock):
            raise ValueError("Generated project failed validation:\n" + "\n".join(errors))
        if destination.exists():
            raise FileExistsError(f"Destination already exists: {destination}")
        staging.rename(destination)

    return destination


def main(argv: list[str] | None = None) -> int:
    """Parse generator options and create the requested project."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Lowercase project name, e.g. sensor-cli")
    parser.add_argument("--size", required=True, choices=SIZES)
    parser.add_argument("--parent", type=Path, default=Path("."))
    parser.add_argument("--no-ci", action="store_true", help="Skip GitHub Actions CI.")
    parser.add_argument("--no-lock", action="store_true", help="Skip generating uv.lock.")
    args = parser.parse_args(argv)
    try:
        created = create_project(
            args.name,
            args.size,
            args.parent,
            ci=not args.no_ci,
            lock=not args.no_lock,
        )
    except (ValueError, FileExistsError, OSError, RuntimeError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print(f"Created {created}")
    print("Inspect the README and files before committing to GitHub.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
