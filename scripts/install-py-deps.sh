#!/bin/bash
# Install Python dependencies into py_modules/ for bundling with the plugin
set -e

WORKSPACE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PY_MODULES="${WORKSPACE_DIR}/py_modules"
SDK_DIR="${WORKSPACE_DIR}/rom-m-api-client"

echo "=== Installing Python dependencies into py_modules/ ==="

# Clean existing (except .keep)
find "$PY_MODULES" -mindepth 1 ! -name '.keep' -exec rm -rf {} + 2>/dev/null || true

# Install the SDK and all its dependencies
pip install --target "$PY_MODULES" "$SDK_DIR/" --quiet 2>&1

# Copy the high-level wrapper as a proper module
cp "$SDK_DIR/romm-client.py" "$PY_MODULES/romm_client.py"

echo "=== Done. Contents of py_modules/: ==="
ls "$PY_MODULES/" | grep -v dist-info | grep -v __pycache__
