# Optional environment configuration template

This template is **not copied by default**. Use the project generator
with the `--with-env` flag for a new S or M project.

- `config.py` demonstrates immutable, validated settings with only the standard library.
- `test_config.py` verifies defaults, invalid values, overrides and no sensitive input in errors.
- `.env.example` contains safe example values and never any real secret.
- Generated names use a project-specific prefix, for example `SENSOR_CLI_LOG_LEVEL`.
- The feature does not automatically add configuration requirements to business logic.

Copy `.env.example` to `.env` only if you need local overrides, and load it explicitly
with `uv run --env-file .env ...`. Real deployment secrets belong in a secrets manager
or secure environment variables, not in committed files.

See [the configuration convention](../../docs/CONFIGURATION.md).
