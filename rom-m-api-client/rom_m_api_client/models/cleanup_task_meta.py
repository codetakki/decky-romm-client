from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cleanup_stats import CleanupStats


T = TypeVar("T", bound="CleanupTaskMeta")


@_attrs_define
class CleanupTaskMeta:
    """
    Attributes:
        cleanup_stats (CleanupStats | None):
    """

    cleanup_stats: CleanupStats | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cleanup_stats import CleanupStats

        cleanup_stats: dict[str, Any] | None
        if isinstance(self.cleanup_stats, CleanupStats):
            cleanup_stats = self.cleanup_stats.to_dict()
        else:
            cleanup_stats = self.cleanup_stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cleanup_stats": cleanup_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cleanup_stats import CleanupStats

        d = dict(src_dict)

        def _parse_cleanup_stats(data: object) -> CleanupStats | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cleanup_stats_type_0 = CleanupStats.from_dict(data)

                return cleanup_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CleanupStats | None, data)

        cleanup_stats = _parse_cleanup_stats(d.pop("cleanup_stats"))

        cleanup_task_meta = cls(
            cleanup_stats=cleanup_stats,
        )

        cleanup_task_meta.additional_properties = d
        return cleanup_task_meta

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
