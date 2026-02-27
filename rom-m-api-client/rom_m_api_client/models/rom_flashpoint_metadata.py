from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RomFlashpointMetadata")


@_attrs_define
class RomFlashpointMetadata:
    """
    Attributes:
        franchises (list[str] | Unset):
        companies (list[str] | Unset):
        source (None | str | Unset):
        genres (list[str] | Unset):
        first_release_date (str | Unset):
        game_modes (list[str] | Unset):
        status (None | str | Unset):
        version (None | str | Unset):
        language (None | str | Unset):
        notes (None | str | Unset):
    """

    franchises: list[str] | Unset = UNSET
    companies: list[str] | Unset = UNSET
    source: None | str | Unset = UNSET
    genres: list[str] | Unset = UNSET
    first_release_date: str | Unset = UNSET
    game_modes: list[str] | Unset = UNSET
    status: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        franchises: list[str] | Unset = UNSET
        if not isinstance(self.franchises, Unset):
            franchises = self.franchises

        companies: list[str] | Unset = UNSET
        if not isinstance(self.companies, Unset):
            companies = self.companies

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        first_release_date = self.first_release_date

        game_modes: list[str] | Unset = UNSET
        if not isinstance(self.game_modes, Unset):
            game_modes = self.game_modes

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if franchises is not UNSET:
            field_dict["franchises"] = franchises
        if companies is not UNSET:
            field_dict["companies"] = companies
        if source is not UNSET:
            field_dict["source"] = source
        if genres is not UNSET:
            field_dict["genres"] = genres
        if first_release_date is not UNSET:
            field_dict["first_release_date"] = first_release_date
        if game_modes is not UNSET:
            field_dict["game_modes"] = game_modes
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version
        if language is not UNSET:
            field_dict["language"] = language
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        franchises = cast(list[str], d.pop("franchises", UNSET))

        companies = cast(list[str], d.pop("companies", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        genres = cast(list[str], d.pop("genres", UNSET))

        first_release_date = d.pop("first_release_date", UNSET)

        game_modes = cast(list[str], d.pop("game_modes", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        rom_flashpoint_metadata = cls(
            franchises=franchises,
            companies=companies,
            source=source,
            genres=genres,
            first_release_date=first_release_date,
            game_modes=game_modes,
            status=status,
            version=version,
            language=language,
            notes=notes,
        )

        rom_flashpoint_metadata.additional_properties = d
        return rom_flashpoint_metadata

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
