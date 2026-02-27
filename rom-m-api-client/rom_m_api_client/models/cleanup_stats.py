from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CleanupStats")


@_attrs_define
class CleanupStats:
    """
    Attributes:
        platforms_in_db (int):
        roms_in_db (int):
        platforms_in_fs (int):
        roms_in_fs (int):
        removed_fs_platforms (int):
        removed_fs_roms (int):
    """

    platforms_in_db: int
    roms_in_db: int
    platforms_in_fs: int
    roms_in_fs: int
    removed_fs_platforms: int
    removed_fs_roms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platforms_in_db = self.platforms_in_db

        roms_in_db = self.roms_in_db

        platforms_in_fs = self.platforms_in_fs

        roms_in_fs = self.roms_in_fs

        removed_fs_platforms = self.removed_fs_platforms

        removed_fs_roms = self.removed_fs_roms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platforms_in_db": platforms_in_db,
                "roms_in_db": roms_in_db,
                "platforms_in_fs": platforms_in_fs,
                "roms_in_fs": roms_in_fs,
                "removed_fs_platforms": removed_fs_platforms,
                "removed_fs_roms": removed_fs_roms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platforms_in_db = d.pop("platforms_in_db")

        roms_in_db = d.pop("roms_in_db")

        platforms_in_fs = d.pop("platforms_in_fs")

        roms_in_fs = d.pop("roms_in_fs")

        removed_fs_platforms = d.pop("removed_fs_platforms")

        removed_fs_roms = d.pop("removed_fs_roms")

        cleanup_stats = cls(
            platforms_in_db=platforms_in_db,
            roms_in_db=roms_in_db,
            platforms_in_fs=platforms_in_fs,
            roms_in_fs=roms_in_fs,
            removed_fs_platforms=removed_fs_platforms,
            removed_fs_roms=removed_fs_roms,
        )

        cleanup_stats.additional_properties = d
        return cleanup_stats

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
