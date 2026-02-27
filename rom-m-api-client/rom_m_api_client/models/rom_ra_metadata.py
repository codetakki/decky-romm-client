from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ra_game_rom_achievement import RAGameRomAchievement


T = TypeVar("T", bound="RomRAMetadata")


@_attrs_define
class RomRAMetadata:
    """
    Attributes:
        first_release_date (int | None | Unset):
        genres (list[str] | Unset):
        companies (list[str] | Unset):
        achievements (list[RAGameRomAchievement] | Unset):
    """

    first_release_date: int | None | Unset = UNSET
    genres: list[str] | Unset = UNSET
    companies: list[str] | Unset = UNSET
    achievements: list[RAGameRomAchievement] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_release_date: int | None | Unset
        if isinstance(self.first_release_date, Unset):
            first_release_date = UNSET
        else:
            first_release_date = self.first_release_date

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        companies: list[str] | Unset = UNSET
        if not isinstance(self.companies, Unset):
            companies = self.companies

        achievements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.achievements, Unset):
            achievements = []
            for achievements_item_data in self.achievements:
                achievements_item = achievements_item_data.to_dict()
                achievements.append(achievements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_release_date is not UNSET:
            field_dict["first_release_date"] = first_release_date
        if genres is not UNSET:
            field_dict["genres"] = genres
        if companies is not UNSET:
            field_dict["companies"] = companies
        if achievements is not UNSET:
            field_dict["achievements"] = achievements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ra_game_rom_achievement import RAGameRomAchievement

        d = dict(src_dict)

        def _parse_first_release_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_release_date = _parse_first_release_date(d.pop("first_release_date", UNSET))

        genres = cast(list[str], d.pop("genres", UNSET))

        companies = cast(list[str], d.pop("companies", UNSET))

        _achievements = d.pop("achievements", UNSET)
        achievements: list[RAGameRomAchievement] | Unset = UNSET
        if _achievements is not UNSET:
            achievements = []
            for achievements_item_data in _achievements:
                achievements_item = RAGameRomAchievement.from_dict(achievements_item_data)

                achievements.append(achievements_item)

        rom_ra_metadata = cls(
            first_release_date=first_release_date,
            genres=genres,
            companies=companies,
            achievements=achievements,
        )

        rom_ra_metadata.additional_properties = d
        return rom_ra_metadata

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
