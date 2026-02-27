"""Pytest conftest – auto-loads .env.test for integration tests."""

import os
from pathlib import Path


def _load_env_file(path: Path) -> None:
    """Minimal .env loader (no extra dependency needed)."""
    if not path.is_file():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key:
            os.environ.setdefault(key, value)


# Load .env.test from the rom-m-api-client directory
_load_env_file(Path(__file__).resolve().parent.parent / ".env.test")
