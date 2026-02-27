from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.conversion_stats import ConversionStats


T = TypeVar("T", bound="ConversionTaskMeta")


@_attrs_define
class ConversionTaskMeta:
    """
    Attributes:
        conversion_stats (ConversionStats | None):
    """

    conversion_stats: ConversionStats | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.conversion_stats import ConversionStats

        conversion_stats: dict[str, Any] | None
        if isinstance(self.conversion_stats, ConversionStats):
            conversion_stats = self.conversion_stats.to_dict()
        else:
            conversion_stats = self.conversion_stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversion_stats": conversion_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_stats import ConversionStats

        d = dict(src_dict)

        def _parse_conversion_stats(data: object) -> ConversionStats | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conversion_stats_type_0 = ConversionStats.from_dict(data)

                return conversion_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConversionStats | None, data)

        conversion_stats = _parse_conversion_stats(d.pop("conversion_stats"))

        conversion_task_meta = cls(
            conversion_stats=conversion_stats,
        )

        conversion_task_meta.additional_properties = d
        return conversion_task_meta

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
