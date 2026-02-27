"""High-level RomM client wrapper providing simple methods for login, search, and download."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import base64

import httpx

from rom_m_api_client import AuthenticatedClient, Client
from rom_m_api_client.api.auth import token_api_token_post
from rom_m_api_client.api.platforms import get_platforms_api_platforms_get
from rom_m_api_client.api.roms import (
    download_roms_api_roms_download_get,
    get_rom_api_roms_id_get,
    get_rom_content_api_roms_id_content_file_name_get,
    get_roms_api_roms_get,
)
from rom_m_api_client.errors import UnexpectedStatus
from rom_m_api_client.models.body_token_api_token_post import BodyTokenApiTokenPost
from rom_m_api_client.models.custom_limit_offset_page_simple_rom_schema import (
    CustomLimitOffsetPageSimpleRomSchema,
)
from rom_m_api_client.models.detailed_rom_schema import DetailedRomSchema
from rom_m_api_client.models.simple_rom_schema import SimpleRomSchema
from rom_m_api_client.models.token_response import TokenResponse


class RommClientError(Exception):
    """Base exception for RomM client errors."""


class LoginError(RommClientError):
    """Raised when login / token acquisition fails."""


class SearchError(RommClientError):
    """Raised when a ROM search fails."""


class DownloadError(RommClientError):
    """Raised when a ROM download fails."""


class PlatformError(RommClientError):
    """Raised when a platform request fails."""


@dataclass
class PlatformResult:
    """Lightweight representation of a platform from RomM."""

    id: int
    name: str
    slug: str
    fs_slug: str
    display_name: str
    rom_count: int
    url_logo: str | None

    @classmethod
    def from_schema(cls, p) -> PlatformResult:
        return cls(
            id=p.id,
            name=p.name,
            slug=p.slug,
            fs_slug=p.fs_slug,
            display_name=p.display_name,
            rom_count=p.rom_count,
            url_logo=getattr(p, 'url_logo', None),
        )

    def to_dict(self) -> dict:
        """Return a plain dict suitable for JSON serialisation to the frontend."""
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "fs_slug": self.fs_slug,
            "display_name": self.display_name,
            "rom_count": self.rom_count,
            "url_logo": self.url_logo,
        }


@dataclass
class SearchResult:
    """Lightweight representation of a ROM returned from a search / listing."""

    id: int
    name: str | None
    platform_id: int
    platform_name: str
    platform_slug: str
    file_name: str
    file_size_bytes: int
    url_cover: str | None

    @classmethod
    def from_simple_schema(cls, rom: SimpleRomSchema) -> SearchResult:
        return cls(
            id=rom.id,
            name=rom.name,
            platform_id=rom.platform_id,
            platform_name=rom.platform_display_name,
            platform_slug=rom.platform_slug,
            file_name=rom.fs_name,
            file_size_bytes=rom.fs_size_bytes,
            url_cover=rom.url_cover,
        )

    def to_dict(self) -> dict:
        """Return a plain dict suitable for JSON serialisation to the frontend."""
        return {
            "id": self.id,
            "name": self.name,
            "platform_id": self.platform_id,
            "platform_name": self.platform_name,
            "platform_slug": self.platform_slug,
            "file_name": self.file_name,
            "file_size_bytes": self.file_size_bytes,
            "url_cover": self.url_cover,
        }


class RommClient:
    """High-level wrapper around the generated RomM SDK.

    Usage::

        client = RommClient("https://your-romm-instance.example.com")
        client.login("user", "password")
        results = client.search_roms("Mario Kart")
        client.download_rom(results[0].id, Path("./downloads"))
    """

    def __init__(self, base_url: str, *, verify_ssl: bool = True) -> None:
        self._base_url = base_url.rstrip("/")
        self._verify_ssl = verify_ssl
        self._client: AuthenticatedClient | None = None

    # ------------------------------------------------------------------
    # Authentication
    # ------------------------------------------------------------------

    def login(self, username: str, password: str) -> None:
        """Authenticate with the RomM server using session-based auth.

        Calls ``POST /api/login`` with HTTP Basic credentials. The server
        responds with a ``romm_session`` cookie which is stored and sent
        with every subsequent request.

        Args:
            username: RomM account username.
            password: RomM account password.

        Raises:
            LoginError: If the server rejects the credentials or returns an error.
        """
        try:
            creds = base64.b64encode(f"{username}:{password}".encode()).decode()
            transport_client = httpx.Client(
                base_url=self._base_url,
                verify=self._verify_ssl,
            )
            response = transport_client.post(
                "/api/login",
                headers={"Authorization": f"Basic {creds}"},
            )
        except Exception as exc:
            raise LoginError(f"Login request failed: {exc}") from exc

        if response.status_code != 200:
            raise LoginError(
                f"Login failed (HTTP {response.status_code}): "
                f"{response.content.decode(errors='ignore')}"
            )

        # Extract session cookies set by the server
        cookies = dict(transport_client.cookies)
        if not cookies:
            raise LoginError("Login succeeded but no session cookies were returned.")

        # Build a Client that carries the session cookies for all future calls.
        # We use a dummy token with AuthenticatedClient; the real auth is the
        # session cookie, but AuthenticatedClient requires a token value.
        self._client = AuthenticatedClient(
            base_url=self._base_url,
            token="session",
            prefix="",
            verify_ssl=self._verify_ssl,
            cookies=cookies,
        )

    def login_with_token(self, username: str, password: str) -> TokenResponse:
        """Authenticate via the OAuth2 token endpoint (``POST /api/token``).

        .. note::

            Most RomM deployments use session-based auth. Prefer :meth:`login`
            unless you specifically need a Bearer token.

        Args:
            username: RomM account username.
            password: RomM account password.

        Returns:
            The ``TokenResponse`` containing the access token, token type and expiry.

        Raises:
            LoginError: If the server rejects the credentials or returns an error.
        """
        unauthenticated = Client(
            base_url=self._base_url,
            verify_ssl=self._verify_ssl,
        )

        body = BodyTokenApiTokenPost(
            username=username,
            password=password,
            grant_type="password",
        )

        try:
            response = token_api_token_post.sync_detailed(client=unauthenticated, body=body)
        except Exception as exc:
            raise LoginError(f"Login request failed: {exc}") from exc

        if response.status_code.value != 200 or not isinstance(response.parsed, TokenResponse):
            raise LoginError(
                f"Login failed (HTTP {response.status_code.value}): "
                f"{response.content.decode(errors='ignore')}"
            )

        token_data: TokenResponse = response.parsed

        # Build an authenticated client for all future calls
        self._client = AuthenticatedClient(
            base_url=self._base_url,
            token=token_data.access_token,
            verify_ssl=self._verify_ssl,
        )

        return token_data

    def set_token(self, token: str) -> None:
        """Manually set a pre-existing access token (skips the login flow).

        Args:
            token: A valid RomM access token.
        """
        self._client = AuthenticatedClient(
            base_url=self._base_url,
            token=token,
            verify_ssl=self._verify_ssl,
        )

    def set_session_cookies(self, cookies: dict[str, str]) -> None:
        """Manually set session cookies (e.g. a previously saved ``romm_session``).

        Args:
            cookies: Dictionary of cookie name/value pairs.
        """
        self._client = AuthenticatedClient(
            base_url=self._base_url,
            token="session",
            prefix="",
            verify_ssl=self._verify_ssl,
            cookies=cookies,
        )

    @property
    def is_authenticated(self) -> bool:
        """Return ``True`` if the client has been authenticated."""
        return self._client is not None

    def _require_auth(self) -> AuthenticatedClient:
        if self._client is None:
            raise RommClientError("Not authenticated – call login() or set_token() first.")
        return self._client

    # ------------------------------------------------------------------
    # Platforms
    # ------------------------------------------------------------------

    def get_platforms(self) -> list[PlatformResult]:
        """Fetch all platforms registered on the RomM server.

        Returns:
            A list of :class:`PlatformResult` objects.

        Raises:
            PlatformError: If the request fails or returns an unexpected response.
        """
        client = self._require_auth()

        try:
            response = get_platforms_api_platforms_get.sync_detailed(client=client)
        except Exception as exc:
            raise PlatformError(f"Get platforms request failed: {exc}") from exc

        if response.status_code.value != 200 or not isinstance(response.parsed, list):
            raise PlatformError(
                f"Get platforms failed (HTTP {response.status_code.value}): "
                f"{response.content.decode(errors='ignore')}"
            )

        return [PlatformResult.from_schema(p) for p in response.parsed]

    # ------------------------------------------------------------------
    # Searching / listing ROMs
    # ------------------------------------------------------------------

    def search_roms(
        self,
        search_term: str,
        *,
        platform_ids: list[int] | None = None,
        limit: int = 50,
        offset: int = 0,
        order_by: str = "name",
        order_dir: str = "asc",
    ) -> list[SearchResult]:
        """Search for ROMs on the RomM server by name.

        Args:
            search_term: Free-text search string (matched against ROM names).
            platform_ids: Optional list of platform IDs to restrict the search.
            limit: Maximum number of results to return (default 50).
            offset: Pagination offset.
            order_by: Field to sort by (default ``"name"``).
            order_dir: Sort direction – ``"asc"`` or ``"desc"``.

        Returns:
            A list of :class:`SearchResult` objects.

        Raises:
            SearchError: If the request fails or returns an unexpected response.
        """
        client = self._require_auth()

        try:
            response = get_roms_api_roms_get.sync_detailed(
                client=client,
                search_term=search_term,
                platform_ids=platform_ids,
                limit=limit,
                offset=offset,
                order_by=order_by,
                order_dir=order_dir,
            )
        except Exception as exc:
            raise SearchError(f"ROM search request failed: {exc}") from exc

        if response.status_code.value != 200 or not isinstance(
            response.parsed, CustomLimitOffsetPageSimpleRomSchema
        ):
            raise SearchError(
                f"ROM search failed (HTTP {response.status_code.value}): "
                f"{response.content.decode(errors='ignore')}"
            )

        page: CustomLimitOffsetPageSimpleRomSchema = response.parsed
        return [SearchResult.from_simple_schema(rom) for rom in page.items]

    def get_rom(self, rom_id: int) -> DetailedRomSchema:
        """Fetch detailed information for a specific ROM.

        Args:
            rom_id: The internal RomM ID of the ROM.

        Returns:
            A ``DetailedRomSchema`` object with full ROM metadata.

        Raises:
            SearchError: If the ROM is not found or the request fails.
        """
        client = self._require_auth()

        try:
            response = get_rom_api_roms_id_get.sync_detailed(rom_id, client=client)
        except Exception as exc:
            raise SearchError(f"Get ROM request failed: {exc}") from exc

        if response.status_code.value == 404:
            raise SearchError(f"ROM with ID {rom_id} not found.")

        if response.status_code.value != 200 or not isinstance(response.parsed, DetailedRomSchema):
            raise SearchError(
                f"Get ROM failed (HTTP {response.status_code.value}): "
                f"{response.content.decode(errors='ignore')}"
            )

        return response.parsed

    # ------------------------------------------------------------------
    # Downloading ROMs
    # ------------------------------------------------------------------

    def download_rom(
        self,
        rom_id: int,
        output_dir: str | Path,
        *,
        file_name: str | None = None,
    ) -> Path:
        """Download a single ROM file to disk.

        This uses the ``/api/roms/{id}/content/{file_name}`` endpoint which
        streams the actual ROM file content (single-file ROMs) or a zip
        (multi-part ROMs).

        Args:
            rom_id: The internal RomM ID of the ROM to download.
            output_dir: Directory where the file will be saved.
            file_name: Optional override for the output file name. If not
                provided the ROM's ``fs_name`` from the server is used.

        Returns:
            The ``Path`` to the downloaded file.

        Raises:
            DownloadError: If the download fails for any reason.
        """
        client = self._require_auth()

        # First, get ROM details so we know the actual file name
        rom = self.get_rom(rom_id)
        out_name = file_name or rom.fs_name
        if not out_name:
            out_name = f"rom_{rom_id}"

        try:
            # Make the request directly via httpx to avoid the SDK's
            # _parse_response which tries response.json() on binary content.
            from urllib.parse import quote
            url = f"/api/roms/{quote(str(rom_id), safe='')}/content/{quote(out_name, safe='')}"
            httpx_client = client.get_httpx_client()
            raw_response = httpx_client.request("GET", url)
        except Exception as exc:
            raise DownloadError(f"Download request failed: {exc}") from exc

        if raw_response.status_code != 200:
            raise DownloadError(
                f"Download failed (HTTP {raw_response.status_code}): "
                f"{raw_response.content.decode(errors='ignore')}"
            )

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        dest = output_path / out_name

        dest.write_bytes(raw_response.content)
        return dest

    def download_roms_zip(
        self,
        rom_ids: list[int],
        output_dir: str | Path,
        *,
        zip_name: str | None = None,
    ) -> Path:
        """Download multiple ROMs as a single zip archive.

        Args:
            rom_ids: List of ROM IDs to bundle.
            output_dir: Directory where the zip will be saved.
            zip_name: Optional name for the zip file (without extension).

        Returns:
            The ``Path`` to the downloaded zip file.

        Raises:
            DownloadError: If the download fails for any reason.
        """
        client = self._require_auth()

        ids_str = ",".join(str(rid) for rid in rom_ids)
        out_name = zip_name or f"romm_download_{ids_str}"
        if not out_name.endswith(".zip"):
            out_name += ".zip"

        try:
            response = download_roms_api_roms_download_get.sync_detailed(
                client=client,
                rom_ids=ids_str,
                filename=out_name,
            )
        except Exception as exc:
            raise DownloadError(f"Batch download request failed: {exc}") from exc

        if response.status_code.value != 200:
            raise DownloadError(
                f"Batch download failed (HTTP {response.status_code.value}): "
                f"{response.content.decode(errors='ignore')}"
            )

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        dest = output_path / out_name

        dest.write_bytes(response.content)
        return dest
