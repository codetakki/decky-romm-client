from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScanStats")


@_attrs_define
class ScanStats:
    """
    Attributes:
        total_platforms (int):
        total_roms (int):
        scanned_platforms (int):
        new_platforms (int):
        identified_platforms (int):
        scanned_roms (int):
        new_roms (int):
        identified_roms (int):
        scanned_firmware (int):
        new_firmware (int):
    """

    total_platforms: int
    total_roms: int
    scanned_platforms: int
    new_platforms: int
    identified_platforms: int
    scanned_roms: int
    new_roms: int
    identified_roms: int
    scanned_firmware: int
    new_firmware: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_platforms = self.total_platforms

        total_roms = self.total_roms

        scanned_platforms = self.scanned_platforms

        new_platforms = self.new_platforms

        identified_platforms = self.identified_platforms

        scanned_roms = self.scanned_roms

        new_roms = self.new_roms

        identified_roms = self.identified_roms

        scanned_firmware = self.scanned_firmware

        new_firmware = self.new_firmware

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_platforms": total_platforms,
                "total_roms": total_roms,
                "scanned_platforms": scanned_platforms,
                "new_platforms": new_platforms,
                "identified_platforms": identified_platforms,
                "scanned_roms": scanned_roms,
                "new_roms": new_roms,
                "identified_roms": identified_roms,
                "scanned_firmware": scanned_firmware,
                "new_firmware": new_firmware,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_platforms = d.pop("total_platforms")

        total_roms = d.pop("total_roms")

        scanned_platforms = d.pop("scanned_platforms")

        new_platforms = d.pop("new_platforms")

        identified_platforms = d.pop("identified_platforms")

        scanned_roms = d.pop("scanned_roms")

        new_roms = d.pop("new_roms")

        identified_roms = d.pop("identified_roms")

        scanned_firmware = d.pop("scanned_firmware")

        new_firmware = d.pop("new_firmware")

        scan_stats = cls(
            total_platforms=total_platforms,
            total_roms=total_roms,
            scanned_platforms=scanned_platforms,
            new_platforms=new_platforms,
            identified_platforms=identified_platforms,
            scanned_roms=scanned_roms,
            new_roms=new_roms,
            identified_roms=identified_roms,
            scanned_firmware=scanned_firmware,
            new_firmware=new_firmware,
        )

        scan_stats.additional_properties = d
        return scan_stats

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
