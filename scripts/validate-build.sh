#!/bin/bash
# Validate that the built plugin zip contains all required files and
# that the packaged code matches the current source.
set -e

WORKSPACE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="${WORKSPACE_DIR}/out"

# Derive expected names from plugin.json
PLUGIN_JSON_NAME="$(python3 -c "import json; print(json.load(open('${WORKSPACE_DIR}/plugin.json'))['name'])")"
ZIP_FILE="${OUT_DIR}/${PLUGIN_JSON_NAME}.zip"

echo "=== Validating plugin build ==="
echo "  Plugin name : ${PLUGIN_JSON_NAME}"
echo "  Expected zip: ${ZIP_FILE}"
echo ""

ERRORS=0

# ---------------------------------------------------------------
# 1. Zip exists
# ---------------------------------------------------------------
if [ ! -f "$ZIP_FILE" ]; then
    echo "FAIL: Zip file not found: ${ZIP_FILE}"
    # Try to show what IS in out/
    echo "  Contents of ${OUT_DIR}/:"
    ls -la "$OUT_DIR/" 2>/dev/null || echo "  (directory does not exist)"
    exit 1
fi
echo "OK   Zip exists"

# ---------------------------------------------------------------
# 2. Required files inside the zip
# ---------------------------------------------------------------
REQUIRED_FILES=(
    "${PLUGIN_JSON_NAME}/plugin.json"
    "${PLUGIN_JSON_NAME}/main.py"
    "${PLUGIN_JSON_NAME}/package.json"
    "${PLUGIN_JSON_NAME}/dist/index.js"
    "${PLUGIN_JSON_NAME}/py_modules/romm_client.py"
)

ZIP_LISTING="$(python3 -c "import zipfile; z=zipfile.ZipFile('${ZIP_FILE}'); print('\n'.join(z.namelist()))")"

for f in "${REQUIRED_FILES[@]}"; do
    if echo "$ZIP_LISTING" | grep -qF "$f"; then
        echo "OK   Contains ${f}"
    else
        echo "FAIL Missing ${f}"
        ERRORS=$((ERRORS + 1))
    fi
done

# ---------------------------------------------------------------
# 3. Key code markers in main.py (ensure new features are included)
# ---------------------------------------------------------------
MAIN_PY="$(python3 -c "import zipfile; z=zipfile.ZipFile('${ZIP_FILE}'); print(z.read('${PLUGIN_JSON_NAME}/main.py').decode())")"

MARKERS=(
    "async def download_rom"
    "def _extract_zip"
    "import zipfile"
    "async def search_roms"
    "async def get_platforms"
    "async def romm_login"
    "async def get_download_status"
)

for marker in "${MARKERS[@]}"; do
    if echo "$MAIN_PY" | grep -qF "$marker"; then
        echo "OK   main.py contains '${marker}'"
    else
        echo "FAIL main.py missing '${marker}'"
        ERRORS=$((ERRORS + 1))
    fi
done

# ---------------------------------------------------------------
# 4. Key code markers in dist/index.js (frontend)
# ---------------------------------------------------------------
INDEX_JS="$(python3 -c "import zipfile; z=zipfile.ZipFile('${ZIP_FILE}'); print(z.read('${PLUGIN_JSON_NAME}/dist/index.js').decode())")"

JS_MARKERS=(
    "download_rom"
    "Download Complete"
    "search_roms"
)

for marker in "${JS_MARKERS[@]}"; do
    if echo "$INDEX_JS" | grep -qF "$marker"; then
        echo "OK   index.js contains '${marker}'"
    else
        echo "FAIL index.js missing '${marker}'"
        ERRORS=$((ERRORS + 1))
    fi
done

# ---------------------------------------------------------------
# 5. Verify rom_m_api_client SDK is bundled
# ---------------------------------------------------------------
if echo "$ZIP_LISTING" | grep -q "rom_m_api_client/"; then
    echo "OK   rom_m_api_client/ SDK bundled"
else
    echo "FAIL rom_m_api_client/ SDK not found in zip"
    ERRORS=$((ERRORS + 1))
fi

# ---------------------------------------------------------------
# 6. Verify plugin.json name inside zip matches expected
# ---------------------------------------------------------------
INNER_NAME="$(python3 -c "
import zipfile, json
z = zipfile.ZipFile('${ZIP_FILE}')
pj = json.loads(z.read('${PLUGIN_JSON_NAME}/plugin.json'))
print(pj['name'])
")"

if [ "$INNER_NAME" = "$PLUGIN_JSON_NAME" ]; then
    echo "OK   plugin.json name matches: '${INNER_NAME}'"
else
    echo "FAIL plugin.json name mismatch: expected '${PLUGIN_JSON_NAME}', got '${INNER_NAME}'"
    ERRORS=$((ERRORS + 1))
fi

# ---------------------------------------------------------------
# 7. Verify package.json has no template defaults
# ---------------------------------------------------------------
PKG_NAME="$(python3 -c "
import zipfile, json
z = zipfile.ZipFile('${ZIP_FILE}')
pkg = json.loads(z.read('${PLUGIN_JSON_NAME}/package.json'))
print(pkg.get('name', ''))
")"

if [ "$PKG_NAME" = "decky-plugin-template" ]; then
    echo "FAIL package.json still has template name 'decky-plugin-template'"
    ERRORS=$((ERRORS + 1))
elif [ -z "$PKG_NAME" ]; then
    echo "FAIL package.json has no name field"
    ERRORS=$((ERRORS + 1))
else
    echo "OK   package.json name: '${PKG_NAME}'"
fi

# ---------------------------------------------------------------
# 8. No dummy template backend binary (bin/hello)
# ---------------------------------------------------------------
if echo "$ZIP_LISTING" | grep -q "${PLUGIN_JSON_NAME}/bin/hello"; then
    echo "FAIL Template backend binary 'bin/hello' found in zip — remove backend/ directory"
    ERRORS=$((ERRORS + 1))
else
    echo "OK   No template backend binary"
fi

# ---------------------------------------------------------------
# Summary
# ---------------------------------------------------------------
echo ""
if [ $ERRORS -eq 0 ]; then
    echo "=== All checks passed ==="
else
    echo "=== ${ERRORS} check(s) FAILED ==="
    exit 1
fi
