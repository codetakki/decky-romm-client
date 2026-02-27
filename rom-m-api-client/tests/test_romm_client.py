"""Tests for the high-level RomM client wrapper.

Run unit tests (no server needed):
    cd rom-m-api-client && python -m pytest tests/ -v

Run integration tests against a real server:
    ROMM_TEST_URL=https://demo.romm.app \
    ROMM_TEST_USER=admin \
    ROMM_TEST_PASS=admin \
    python -m pytest tests/ -v -m integration
"""

from __future__ import annotations

import importlib
import os
import sys
import tempfile
from http import HTTPStatus
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

# ---------------------------------------------------------------------------
# Ensure the package & wrapper are importable from the repo root
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# The wrapper lives at romm-client.py (hyphen in name), so import it by path.
# We register the module in sys.modules *before* exec_module so that
# @dataclass + `from __future__ import annotations` can resolve the module.
import importlib.util

_spec = importlib.util.spec_from_file_location("romm_client", ROOT / "romm-client.py")
romm_client = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
sys.modules["romm_client"] = romm_client
_spec.loader.exec_module(romm_client)  # type: ignore[union-attr]

RommClient = romm_client.RommClient
RommClientError = romm_client.RommClientError
LoginError = romm_client.LoginError
SearchError = romm_client.SearchError
DownloadError = romm_client.DownloadError
SearchResult = romm_client.SearchResult

from rom_m_api_client.types import Response


# ===================================================================
# Helpers to build fake SDK responses
# ===================================================================

def _ok_response(parsed, content: bytes = b"ok") -> Response:
    """Return a minimal Response with HTTP 200."""
    return Response(
        status_code=HTTPStatus.OK,
        content=content,
        headers={},
        parsed=parsed,
    )


def _error_response(status: int, body: bytes = b"error") -> Response:
    return Response(
        status_code=HTTPStatus(status),
        content=body,
        headers={},
        parsed=None,
    )


def _fake_token_response():
    """Build a TokenResponse-like object."""
    from rom_m_api_client.models.token_response import TokenResponse
    return TokenResponse(
        access_token="test-access-token",
        token_type="bearer",
        expires=3600,
    )


def _fake_simple_rom(rom_id: int = 1, name: str = "Super Mario World"):
    """Build a minimal SimpleRomSchema-like mock."""
    mock = MagicMock()
    mock.id = rom_id
    mock.name = name
    mock.platform_id = 10
    mock.platform_display_name = "SNES"
    mock.fs_name = f"{name.replace(' ', '_')}.sfc"
    mock.fs_size_bytes = 1_048_576
    return mock


def _fake_page(items):
    """Build a CustomLimitOffsetPageSimpleRomSchema-like object."""
    from rom_m_api_client.models.custom_limit_offset_page_simple_rom_schema import (
        CustomLimitOffsetPageSimpleRomSchema,
    )
    mock = MagicMock(spec=CustomLimitOffsetPageSimpleRomSchema)
    mock.items = items
    return mock


def _fake_detailed_rom(rom_id: int = 1, name: str = "Super Mario World"):
    """Build a minimal DetailedRomSchema-like mock."""
    from rom_m_api_client.models.detailed_rom_schema import DetailedRomSchema
    mock = MagicMock(spec=DetailedRomSchema)
    mock.id = rom_id
    mock.name = name
    mock.fs_name = f"{name.replace(' ', '_')}.sfc"
    mock.fs_size_bytes = 1_048_576
    return mock


# ===================================================================
# Unit tests – all SDK calls are mocked
# ===================================================================

class TestAuthentication:
    """Tests for login / set_token / is_authenticated."""

    def test_not_authenticated_initially(self):
        client = RommClient("https://example.com")
        assert client.is_authenticated is False

    def test_require_auth_raises_before_login(self):
        client = RommClient("https://example.com")
        with pytest.raises(RommClientError, match="Not authenticated"):
            client._require_auth()

    @patch("rom_m_api_client.api.auth.token_api_token_post.sync_detailed")
    def test_login_success(self, mock_token):
        token_resp = _fake_token_response()
        mock_token.return_value = _ok_response(token_resp)

        client = RommClient("https://example.com")
        result = client.login("admin", "admin")

        assert result.access_token == "test-access-token"
        assert client.is_authenticated is True
        mock_token.assert_called_once()

    @patch("rom_m_api_client.api.auth.token_api_token_post.sync_detailed")
    def test_login_bad_credentials(self, mock_token):
        mock_token.return_value = _error_response(401, b"Invalid credentials")

        client = RommClient("https://example.com")
        with pytest.raises(LoginError, match="Login failed"):
            client.login("bad", "creds")

    @patch("rom_m_api_client.api.auth.token_api_token_post.sync_detailed")
    def test_login_network_error(self, mock_token):
        mock_token.side_effect = ConnectionError("refused")

        client = RommClient("https://example.com")
        with pytest.raises(LoginError, match="Login request failed"):
            client.login("admin", "admin")

    def test_set_token(self):
        client = RommClient("https://example.com")
        client.set_token("my-token")
        assert client.is_authenticated is True


