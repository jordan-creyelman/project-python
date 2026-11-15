"""Check that a Python project follows essential size-based standards.

This script intentionally uses only the Python standard library so it can
be copied into generated repositories without introducing dependencies.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path

SIZES = ("xs", "s", "m", "l")
IGNORED = {".git", ".venv", ".pytest_cache", ".ruff_cache", "dist", "build"}


@dataclass(frozen=True)
class Finding:
    """Describe one actionable convention failure or recommendation."""

    level: str
    message: str


def _read_config(root: Path) -> dict[str, object]:
    """Read the optional context marker and validate its basic structure."""
    marker = root / ".project-python.toml"
    if not marker.is_file():
        return {}
    with marker.open("rb") as stream:
        value = tomllib.load(stream)
    section = value.get("project-python", {})
    if not isinstance(section, dict):
        raise TypeError("Invalid [project-python] section.")
    return section


def _python_files(root: Path) -> list[Path]:
    """Return source files while ignoring generated environments and builds."""
    return [
        path
        for path in root.rglob("*.py")
        if not any(part in IGNORED for part in path.relative_to(root).parts)
    ]


def check_project(root: Path, size: str | None = None) -> list[Finding]:
    """Check enforceable project standards without accessing the network.

    The check cannot establish that a dependency is recently maintained or
    that every docstring is grammatically correct English. Review those
    requirements manually when adding dependencies or changing public APIs.
    """
    root = root.resolve()
    if not root.is_dir():
        return [Finding("error", f"Project directory does not exist: {root}")]

    findings: list[Finding] = []
    try:
        configuration = _read_config(root)
    except (OSError, TypeError, ValueError, tomllib.TOMLDecodeError) as exc:
        return [Finding("error", f"Invalid .project-python.toml: {exc}")]

    declared_size = configuration.get("size")
    size = size or declared_size
    if size not in SIZES:
        return [
            Finding(
                "error",
                "Specify --size xs|s|m|l or add [project-python] size to "
                ".project-python.toml.",
            )
        ]
    if declared_size is not None and declared_size != size:
        findings.append(
            Finding("error", "The requested size conflicts with the marker.")
        )

    if not _python_files(root):
        findings.append(Finding("error", "No Python source files were found."))

    for path in _python_files(root):
        try:
            source = path.read_text(encoding="utf-8")
            ast.parse(source, filename=str(path))
        except (UnicodeError, OSError, SyntaxError) as exc:
            findings.append(
                Finding(
                    "error", f"Invalid Python source in {path.relative_to(root)}: {exc}"
                )
            )

    environment_enabled = configuration.get("environment-config", False)
    if not isinstance(environment_enabled, bool):
        findings.append(Finding("error", "environment-config must be a boolean."))
    if size == "xs":
        if environment_enabled:
            findings.append(
                Finding("error", "Environment configuration is supported only for S/M.")
            )
        return findings

    if not (root / "README.md").is_file():
        findings.append(Finding("error", "README.md is missing."))

    pyproject = root / "pyproject.toml"
    metadata: dict[str, object] = {}
    if not pyproject.is_file():
        findings.append(
            Finding("error", "pyproject.toml is required for size S or above.")
        )
    else:
        try:
            with pyproject.open("rb") as stream:
                metadata = tomllib.load(stream)
        except (OSError, tomllib.TOMLDecodeError) as exc:
            findings.append(Finding("error", f"Invalid pyproject.toml: {exc}"))

    project = metadata.get("project", {})
    if not isinstance(project, dict):
        project = {}
    if not project.get("name"):
        findings.append(Finding("error", "Set [project].name in pyproject.toml."))
    if not project.get("requires-python"):
        findings.append(Finding("error", "Set [project].requires-python."))

    groups = metadata.get("dependency-groups", {})
    optional = project.get("optional-dependencies", {})
    if not isinstance(groups, dict):
        groups = {}
    if not isinstance(optional, dict):
        optional = {}
    dev_dependencies = groups.get("dev", optional.get("dev", []))
    if not isinstance(dev_dependencies, list):
        dev_dependencies = []
    names = {
        match.group(0).lower().replace("_", "-")
        for dep in dev_dependencies
        if (match := re.match(r"[A-Za-z0-9_.-]+", str(dep)))
    }
    for tool in ("pytest", "ruff"):
        if tool not in names:
            level = "warning" if size == "s" else "error"
            findings.append(
                Finding(level, f"Declare {tool} in development dependencies.")
            )

    tests = root / "tests"
    if not tests.is_dir() or not any(tests.rglob("test_*.py")):
        level = "warning" if size == "s" else "error"
        findings.append(Finding(level, "Add meaningful tests under tests/."))

    if not (root / "uv.lock").is_file():
        level = "warning" if size == "s" else "error"
        findings.append(Finding(level, "Commit uv.lock for a reproducible uv project."))

    gitignore = root / ".gitignore"
    ignored = gitignore.read_text(encoding="utf-8") if gitignore.is_file() else ""
    if ".venv" not in ignored:
        findings.append(Finding("warning", "Ignore the .venv/ environment in Git."))

    if environment_enabled:
        if not (root / ".env.example").is_file():
            findings.append(Finding("error", "Add a safe .env.example template."))
        if not (root / "tests" / "test_config.py").is_file():
            findings.append(
                Finding("error", "Test optional environment configuration.")
            )
        if ".env" not in ignored:
            findings.append(Finding("error", "Ignore .env files in Git."))
        project_name = str(project.get("name", "")).replace("-", "_")
        config_module = root / "src" / project_name / "config.py"
        if not config_module.is_file():
            findings.append(Finding("error", "Add a central config.py module."))

    workflow_dir = root / ".github" / "workflows"
    workflows = (
        [*workflow_dir.glob("*.yml"), *workflow_dir.glob("*.yaml")]
        if workflow_dir.is_dir()
        else []
    )
    if not workflows:
        level = "warning" if size == "s" else "error"
        findings.append(Finding(level, "Add GitHub Actions CI for this project."))

    return findings


def main(argv: list[str] | None = None) -> int:
    """Check a local project and report actionable findings."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, default=Path("."))
    parser.add_argument(
        "--size", choices=SIZES, help="Override or supply the project size."
    )
    parser.add_argument(
        "--strict", action="store_true", help="Treat warnings as failures."
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit machine-readable results."
    )
    args = parser.parse_args(argv)
    findings = check_project(args.path, args.size)
    errors = sum(item.level == "error" for item in findings)
    warnings = sum(item.level == "warning" for item in findings)
    if args.json:
        print(json.dumps([asdict(item) for item in findings], indent=2))
    else:
        for item in findings:
            print(f"{item.level.upper()}: {item.message}")
        print(f"Project standards: {errors} error(s), {warnings} warning(s).")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
