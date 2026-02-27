from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="FirmwareSchema")


@_attrs_define
class FirmwareSchema:
    """
    Attributes:
        id (int):
        file_name (str):
        file_name_no_tags (str):
        file_name_no_ext (str):
        file_extension (str):
        file_path (str):
        file_size_bytes (int):
        full_path (str):
        is_verified (bool):
        crc_hash (str):
        md5_hash (str):
        sha1_hash (str):
        missing_from_fs (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    file_name: str
    file_name_no_tags: str
    file_name_no_ext: str
    file_extension: str
    file_path: str
    file_size_bytes: int
    full_path: str
    is_verified: bool
    crc_hash: str
    md5_hash: str
    sha1_hash: str
    missing_from_fs: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file_name = self.file_name

        file_name_no_tags = self.file_name_no_tags

        file_name_no_ext = self.file_name_no_ext

        file_extension = self.file_extension

        file_path = self.file_path

        file_size_bytes = self.file_size_bytes

        full_path = self.full_path

        is_verified = self.is_verified

        crc_hash = self.crc_hash

        md5_hash = self.md5_hash

        sha1_hash = self.sha1_hash

        missing_from_fs = self.missing_from_fs

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "file_name": file_name,
                "file_name_no_tags": file_name_no_tags,
                "file_name_no_ext": file_name_no_ext,
                "file_extension": file_extension,
                "file_path": file_path,
                "file_size_bytes": file_size_bytes,
                "full_path": full_path,
                "is_verified": is_verified,
                "crc_hash": crc_hash,
                "md5_hash": md5_hash,
                "sha1_hash": sha1_hash,
                "missing_from_fs": missing_from_fs,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        file_name = d.pop("file_name")

        file_name_no_tags = d.pop("file_name_no_tags")

        file_name_no_ext = d.pop("file_name_no_ext")

        file_extension = d.pop("file_extension")

        file_path = d.pop("file_path")

        file_size_bytes = d.pop("file_size_bytes")

        full_path = d.pop("full_path")

        is_verified = d.pop("is_verified")

        crc_hash = d.pop("crc_hash")

        md5_hash = d.pop("md5_hash")

        sha1_hash = d.pop("sha1_hash")

        missing_from_fs = d.pop("missing_from_fs")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        firmware_schema = cls(
            id=id,
            file_name=file_name,
            file_name_no_tags=file_name_no_tags,
            file_name_no_ext=file_name_no_ext,
            file_extension=file_extension,
            file_path=file_path,
            file_size_bytes=file_size_bytes,
            full_path=full_path,
            is_verified=is_verified,
            crc_hash=crc_hash,
            md5_hash=md5_hash,
            sha1_hash=sha1_hash,
            missing_from_fs=missing_from_fs,
            created_at=created_at,
            updated_at=updated_at,
        )

        firmware_schema.additional_properties = d
        return firmware_schema

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
