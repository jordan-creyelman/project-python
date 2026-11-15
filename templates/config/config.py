"""Load explicitly selected application settings from the environment."""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass

ALLOWED_LOG_LEVELS = frozenset({"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"})


@dataclass(frozen=True)
class Settings:
    """Store validated, immutable application settings."""

    log_level: str = "INFO"
    timeout_seconds: int = 10


def load_settings(environ: Mapping[str, str] | None = None) -> Settings:
    """Validate settings without reading or logging secret values.

    Args:
        environ: Optional mapping for isolated tests. Defaults to os.environ.

    Returns:
        Validated application settings.

    Raises:
        ValueError: If a configured value is unsupported or out of range.
    """
    values = os.environ if environ is None else environ
    log_level = values.get("PROJECT_LOG_LEVEL", "INFO").strip().upper()
    if log_level not in ALLOWED_LOG_LEVELS:
        raise ValueError(
            "PROJECT_LOG_LEVEL must be DEBUG, INFO, WARNING, ERROR, or CRITICAL."
        )

    raw_timeout = values.get("PROJECT_TIMEOUT_SECONDS", "10").strip()
    try:
        timeout_seconds = int(raw_timeout)
    except ValueError:
        raise ValueError("PROJECT_TIMEOUT_SECONDS must be an integer.") from None
    if not 1 <= timeout_seconds <= 300:
        raise ValueError("PROJECT_TIMEOUT_SECONDS must be between 1 and 300.")

    return Settings(log_level=log_level, timeout_seconds=timeout_seconds)
