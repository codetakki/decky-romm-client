import os
import sys

# The decky plugin module is located at decky-loader/plugin
# For easy intellisense checkout the decky-loader code repo
# and add the `decky-loader/plugin/imports` path to `python.analysis.extraPaths` in `.vscode/settings.json`
import decky
import asyncio
from settings import SettingsManager
from decky import logger

# Make the rom-m-api-client package importable
PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
ROM_CLIENT_DIR = os.path.join(PLUGIN_DIR, "rom-m-api-client")
if ROM_CLIENT_DIR not in sys.path:
    sys.path.insert(0, ROM_CLIENT_DIR)

import importlib.util
_spec = importlib.util.spec_from_file_location(
    "romm_client", os.path.join(ROM_CLIENT_DIR, "romm-client.py")
)
_romm_mod = importlib.util.module_from_spec(_spec)
sys.modules["romm_client"] = _romm_mod
_spec.loader.exec_module(_romm_mod)

RommClient = _romm_mod.RommClient

import os
settings = SettingsManager(name="settings-romm-client")
settings.read()

# Shared RomM client instance (created on login, reused across calls)
_romm_client = None


class Plugin:    
    async def settings_read(self):
        logger.info('Reading settings')
        return settings.read()
    async def settings_commit(self):
        logger.info('Saving settings')
        return settings.commit()
    async def settings_getSetting(self, key: str, defaults):
        logger.info('Get {}'.format(key))
        return settings.getSetting(key, defaults)
    async def settings_setSetting(self, key: str, value):
        logger.info('Set {}: {}'.format(key, value))
        return settings.setSetting(key, value)

    # ------------------------------------------------------------------
    # RomM API bridge
    # ------------------------------------------------------------------

    async def romm_login(self):
        """Log in to RomM using the saved settings. Returns True on success."""
        global _romm_client
        url = settings.getSetting("rommUrl", "")
        user = settings.getSetting("username", "")
        passwd = settings.getSetting("password", "")
        if not url or not user or not passwd:
            raise ValueError("RomM connection settings are incomplete. Configure them in Settings.")
        logger.info("Logging in to RomM at {}".format(url))
        client = RommClient(url)
        client.login(user, passwd)
        _romm_client = client
        logger.info("RomM login successful")
        return True

    async def search_roms(self, search_term: str, limit: int = 50):
        """Search for ROMs. Logs in automatically if needed.
        
        Returns a list of dicts with keys: id, name, platform_id, platform_name,
        platform_slug, file_name, file_size_bytes, url_cover.
        """
        global _romm_client
        if _romm_client is None or not _romm_client.is_authenticated:
            await self.romm_login()
        
        base_url = settings.getSetting("rommUrl", "").rstrip("/")
        results = _romm_client.search_roms(search_term, limit=limit)
        
        items = []
        for r in results:
            d = r.to_dict()
            # Build full cover URL from relative path if url_cover is relative
            if d.get("url_cover") and not d["url_cover"].startswith("http"):
                d["url_cover"] = base_url + "/" + d["url_cover"].lstrip("/")
            items.append(d)
        return items

    # A normal method. It can be called from the TypeScript side using @decky/api.
    async def add(self, left: int, right: int) -> int:
        return left + right

    async def long_running(self):
        await asyncio.sleep(15)
        # Passing through a bunch of random data, just as an example
        await decky.emit("timer_event", "Hello from the backend!", True, 2)

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        self.loop = asyncio.get_event_loop()
        decky.logger.info("Hello World!")

    # Function called first during the unload process, utilize this to handle your plugin being stopped, but not
    # completely removed
    async def _unload(self):
        decky.logger.info("Goodnight World!")
        pass

    # Function called after `_unload` during uninstall, utilize this to clean up processes and other remnants of your
    # plugin that may remain on the system
    async def _uninstall(self):
        decky.logger.info("Goodbye World!")
        pass

    async def start_timer(self):
        self.loop.create_task(self.long_running())

    # Migrations that should be performed before entering `_main()`.
    async def _migration(self):
        decky.logger.info("Migrating")
        # Here's a migration example for logs:
        # - `~/.config/decky-template/template.log` will be migrated to `decky.decky_LOG_DIR/template.log`
        decky.migrate_logs(os.path.join(decky.DECKY_USER_HOME,
                                               ".config", "decky-template", "template.log"))
        # Here's a migration example for settings:
        # - `~/homebrew/settings/template.json` is migrated to `decky.decky_SETTINGS_DIR/template.json`
        # - `~/.config/decky-template/` all files and directories under this root are migrated to `decky.decky_SETTINGS_DIR/`
        decky.migrate_settings(
            os.path.join(decky.DECKY_HOME, "settings", "template.json"),
            os.path.join(decky.DECKY_USER_HOME, ".config", "decky-template"))
        # Here's a migration example for runtime data:
        # - `~/homebrew/template/` all files and directories under this root are migrated to `decky.decky_RUNTIME_DIR/`
        # - `~/.local/share/decky-template/` all files and directories under this root are migrated to `decky.decky_RUNTIME_DIR/`
        decky.migrate_runtime(
            os.path.join(decky.DECKY_HOME, "template"),
            os.path.join(decky.DECKY_USER_HOME, ".local", "share", "decky-template"))
