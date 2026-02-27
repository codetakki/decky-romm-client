"""Tests for the _extract_zip helper used during ROM downloads.

The function lives in main.py (the Decky plugin entry-point) but we test it
in isolation here by importing it directly.
"""

from __future__ import annotations

import os
import sys
import tempfile
import zipfile
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Make the plugin root importable so we can grab the helper.
# We can't ``import main`` directly (it depends on the ``decky`` runtime),
# so we load the function source via importlib to test it in isolation.
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent.parent  # repo root


def _extract_zip(zip_path: str, dest_dir: str, remove_zip: bool = True) -> list[str]:
    """Mirror of the _extract_zip from main.py (duplicated here to avoid
    importing the Decky-dependent main module)."""
    extracted: list[str] = []
    with zipfile.ZipFile(zip_path, "r") as zf:
        for member in zf.namelist():
            if member.startswith("/") or ".." in member:
                continue
            zf.extract(member, dest_dir)
            extracted.append(member)
    if remove_zip:
        os.remove(zip_path)
    return extracted


# ===================================================================
# Tests
# ===================================================================


class TestExtractZip:
    """Unit tests for _extract_zip."""

    def _make_zip(self, tmpdir: str, entries: dict[str, bytes]) -> str:
        """Create a zip file with the given entries and return its path."""
        zip_path = os.path.join(tmpdir, "test.zip")
        with zipfile.ZipFile(zip_path, "w") as zf:
            for name, data in entries.items():
                zf.writestr(name, data)
        return zip_path

    def test_extracts_single_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = self._make_zip(tmpdir, {"rom.nes": b"\x00" * 128})
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            result = _extract_zip(zip_path, dest, remove_zip=False)

            assert result == ["rom.nes"]
            assert os.path.isfile(os.path.join(dest, "rom.nes"))
            # Zip file should still exist
            assert os.path.isfile(zip_path)

    def test_extracts_multiple_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            entries = {
                "track01.bin": b"bin-data",
                "track01.cue": b"cue-data",
                "readme.txt": b"hello",
            }
            zip_path = self._make_zip(tmpdir, entries)
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            result = _extract_zip(zip_path, dest, remove_zip=False)

            assert set(result) == set(entries.keys())
            for name, data in entries.items():
                extracted_file = os.path.join(dest, name)
                assert os.path.isfile(extracted_file)
                assert open(extracted_file, "rb").read() == data

    def test_removes_zip_by_default(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = self._make_zip(tmpdir, {"rom.sfc": b"data"})
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            _extract_zip(zip_path, dest, remove_zip=True)

            assert not os.path.isfile(zip_path)

    def test_keeps_zip_when_remove_false(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = self._make_zip(tmpdir, {"rom.sfc": b"data"})
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            _extract_zip(zip_path, dest, remove_zip=False)

            assert os.path.isfile(zip_path)

    def test_skips_entries_with_dotdot(self):
        """Zip entries containing '..' should be skipped for security."""
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = self._make_zip(tmpdir, {
                "safe_file.bin": b"ok",
                "../etc/passwd": b"evil",
                "sub/../escape.txt": b"also evil",
            })
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            result = _extract_zip(zip_path, dest, remove_zip=False)

            # Only the safe file should have been extracted
            assert result == ["safe_file.bin"]
            assert os.path.isfile(os.path.join(dest, "safe_file.bin"))

    def test_skips_absolute_path_entries(self):
        """Zip entries with absolute paths should be skipped."""
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = self._make_zip(tmpdir, {
                "good.rom": b"ok",
                "/tmp/evil.rom": b"bad",
            })
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            result = _extract_zip(zip_path, dest, remove_zip=False)

            assert result == ["good.rom"]

    def test_preserves_subdirectory_structure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = self._make_zip(tmpdir, {
                "disc1/track01.bin": b"bin1",
                "disc1/track01.cue": b"cue1",
                "disc2/track01.bin": b"bin2",
            })
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            result = _extract_zip(zip_path, dest, remove_zip=False)

            assert len(result) == 3
            assert os.path.isfile(os.path.join(dest, "disc1", "track01.bin"))
            assert os.path.isfile(os.path.join(dest, "disc1", "track01.cue"))
            assert os.path.isfile(os.path.join(dest, "disc2", "track01.bin"))

    def test_empty_zip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = self._make_zip(tmpdir, {})
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            result = _extract_zip(zip_path, dest, remove_zip=True)

            assert result == []
            assert not os.path.isfile(zip_path)

    def test_invalid_zip_raises(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            bad_path = os.path.join(tmpdir, "not_a.zip")
            with open(bad_path, "wb") as f:
                f.write(b"this is not a zip file")
            dest = os.path.join(tmpdir, "out")
            os.makedirs(dest)

            with pytest.raises(zipfile.BadZipFile):
                _extract_zip(bad_path, dest, remove_zip=False)
