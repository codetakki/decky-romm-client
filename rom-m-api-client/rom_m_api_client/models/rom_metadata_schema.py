from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RomMetadataSchema")


@_attrs_define
class RomMetadataSchema:
    """
    Attributes:
        rom_id (int):
        genres (list[str]):
        franchises (list[str]):
        collections (list[str]):
        companies (list[str]):
        game_modes (list[str]):
        age_ratings (list[str]):
        player_count (str):
        first_release_date (int | None):
        average_rating (float | None):
    """

    rom_id: int
    genres: list[str]
    franchises: list[str]
    collections: list[str]
    companies: list[str]
    game_modes: list[str]
    age_ratings: list[str]
    player_count: str
    first_release_date: int | None
    average_rating: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rom_id = self.rom_id

        genres = self.genres

        franchises = self.franchises

        collections = self.collections

        companies = self.companies

        game_modes = self.game_modes

        age_ratings = self.age_ratings

        player_count = self.player_count

        first_release_date: int | None
        first_release_date = self.first_release_date

        average_rating: float | None
        average_rating = self.average_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rom_id": rom_id,
                "genres": genres,
                "franchises": franchises,
                "collections": collections,
                "companies": companies,
                "game_modes": game_modes,
                "age_ratings": age_ratings,
                "player_count": player_count,
                "first_release_date": first_release_date,
                "average_rating": average_rating,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rom_id = d.pop("rom_id")

        genres = cast(list[str], d.pop("genres"))

        franchises = cast(list[str], d.pop("franchises"))

        collections = cast(list[str], d.pop("collections"))

        companies = cast(list[str], d.pop("companies"))

        game_modes = cast(list[str], d.pop("game_modes"))

        age_ratings = cast(list[str], d.pop("age_ratings"))

        player_count = d.pop("player_count")

        def _parse_first_release_date(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        first_release_date = _parse_first_release_date(d.pop("first_release_date"))

        def _parse_average_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        average_rating = _parse_average_rating(d.pop("average_rating"))

        rom_metadata_schema = cls(
            rom_id=rom_id,
            genres=genres,
            franchises=franchises,
            collections=collections,
            companies=companies,
            game_modes=game_modes,
            age_ratings=age_ratings,
            player_count=player_count,
            first_release_date=first_release_date,
            average_rating=average_rating,
        )

        rom_metadata_schema.additional_properties = d
        return rom_metadata_schema

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
