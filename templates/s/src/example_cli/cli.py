"""Expose the electrical power calculator as a command-line tool."""

from __future__ import annotations

import argparse

from example_cli.core import calculate_power


def main() -> int:
    """Parse electrical inputs and display calculated power."""
    parser = argparse.ArgumentParser(description="Calculate power in watts.")
    parser.add_argument("voltage_v", type=float, help="Voltage in volts")
    parser.add_argument("current_a", type=float, help="Current in amperes")
    args = parser.parse_args()
    try:
        power = calculate_power(args.voltage_v, args.current_a)
    except ValueError as exc:
        parser.error(str(exc))
    print(f"{power:g} W")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
