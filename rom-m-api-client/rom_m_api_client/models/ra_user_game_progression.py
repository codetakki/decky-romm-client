from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.earned_achievement import EarnedAchievement


T = TypeVar("T", bound="RAUserGameProgression")


@_attrs_define
class RAUserGameProgression:
    """
    Attributes:
        rom_ra_id (int | None):
        max_possible (int | None):
        num_awarded (int | None):
        num_awarded_hardcore (int | None):
        earned_achievements (list[EarnedAchievement]):
        most_recent_awarded_date (None | str | Unset):
    """

    rom_ra_id: int | None
    max_possible: int | None
    num_awarded: int | None
    num_awarded_hardcore: int | None
    earned_achievements: list[EarnedAchievement]
    most_recent_awarded_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rom_ra_id: int | None
        rom_ra_id = self.rom_ra_id

        max_possible: int | None
        max_possible = self.max_possible

        num_awarded: int | None
        num_awarded = self.num_awarded

        num_awarded_hardcore: int | None
        num_awarded_hardcore = self.num_awarded_hardcore

        earned_achievements = []
        for earned_achievements_item_data in self.earned_achievements:
            earned_achievements_item = earned_achievements_item_data.to_dict()
            earned_achievements.append(earned_achievements_item)

        most_recent_awarded_date: None | str | Unset
        if isinstance(self.most_recent_awarded_date, Unset):
            most_recent_awarded_date = UNSET
        else:
            most_recent_awarded_date = self.most_recent_awarded_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rom_ra_id": rom_ra_id,
                "max_possible": max_possible,
                "num_awarded": num_awarded,
                "num_awarded_hardcore": num_awarded_hardcore,
                "earned_achievements": earned_achievements,
            }
        )
        if most_recent_awarded_date is not UNSET:
            field_dict["most_recent_awarded_date"] = most_recent_awarded_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.earned_achievement import EarnedAchievement

        d = dict(src_dict)

        def _parse_rom_ra_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rom_ra_id = _parse_rom_ra_id(d.pop("rom_ra_id"))

        def _parse_max_possible(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_possible = _parse_max_possible(d.pop("max_possible"))

        def _parse_num_awarded(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        num_awarded = _parse_num_awarded(d.pop("num_awarded"))

        def _parse_num_awarded_hardcore(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        num_awarded_hardcore = _parse_num_awarded_hardcore(d.pop("num_awarded_hardcore"))

        earned_achievements = []
        _earned_achievements = d.pop("earned_achievements")
        for earned_achievements_item_data in _earned_achievements:
            earned_achievements_item = EarnedAchievement.from_dict(earned_achievements_item_data)

            earned_achievements.append(earned_achievements_item)

        def _parse_most_recent_awarded_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        most_recent_awarded_date = _parse_most_recent_awarded_date(d.pop("most_recent_awarded_date", UNSET))

        ra_user_game_progression = cls(
            rom_ra_id=rom_ra_id,
            max_possible=max_possible,
            num_awarded=num_awarded,
            num_awarded_hardcore=num_awarded_hardcore,
            earned_achievements=earned_achievements,
            most_recent_awarded_date=most_recent_awarded_date,
        )

        ra_user_game_progression.additional_properties = d
        return ra_user_game_progression

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
