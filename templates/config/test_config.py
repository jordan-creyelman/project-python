"""Verify environment settings without modifying global process state."""

import traceback

import pytest

from example_package.config import Settings, load_settings


def test_defaults_when_variables_are_missing() -> None:
    assert load_settings({}) == Settings(log_level="INFO", timeout_seconds=10)


def test_explicit_environment_values() -> None:
    result = load_settings({"PROJECT_LOG_LEVEL": "debug", "PROJECT_TIMEOUT_SECONDS": "25"})
    assert result == Settings(log_level="DEBUG", timeout_seconds=25)


@pytest.mark.parametrize("level", ["", "TRACE", "secret-token"])
def test_reject_invalid_log_level(level: str) -> None:
    with pytest.raises(ValueError, match="PROJECT_LOG_LEVEL"):
        load_settings({"PROJECT_LOG_LEVEL": level})


@pytest.mark.parametrize("timeout", ["", "abc", "0", "-1", "301", "3.5"])
def test_reject_invalid_timeout(timeout: str) -> None:
    with pytest.raises(ValueError, match="PROJECT_TIMEOUT_SECONDS"):
        load_settings({"PROJECT_TIMEOUT_SECONDS": timeout})


def test_error_does_not_echo_input_value() -> None:
    private_value = "do-not-log-this-value"
    with pytest.raises(ValueError) as error:
        load_settings({"PROJECT_TIMEOUT_SECONDS": private_value})
    assert private_value not in str(error.value)
    assert private_value not in "".join(
        traceback.format_exception(error.value)
    )


def test_use_process_environment_only_when_explicit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PROJECT_TIMEOUT_SECONDS", "12")
    assert load_settings().timeout_seconds == 12
    assert load_settings({}).timeout_seconds == 10
