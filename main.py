import os
import decky
from settings import SettingsManager
from decky import logger

# py_modules/ is automatically on sys.path when loaded by Decky Loader
from romm_client import RommClient

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

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        decky.logger.info("RomM Client plugin loaded")

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

    # Migrations that should be performed before entering `_main()`.
    async def _migration(self):
        # Migration example for logs:
        # decky.migrate_logs(os.path.join(decky.DECKY_USER_HOME,
        #     ".config", "romm-client", "romm-client.log"))
        # Migration example for settings:
        # decky.migrate_settings(
        #     os.path.join(decky.DECKY_HOME, "settings", "romm-client.json"),
        #     os.path.join(decky.DECKY_USER_HOME, ".config", "romm-client"))
        # Migration example for runtime data:
        # decky.migrate_runtime(
        #     os.path.join(decky.DECKY_HOME, "romm-client"),
        #     os.path.join(decky.DECKY_USER_HOME, ".local", "share", "romm-client"))
        pass
