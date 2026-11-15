"""Persist task titles as a JSON list."""

from __future__ import annotations

import json
from pathlib import Path


def load_tasks(path: Path) -> list[str]:
    """Load a validated list of task titles, defaulting to an empty list."""
    if not path.exists():
        return []
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list) or any(not isinstance(item, str) for item in tasks):
        raise ValueError("The task file must contain a JSON list of strings.")
    return tasks


def save_tasks(path: Path, tasks: list[str]) -> None:
    """Write tasks to an explicitly selected JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
