import os
import zipfile
import decky
from settings import SettingsManager
from decky import logger

# py_modules/ is automatically on sys.path when loaded by Decky Loader
from romm_client import RommClient

settings = SettingsManager(name="settings-romm-client")
settings.read()

# Shared RomM client instance (created on login, reused across calls)
_romm_client = None

# Track active / completed downloads  {rom_id: {status, progress, message, path}}
_downloads: dict[int, dict] = {}


def _extract_zip(zip_path: str, dest_dir: str, remove_zip: bool = True) -> list[str]:
    """Extract a zip archive into *dest_dir* and return the list of extracted file names.

    Args:
        zip_path: Full path to the .zip file.
        dest_dir: Directory to extract into (created if missing).
        remove_zip: Whether to delete the zip after extraction.

    Returns:
        List of extracted file paths (relative to *dest_dir*).
    """
    extracted: list[str] = []
    with zipfile.ZipFile(zip_path, "r") as zf:
        # Security: skip entries with absolute paths or '..' components
        for member in zf.namelist():
            if member.startswith("/") or ".." in member:
                logger.warning("Skipping suspicious zip entry: %s", member)
                continue
            zf.extract(member, dest_dir)
            extracted.append(member)
    if remove_zip:
        os.remove(zip_path)
        logger.info("Removed zip archive: %s", zip_path)
    return extracted


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

    async def get_platforms(self):
        """Fetch all platforms from RomM. Logs in automatically if needed.
        
        Returns a list of dicts with keys: id, name, slug, fs_slug,
        display_name, rom_count, url_logo.
        """
        global _romm_client
        if _romm_client is None or not _romm_client.is_authenticated:
            await self.romm_login()

        base_url = settings.getSetting("rommUrl", "").rstrip("/")
        platforms = _romm_client.get_platforms()

        items = []
        for p in platforms:
            d = p.to_dict()
            if d.get("url_logo") and not d["url_logo"].startswith("http"):
                d["url_logo"] = base_url + "/" + d["url_logo"].lstrip("/")
            items.append(d)
        return items

    # ------------------------------------------------------------------
    # ROM Downloads
    # ------------------------------------------------------------------

    async def download_rom(self, rom_id: int, platform_slug: str):
        """Download a ROM to the configured platform path.

        Looks up the download directory from the per-platform path settings,
        downloads the file via the RomM API, and automatically extracts it
        if the downloaded file is a zip archive.

        Args:
            rom_id: The internal RomM ID of the ROM.
            platform_slug: Platform slug used to resolve the local save path.

        Returns:
            A dict with keys:
                status   – "done"
                path     – final file/directory path on disk
                extracted – list of extracted entries if the ROM was a zip,
                            otherwise None
        """
        global _romm_client, _downloads

        if _romm_client is None or not _romm_client.is_authenticated:
            await self.romm_login()

        # Resolve destination directory from settings
        path_map = settings.getSetting("platformPaths", {})
        dest_dir = path_map.get(platform_slug)
        if not dest_dir:
            raise ValueError(
                f"No download path configured for platform '{platform_slug}'. "
                "Set it in Platform Paths first."
            )

        # Mark download as in-progress
        _downloads[rom_id] = {"status": "downloading", "progress": 0, "message": "Starting download…", "path": None}

        try:
            logger.info("Downloading ROM %d to %s", rom_id, dest_dir)
            _downloads[rom_id]["message"] = "Downloading…"

            downloaded_path = _romm_client.download_rom(rom_id, dest_dir)

            logger.info("Downloaded ROM to %s", downloaded_path)

            # If the file is a zip, extract it
            extracted = None
            final_path = str(downloaded_path)

            if str(downloaded_path).lower().endswith(".zip"):
                logger.info("ROM is a zip archive – extracting to %s", dest_dir)
                _downloads[rom_id]["message"] = "Extracting zip…"
                extracted = _extract_zip(str(downloaded_path), dest_dir, remove_zip=True)
                logger.info("Extracted %d entries from zip", len(extracted))
                # Point final_path at the extraction directory
                final_path = dest_dir

            _downloads[rom_id] = {
                "status": "done",
                "progress": 100,
                "message": "Download complete",
                "path": final_path,
            }

            return {
                "status": "done",
                "path": final_path,
                "extracted": extracted,
            }

        except Exception as exc:
            logger.error("ROM download failed: %s", exc)
            _downloads[rom_id] = {
                "status": "error",
                "progress": 0,
                "message": str(exc),
                "path": None,
            }
            raise

    async def get_download_status(self, rom_id: int):
        """Return the current download status for *rom_id* (or None if no download is tracked)."""
        return _downloads.get(rom_id)

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