class TestSearchRoms:
    """Tests for search_roms and get_rom."""

    def _authed_client(self) -> RommClient:
        c = RommClient("https://example.com")
        c.set_token("tok")
        return c

    @patch("rom_m_api_client.api.roms.get_roms_api_roms_get.sync_detailed")
    def test_search_roms_returns_results(self, mock_get_roms):
        roms = [_fake_simple_rom(1, "Mario Kart"), _fake_simple_rom(2, "Mario Party")]
        page = _fake_page(roms)
        mock_get_roms.return_value = _ok_response(page)

        client = self._authed_client()
        results = client.search_roms("Mario")

        assert len(results) == 2
        assert all(isinstance(r, SearchResult) for r in results)
        assert results[0].name == "Mario Kart"
        assert results[1].name == "Mario Party"

    @patch("rom_m_api_client.api.roms.get_roms_api_roms_get.sync_detailed")
    def test_search_roms_empty(self, mock_get_roms):
        page = _fake_page([])
        mock_get_roms.return_value = _ok_response(page)

        client = self._authed_client()
        results = client.search_roms("nonexistent")
        assert results == []

    @patch("rom_m_api_client.api.roms.get_roms_api_roms_get.sync_detailed")
    def test_search_roms_server_error(self, mock_get_roms):
        mock_get_roms.return_value = _error_response(500, b"Internal Server Error")

        client = self._authed_client()
        with pytest.raises(SearchError, match="ROM search failed"):
            client.search_roms("Mario")

    @patch("rom_m_api_client.api.roms.get_roms_api_roms_get.sync_detailed")
    def test_search_roms_passes_params(self, mock_get_roms):
        page = _fake_page([])
        mock_get_roms.return_value = _ok_response(page)

        client = self._authed_client()
        client.search_roms("Zelda", platform_ids=[1, 2], limit=10, offset=5, order_by="id", order_dir="desc")

        _, kwargs = mock_get_roms.call_args
        assert kwargs["search_term"] == "Zelda"
        assert kwargs["platform_ids"] == [1, 2]
        assert kwargs["limit"] == 10
        assert kwargs["offset"] == 5

    @patch("rom_m_api_client.api.roms.get_rom_api_roms_id_get.sync_detailed")
    def test_get_rom_success(self, mock_get_rom):
        rom = _fake_detailed_rom(42, "Sonic")
        mock_get_rom.return_value = _ok_response(rom)

        client = self._authed_client()
        result = client.get_rom(42)
        assert result.name == "Sonic"

    @patch("rom_m_api_client.api.roms.get_rom_api_roms_id_get.sync_detailed")
    def test_get_rom_not_found(self, mock_get_rom):
        mock_get_rom.return_value = _error_response(404, b"Not found")

        client = self._authed_client()
        with pytest.raises(SearchError, match="not found"):
            client.get_rom(9999)


