from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatsReturn")


@_attrs_define
class StatsReturn:
    """
    Attributes:
        platforms (int):
        roms (int):
        saves (int):
        states (int):
        screenshots (int):
        total_filesize_bytes (int):
    """

    platforms: int
    roms: int
    saves: int
    states: int
    screenshots: int
    total_filesize_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platforms = self.platforms

        roms = self.roms

        saves = self.saves

        states = self.states

        screenshots = self.screenshots

        total_filesize_bytes = self.total_filesize_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "PLATFORMS": platforms,
                "ROMS": roms,
                "SAVES": saves,
                "STATES": states,
                "SCREENSHOTS": screenshots,
                "TOTAL_FILESIZE_BYTES": total_filesize_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platforms = d.pop("PLATFORMS")

        roms = d.pop("ROMS")

        saves = d.pop("SAVES")

        states = d.pop("STATES")

        screenshots = d.pop("SCREENSHOTS")

        total_filesize_bytes = d.pop("TOTAL_FILESIZE_BYTES")

        stats_return = cls(
            platforms=platforms,
            roms=roms,
            saves=saves,
            states=states,
            screenshots=screenshots,
            total_filesize_bytes=total_filesize_bytes,
        )

        stats_return.additional_properties = d
        return stats_return

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
