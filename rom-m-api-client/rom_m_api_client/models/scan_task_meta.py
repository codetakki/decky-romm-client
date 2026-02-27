from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.scan_stats import ScanStats


T = TypeVar("T", bound="ScanTaskMeta")


@_attrs_define
class ScanTaskMeta:
    """
    Attributes:
        scan_stats (None | ScanStats):
    """

    scan_stats: None | ScanStats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.scan_stats import ScanStats

        scan_stats: dict[str, Any] | None
        if isinstance(self.scan_stats, ScanStats):
            scan_stats = self.scan_stats.to_dict()
        else:
            scan_stats = self.scan_stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scan_stats": scan_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scan_stats import ScanStats

        d = dict(src_dict)

        def _parse_scan_stats(data: object) -> None | ScanStats:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scan_stats_type_0 = ScanStats.from_dict(data)

                return scan_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScanStats, data)

        scan_stats = _parse_scan_stats(d.pop("scan_stats"))

        scan_task_meta = cls(
            scan_stats=scan_stats,
        )

        scan_task_meta.additional_properties = d
        return scan_task_meta

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
