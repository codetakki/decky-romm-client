from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_stats import UpdateStats


T = TypeVar("T", bound="UpdateTaskMeta")


@_attrs_define
class UpdateTaskMeta:
    """
    Attributes:
        update_stats (None | UpdateStats):
    """

    update_stats: None | UpdateStats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_stats import UpdateStats

        update_stats: dict[str, Any] | None
        if isinstance(self.update_stats, UpdateStats):
            update_stats = self.update_stats.to_dict()
        else:
            update_stats = self.update_stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "update_stats": update_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_stats import UpdateStats

        d = dict(src_dict)

        def _parse_update_stats(data: object) -> None | UpdateStats:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_stats_type_0 = UpdateStats.from_dict(data)

                return update_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UpdateStats, data)

        update_stats = _parse_update_stats(d.pop("update_stats"))

        update_task_meta = cls(
            update_stats=update_stats,
        )

        update_task_meta.additional_properties = d
        return update_task_meta

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
