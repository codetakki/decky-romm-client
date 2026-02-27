#!/bin/bash
# Deploy built plugin locally to ~/homebrew/plugins/ (for WSL2 / desktop dev)
set -e

WORKSPACE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Derive plugin name from plugin.json (single source of truth)
PLUGIN_JSON_NAME="$(python3 -c "import json; print(json.load(open('${WORKSPACE_DIR}/plugin.json'))['name'])")"
# Folder name on disk uses hyphens instead of spaces
PLUGIN_NAME="${PLUGIN_JSON_NAME// /-}"

HOMEBREW_PLUGINS="$HOME/homebrew/plugins"
PLUGIN_DIR="${HOMEBREW_PLUGINS}/${PLUGIN_NAME}"
OUT_DIR="${WORKSPACE_DIR}/out"

echo "=== Local Deploy: ${PLUGIN_NAME} ==="

# Check that out/ exists (plugin was built)
if [ ! -d "$OUT_DIR" ] || [ -z "$(ls -A "$OUT_DIR" 2>/dev/null)" ]; then
    echo "ERROR: No build output found in ${OUT_DIR}"
    echo "Run the 'build' task first."
    exit 1
fi

# Check that homebrew/plugins exists
if [ ! -d "$HOMEBREW_PLUGINS" ]; then
    echo "ERROR: Decky plugins directory not found at ${HOMEBREW_PLUGINS}"
    echo "Install Decky Loader first: bash scripts/install-decky.sh"
    exit 1
fi

echo "[1/3] Cleaning previous deployment..."
sudo rm -rf "${PLUGIN_DIR}"
sudo mkdir -p "${PLUGIN_DIR}"

echo "[2/3] Extracting plugin..."
# Find the zip in out/
ZIP_FILE=$(find "$OUT_DIR" -name "*.zip" -type f | head -1)
if [ -n "$ZIP_FILE" ]; then
    echo "  -> Extracting: $(basename "$ZIP_FILE")"
    # Extract to a temp dir first, then move contents (the zip has a nested folder)
    TMPDIR=$(mktemp -d)
    sudo unzip -o "$ZIP_FILE" -d "$TMPDIR" >/dev/null 2>&1
    # The zip contains a top-level folder — move its contents up
    INNER_DIR=$(find "$TMPDIR" -mindepth 1 -maxdepth 1 -type d | head -1)
    if [ -n "$INNER_DIR" ]; then
        sudo cp -r "$INNER_DIR"/* "${PLUGIN_DIR}/"
    else
        sudo cp -r "$TMPDIR"/* "${PLUGIN_DIR}/"
    fi
    sudo rm -rf "$TMPDIR"
else
    echo "  -> No zip found, copying out/ directly..."
    sudo cp -r "$OUT_DIR"/* "${PLUGIN_DIR}/"
fi

echo "[3/3] Setting permissions..."
sudo chown -R "$(whoami):$(whoami)" "${PLUGIN_DIR}"
sudo chmod -R 755 "${PLUGIN_DIR}"

echo ""
echo "=== Deployed to: ${PLUGIN_DIR} ==="
ls -la "${PLUGIN_DIR}/"
echo ""

# Restart Decky Loader to pick up changes
echo "Restarting Decky Loader..."
sudo systemctl restart plugin_loader 2>/dev/null && echo "  -> Done" || echo "  -> plugin_loader service not running (start Steam first)"
echo ""
