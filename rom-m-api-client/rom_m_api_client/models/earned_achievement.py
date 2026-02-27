from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EarnedAchievement")


@_attrs_define
class EarnedAchievement:
    """
    Attributes:
        id (str):
        date (str):
        date_hardcore (str | Unset):
    """

    id: str
    date: str
    date_hardcore: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date

        date_hardcore = self.date_hardcore

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
            }
        )
        if date_hardcore is not UNSET:
            field_dict["date_hardcore"] = date_hardcore

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        date = d.pop("date")

        date_hardcore = d.pop("date_hardcore", UNSET)

        earned_achievement = cls(
            id=id,
            date=date,
            date_hardcore=date_hardcore,
        )

        earned_achievement.additional_properties = d
        return earned_achievement

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
