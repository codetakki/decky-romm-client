from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.moby_metadata_platform import MobyMetadataPlatform


T = TypeVar("T", bound="RomMobyMetadata")


@_attrs_define
class RomMobyMetadata:
    """
    Attributes:
        moby_score (None | str | Unset):
        genres (list[str] | Unset):
        alternate_titles (list[str] | Unset):
        platforms (list[MobyMetadataPlatform] | Unset):
    """

    moby_score: None | str | Unset = UNSET
    genres: list[str] | Unset = UNSET
    alternate_titles: list[str] | Unset = UNSET
    platforms: list[MobyMetadataPlatform] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        moby_score: None | str | Unset
        if isinstance(self.moby_score, Unset):
            moby_score = UNSET
        else:
            moby_score = self.moby_score

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        alternate_titles: list[str] | Unset = UNSET
        if not isinstance(self.alternate_titles, Unset):
            alternate_titles = self.alternate_titles

        platforms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.to_dict()
                platforms.append(platforms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if moby_score is not UNSET:
            field_dict["moby_score"] = moby_score
        if genres is not UNSET:
            field_dict["genres"] = genres
        if alternate_titles is not UNSET:
            field_dict["alternate_titles"] = alternate_titles
        if platforms is not UNSET:
            field_dict["platforms"] = platforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.moby_metadata_platform import MobyMetadataPlatform

        d = dict(src_dict)

        def _parse_moby_score(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        moby_score = _parse_moby_score(d.pop("moby_score", UNSET))

        genres = cast(list[str], d.pop("genres", UNSET))

        alternate_titles = cast(list[str], d.pop("alternate_titles", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[MobyMetadataPlatform] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = MobyMetadataPlatform.from_dict(platforms_item_data)

                platforms.append(platforms_item)

        rom_moby_metadata = cls(
            moby_score=moby_score,
            genres=genres,
            alternate_titles=alternate_titles,
            platforms=platforms,
        )

        rom_moby_metadata.additional_properties = d
        return rom_moby_metadata

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
