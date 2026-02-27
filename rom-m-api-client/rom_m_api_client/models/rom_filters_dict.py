from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RomFiltersDict")


@_attrs_define
class RomFiltersDict:
    """
    Attributes:
        genres (list[str]):
        franchises (list[str]):
        collections (list[str]):
        companies (list[str]):
        game_modes (list[str]):
        age_ratings (list[str]):
        player_counts (list[str]):
        regions (list[str]):
        languages (list[str]):
        platforms (list[int]):
    """

    genres: list[str]
    franchises: list[str]
    collections: list[str]
    companies: list[str]
    game_modes: list[str]
    age_ratings: list[str]
    player_counts: list[str]
    regions: list[str]
    languages: list[str]
    platforms: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        genres = self.genres

        franchises = self.franchises

        collections = self.collections

        companies = self.companies

        game_modes = self.game_modes

        age_ratings = self.age_ratings

        player_counts = self.player_counts

        regions = self.regions

        languages = self.languages

        platforms = self.platforms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "genres": genres,
                "franchises": franchises,
                "collections": collections,
                "companies": companies,
                "game_modes": game_modes,
                "age_ratings": age_ratings,
                "player_counts": player_counts,
                "regions": regions,
                "languages": languages,
                "platforms": platforms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        genres = cast(list[str], d.pop("genres"))

        franchises = cast(list[str], d.pop("franchises"))

        collections = cast(list[str], d.pop("collections"))

        companies = cast(list[str], d.pop("companies"))

        game_modes = cast(list[str], d.pop("game_modes"))

        age_ratings = cast(list[str], d.pop("age_ratings"))

        player_counts = cast(list[str], d.pop("player_counts"))

        regions = cast(list[str], d.pop("regions"))

        languages = cast(list[str], d.pop("languages"))

        platforms = cast(list[int], d.pop("platforms"))

        rom_filters_dict = cls(
            genres=genres,
            franchises=franchises,
            collections=collections,
            companies=companies,
            game_modes=game_modes,
            age_ratings=age_ratings,
            player_counts=player_counts,
            regions=regions,
            languages=languages,
            platforms=platforms,
        )

        rom_filters_dict.additional_properties = d
        return rom_filters_dict

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
