"""Contain task rules without file or network access."""


def normalize_title(title: str) -> str:
    """Return a normalized task title or reject a blank one."""
    normalized = title.strip()
    if not normalized:
        raise ValueError("A task title cannot be empty.")
    return normalized
