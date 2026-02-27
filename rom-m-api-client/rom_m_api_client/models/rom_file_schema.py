from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rom_file_category import RomFileCategory

T = TypeVar("T", bound="RomFileSchema")


@_attrs_define
class RomFileSchema:
    """
    Attributes:
        id (int):
        rom_id (int):
        file_name (str):
        file_path (str):
        file_size_bytes (int):
        full_path (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_modified (datetime.datetime):
        crc_hash (None | str):
        md5_hash (None | str):
        sha1_hash (None | str):
        category (None | RomFileCategory):
    """

    id: int
    rom_id: int
    file_name: str
    file_path: str
    file_size_bytes: int
    full_path: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_modified: datetime.datetime
    crc_hash: None | str
    md5_hash: None | str
    sha1_hash: None | str
    category: None | RomFileCategory
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rom_id = self.rom_id

        file_name = self.file_name

        file_path = self.file_path

        file_size_bytes = self.file_size_bytes

        full_path = self.full_path

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_modified = self.last_modified.isoformat()

        crc_hash: None | str
        crc_hash = self.crc_hash

        md5_hash: None | str
        md5_hash = self.md5_hash

        sha1_hash: None | str
        sha1_hash = self.sha1_hash

        category: None | str
        if isinstance(self.category, RomFileCategory):
            category = self.category.value
        else:
            category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rom_id": rom_id,
                "file_name": file_name,
                "file_path": file_path,
                "file_size_bytes": file_size_bytes,
                "full_path": full_path,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_modified": last_modified,
                "crc_hash": crc_hash,
                "md5_hash": md5_hash,
                "sha1_hash": sha1_hash,
                "category": category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        rom_id = d.pop("rom_id")

        file_name = d.pop("file_name")

        file_path = d.pop("file_path")

        file_size_bytes = d.pop("file_size_bytes")

        full_path = d.pop("full_path")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        last_modified = isoparse(d.pop("last_modified"))

        def _parse_crc_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        crc_hash = _parse_crc_hash(d.pop("crc_hash"))

        def _parse_md5_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        md5_hash = _parse_md5_hash(d.pop("md5_hash"))

        def _parse_sha1_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sha1_hash = _parse_sha1_hash(d.pop("sha1_hash"))

        def _parse_category(data: object) -> None | RomFileCategory:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_0 = RomFileCategory(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomFileCategory, data)

        category = _parse_category(d.pop("category"))

        rom_file_schema = cls(
            id=id,
            rom_id=rom_id,
            file_name=file_name,
            file_path=file_path,
            file_size_bytes=file_size_bytes,
            full_path=full_path,
            created_at=created_at,
            updated_at=updated_at,
            last_modified=last_modified,
            crc_hash=crc_hash,
            md5_hash=md5_hash,
            sha1_hash=sha1_hash,
            category=category,
        )

        rom_file_schema.additional_properties = d
        return rom_file_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
