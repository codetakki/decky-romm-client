from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManualMetadata")


@_attrs_define
class ManualMetadata:
    """
    Attributes:
        genres (list[str] | None | Unset):
        franchises (list[str] | None | Unset):
        companies (list[str] | None | Unset):
        game_modes (list[str] | None | Unset):
        age_ratings (list[str] | None | Unset):
        first_release_date (int | None | Unset):
        youtube_video_id (None | str | Unset):
    """

    genres: list[str] | None | Unset = UNSET
    franchises: list[str] | None | Unset = UNSET
    companies: list[str] | None | Unset = UNSET
    game_modes: list[str] | None | Unset = UNSET
    age_ratings: list[str] | None | Unset = UNSET
    first_release_date: int | None | Unset = UNSET
    youtube_video_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        genres: list[str] | None | Unset
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        franchises: list[str] | None | Unset
        if isinstance(self.franchises, Unset):
            franchises = UNSET
        elif isinstance(self.franchises, list):
            franchises = self.franchises

        else:
            franchises = self.franchises

        companies: list[str] | None | Unset
        if isinstance(self.companies, Unset):
            companies = UNSET
        elif isinstance(self.companies, list):
            companies = self.companies

        else:
            companies = self.companies

        game_modes: list[str] | None | Unset
        if isinstance(self.game_modes, Unset):
            game_modes = UNSET
        elif isinstance(self.game_modes, list):
            game_modes = self.game_modes

        else:
            game_modes = self.game_modes

        age_ratings: list[str] | None | Unset
        if isinstance(self.age_ratings, Unset):
            age_ratings = UNSET
        elif isinstance(self.age_ratings, list):
            age_ratings = self.age_ratings

        else:
            age_ratings = self.age_ratings

        first_release_date: int | None | Unset
        if isinstance(self.first_release_date, Unset):
            first_release_date = UNSET
        else:
            first_release_date = self.first_release_date

        youtube_video_id: None | str | Unset
        if isinstance(self.youtube_video_id, Unset):
            youtube_video_id = UNSET
        else:
            youtube_video_id = self.youtube_video_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if genres is not UNSET:
            field_dict["genres"] = genres
        if franchises is not UNSET:
            field_dict["franchises"] = franchises
        if companies is not UNSET:
            field_dict["companies"] = companies
        if game_modes is not UNSET:
            field_dict["game_modes"] = game_modes
        if age_ratings is not UNSET:
            field_dict["age_ratings"] = age_ratings
        if first_release_date is not UNSET:
            field_dict["first_release_date"] = first_release_date
        if youtube_video_id is not UNSET:
            field_dict["youtube_video_id"] = youtube_video_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_genres(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = cast(list[str], data)

                return genres_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        genres = _parse_genres(d.pop("genres", UNSET))

        def _parse_franchises(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                franchises_type_0 = cast(list[str], data)

                return franchises_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        franchises = _parse_franchises(d.pop("franchises", UNSET))

        def _parse_companies(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                companies_type_0 = cast(list[str], data)

                return companies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        companies = _parse_companies(d.pop("companies", UNSET))

        def _parse_game_modes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                game_modes_type_0 = cast(list[str], data)

                return game_modes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        game_modes = _parse_game_modes(d.pop("game_modes", UNSET))

        def _parse_age_ratings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                age_ratings_type_0 = cast(list[str], data)

                return age_ratings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        age_ratings = _parse_age_ratings(d.pop("age_ratings", UNSET))

        def _parse_first_release_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_release_date = _parse_first_release_date(d.pop("first_release_date", UNSET))

        def _parse_youtube_video_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        youtube_video_id = _parse_youtube_video_id(d.pop("youtube_video_id", UNSET))

        manual_metadata = cls(
            genres=genres,
            franchises=franchises,
            companies=companies,
            game_modes=game_modes,
            age_ratings=age_ratings,
            first_release_date=first_release_date,
            youtube_video_id=youtube_video_id,
        )

        manual_metadata.additional_properties = d
        return manual_metadata

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