class TestDownloadRom:
    """Tests for download_rom and download_roms_zip."""

    def _authed_client(self) -> RommClient:
        c = RommClient("https://example.com")
        c.set_token("tok")
        return c

    @patch("rom_m_api_client.api.roms.get_rom_content_api_roms_id_content_file_name_get.sync_detailed")
    @patch("rom_m_api_client.api.roms.get_rom_api_roms_id_get.sync_detailed")
    def test_download_rom_success(self, mock_get_rom, mock_content):
        rom = _fake_detailed_rom(1, "TestRom")
        mock_get_rom.return_value = _ok_response(rom)

        file_bytes = b"\x00" * 256
        mock_content.return_value = _ok_response(parsed=None, content=file_bytes)

        client = self._authed_client()

        with tempfile.TemporaryDirectory() as tmpdir:
            path = client.download_rom(1, tmpdir)
            assert path.exists()
            assert path.read_bytes() == file_bytes
            assert path.name == "TestRom.sfc"

    @patch("rom_m_api_client.api.roms.get_rom_content_api_roms_id_content_file_name_get.sync_detailed")
    @patch("rom_m_api_client.api.roms.get_rom_api_roms_id_get.sync_detailed")
    def test_download_rom_custom_filename(self, mock_get_rom, mock_content):
        rom = _fake_detailed_rom(1, "TestRom")
        mock_get_rom.return_value = _ok_response(rom)
        mock_content.return_value = _ok_response(parsed=None, content=b"data")

        client = self._authed_client()

        with tempfile.TemporaryDirectory() as tmpdir:
            path = client.download_rom(1, tmpdir, file_name="custom.bin")
            assert path.name == "custom.bin"

    @patch("rom_m_api_client.api.roms.get_rom_content_api_roms_id_content_file_name_get.sync_detailed")
    @patch("rom_m_api_client.api.roms.get_rom_api_roms_id_get.sync_detailed")
    def test_download_rom_server_error(self, mock_get_rom, mock_content):
        rom = _fake_detailed_rom(1, "TestRom")
        mock_get_rom.return_value = _ok_response(rom)
        mock_content.return_value = _error_response(500, b"fail")

        client = self._authed_client()
        with tempfile.TemporaryDirectory() as tmpdir:
            with pytest.raises(DownloadError, match="Download failed"):
                client.download_rom(1, tmpdir)

    @patch("rom_m_api_client.api.roms.download_roms_api_roms_download_get.sync_detailed")
    def test_download_roms_zip_success(self, mock_dl):
        zip_bytes = b"PK\x03\x04fake-zip"
        mock_dl.return_value = _ok_response(parsed=None, content=zip_bytes)

        client = self._authed_client()

        with tempfile.TemporaryDirectory() as tmpdir:
            path = client.download_roms_zip([1, 2, 3], tmpdir, zip_name="bundle")
            assert path.exists()
            assert path.name == "bundle.zip"
            assert path.read_bytes() == zip_bytes

    @patch("rom_m_api_client.api.roms.download_roms_api_roms_download_get.sync_detailed")
    def test_download_roms_zip_error(self, mock_dl):
        mock_dl.return_value = _error_response(403, b"forbidden")

        client = self._authed_client()
        with tempfile.TemporaryDirectory() as tmpdir:
            with pytest.raises(DownloadError, match="Batch download failed"):
                client.download_roms_zip([1], tmpdir)


class TestSearchResultDataclass:
    """Tests for the SearchResult dataclass / from_simple_schema factory."""

    def test_from_simple_schema(self):
        mock_rom = _fake_simple_rom(7, "Kirby")
        result = SearchResult.from_simple_schema(mock_rom)
        assert result.id == 7
        assert result.name == "Kirby"
        assert result.platform_name == "SNES"
        assert result.file_name == "Kirby.sfc"


# ===================================================================
# Integration tests – run against a live server
# ===================================================================

ROMM_TEST_URL = os.environ.get("ROMM_TEST_URL", "")
ROMM_TEST_USER = os.environ.get("ROMM_TEST_USER", "")
ROMM_TEST_PASS = os.environ.get("ROMM_TEST_PASS", "")

integration = pytest.mark.skipif(
    not ROMM_TEST_URL,
    reason="Set ROMM_TEST_URL, ROMM_TEST_USER, ROMM_TEST_PASS to run integration tests",
)


@pytest.mark.integration
class TestIntegration:
    """End-to-end tests against a real RomM instance.

    Activate by setting env vars:
        ROMM_TEST_URL  – e.g. https://demo.romm.app
        ROMM_TEST_USER – e.g. admin
        ROMM_TEST_PASS – e.g. admin
    """

    @integration
    def test_login(self):
        client = RommClient(ROMM_TEST_URL, verify_ssl=True)
        token = client.login(ROMM_TEST_USER, ROMM_TEST_PASS)
        assert token.access_token
        assert client.is_authenticated

    @integration
    def test_search_roms(self):
        client = RommClient(ROMM_TEST_URL, verify_ssl=True)
        client.login(ROMM_TEST_USER, ROMM_TEST_PASS)
        # A broad search that should return *something* on the demo server
        results = client.search_roms("", limit=5)
        assert isinstance(results, list)
        # Demo server may or may not have roms; just verify no crash
        for r in results:
            assert isinstance(r, SearchResult)
            print(f"  [{r.id}] {r.name} ({r.platform_name}) – {r.file_name}")

    @integration
    def test_get_rom(self):
        client = RommClient(ROMM_TEST_URL, verify_ssl=True)
        client.login(ROMM_TEST_USER, ROMM_TEST_PASS)
        results = client.search_roms("", limit=1)
        if not results:
            pytest.skip("No ROMs on server to test get_rom")
        rom = client.get_rom(results[0].id)
        assert rom.id == results[0].id
        print(f"  ROM detail: {rom.name}")

    @integration
    def test_download_rom(self):
        client = RommClient(ROMM_TEST_URL, verify_ssl=True)
        client.login(ROMM_TEST_USER, ROMM_TEST_PASS)
        results = client.search_roms("", limit=1)
        if not results:
            pytest.skip("No ROMs on server to test download")
        with tempfile.TemporaryDirectory() as tmpdir:
            path = client.download_rom(results[0].id, tmpdir)
            assert path.exists()
            assert path.stat().st_size > 0
            print(f"  Downloaded {path.name} ({path.stat().st_size} bytes)")
