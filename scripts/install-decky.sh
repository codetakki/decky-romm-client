#!/bin/bash
# Non-interactive Decky Loader installer for WSL2 / Linux desktop development
# Based on: https://github.com/SteamDeckHomebrew/decky-installer
set -e

BRANCH="${1:-release}"
USER_DIR="$HOME"
HOMEBREW_FOLDER="${USER_DIR}/homebrew"

echo "=== Decky Loader Installer (non-interactive, branch: ${BRANCH}) ==="

# Check dependencies
for cmd in jq curl; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "ERROR: $cmd is required but not found. Install it first."
        exit 1
    fi
done

# Check if github.com is reachable
if ! curl -Is https://github.com | head -1 | grep 200 >/dev/null; then
    echo "ERROR: GitHub is unreachable. Check your internet connection."
    exit 1
fi

echo "[1/6] Creating directory structure..."
mkdir -p "${HOMEBREW_FOLDER}/services"
mkdir -p "${HOMEBREW_FOLDER}/plugins"

echo "[2/6] Enabling CEF remote debugging..."
# Native Steam
if [ -d "${USER_DIR}/.steam/steam" ]; then
    touch "${USER_DIR}/.steam/steam/.cef-enable-remote-debugging"
    echo "  -> ${USER_DIR}/.steam/steam/.cef-enable-remote-debugging"
fi
# Flatpak Steam
if [ -d "${USER_DIR}/.var/app/com.valvesoftware.Steam/data/Steam/" ]; then
    touch "${USER_DIR}/.var/app/com.valvesoftware.Steam/data/Steam/.cef-enable-remote-debugging"
    echo "  -> Flatpak Steam dir"
fi

echo "[3/6] Finding latest ${BRANCH}..."
if [ "$BRANCH" = "prerelease" ]; then
    RELEASE=$(curl -s 'https://api.github.com/repos/SteamDeckHomebrew/decky-loader/releases' | jq -r 'first(.[] | select(.prerelease == true))')
else
    RELEASE=$(curl -s 'https://api.github.com/repos/SteamDeckHomebrew/decky-loader/releases' | jq -r 'first(.[] | select(.prerelease == false))')
fi

VERSION=$(jq -r '.tag_name' <<< "${RELEASE}")
DOWNLOADURL=$(jq -r '.assets[].browser_download_url | select(endswith("PluginLoader"))' <<< "${RELEASE}")

if [ -z "$VERSION" ] || [ "$VERSION" = "null" ]; then
    echo "ERROR: Could not determine latest version."
    exit 1
fi

echo "  -> Version: ${VERSION}"
echo "  -> URL: ${DOWNLOADURL}"

echo "[4/6] Downloading PluginLoader..."
curl -L "$DOWNLOADURL" -o "${HOMEBREW_FOLDER}/services/PluginLoader" --progress-bar
chmod +x "${HOMEBREW_FOLDER}/services/PluginLoader"
echo "$VERSION" > "${HOMEBREW_FOLDER}/services/.loader.version"

# SELinux fix
if hash getenforce 2>/dev/null && getenforce | grep "Enforcing" >/dev/null; then
    chcon -t bin_t "${HOMEBREW_FOLDER}/services/PluginLoader"
fi

echo "[5/6] Setting up systemd service..."
# Stop existing if running
sudo systemctl stop plugin_loader 2>/dev/null || true
sudo systemctl disable plugin_loader 2>/dev/null || true

# Download official service file
curl -sL "https://raw.githubusercontent.com/SteamDeckHomebrew/decky-loader/main/dist/plugin_loader-${BRANCH}.service" \
    --output "${HOMEBREW_FOLDER}/services/plugin_loader-${BRANCH}.service" 2>/dev/null || true

# Create backup service file
cat > "${HOMEBREW_FOLDER}/services/plugin_loader-backup.service" <<- EOM
[Unit]
Description=SteamDeck Plugin Loader
After=network-online.target
Wants=network-online.target
[Service]
Type=simple
User=root
Restart=always
ExecStart=${HOMEBREW_FOLDER}/services/PluginLoader
WorkingDirectory=${HOMEBREW_FOLDER}/services
KillSignal=SIGKILL
Environment=PLUGIN_PATH=${HOMEBREW_FOLDER}/plugins
Environment=LOG_LEVEL=DEBUG
[Install]
WantedBy=multi-user.target
EOM

if [ -f "${HOMEBREW_FOLDER}/services/plugin_loader-${BRANCH}.service" ]; then
    echo "  -> Using official ${BRANCH} service file"
    sed -i -e "s|\${HOMEBREW_FOLDER}|${HOMEBREW_FOLDER}|" "${HOMEBREW_FOLDER}/services/plugin_loader-${BRANCH}.service"
    sudo cp -f "${HOMEBREW_FOLDER}/services/plugin_loader-${BRANCH}.service" "/etc/systemd/system/plugin_loader.service"
else
    echo "  -> Using backup service file"
    sudo cp "${HOMEBREW_FOLDER}/services/plugin_loader-backup.service" "/etc/systemd/system/plugin_loader.service"
fi

# Save copies
mkdir -p "${HOMEBREW_FOLDER}/services/.systemd"
cp "${HOMEBREW_FOLDER}/services/plugin_loader-backup.service" "${HOMEBREW_FOLDER}/services/.systemd/" 2>/dev/null || true
[ -f "${HOMEBREW_FOLDER}/services/plugin_loader-${BRANCH}.service" ] && \
    cp "${HOMEBREW_FOLDER}/services/plugin_loader-${BRANCH}.service" "${HOMEBREW_FOLDER}/services/.systemd/" 2>/dev/null || true

sudo systemctl daemon-reload

echo "[6/6] Starting Decky Loader service..."
sudo systemctl enable plugin_loader
sudo systemctl start plugin_loader

echo ""
echo "=== Decky Loader ${VERSION} installed successfully! ==="
echo ""
echo "Homebrew directory: ${HOMEBREW_FOLDER}"
echo "Plugins directory:  ${HOMEBREW_FOLDER}/plugins"
echo "Service status:     sudo systemctl status plugin_loader"
echo ""
echo "Next steps:"
echo "  1. Launch Steam in Big Picture / Game Mode"
echo "  2. Decky menu should appear (press ... button or Ctrl+2)"
echo ""
