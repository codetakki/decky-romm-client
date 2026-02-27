from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchRomSchema")


@_attrs_define
class SearchRomSchema:
    """
    Attributes:
        platform_id (int):
        name (str):
        is_unidentified (bool):
        is_identified (bool):
        id (int | None | Unset):
        igdb_id (int | None | Unset):
        moby_id (int | None | Unset):
        ss_id (int | None | Unset):
        sgdb_id (int | None | Unset):
        flashpoint_id (None | str | Unset):
        launchbox_id (int | None | Unset):
        slug (str | Unset):  Default: ''.
        summary (str | Unset):  Default: ''.
        igdb_url_cover (str | Unset):  Default: ''.
        moby_url_cover (str | Unset):  Default: ''.
        ss_url_cover (str | Unset):  Default: ''.
        sgdb_url_cover (str | Unset):  Default: ''.
        flashpoint_url_cover (str | Unset):  Default: ''.
        launchbox_url_cover (str | Unset):  Default: ''.
    """

    platform_id: int
    name: str
    is_unidentified: bool
    is_identified: bool
    id: int | None | Unset = UNSET
    igdb_id: int | None | Unset = UNSET
    moby_id: int | None | Unset = UNSET
    ss_id: int | None | Unset = UNSET
    sgdb_id: int | None | Unset = UNSET
    flashpoint_id: None | str | Unset = UNSET
    launchbox_id: int | None | Unset = UNSET
    slug: str | Unset = ""
    summary: str | Unset = ""
    igdb_url_cover: str | Unset = ""
    moby_url_cover: str | Unset = ""
    ss_url_cover: str | Unset = ""
    sgdb_url_cover: str | Unset = ""
    flashpoint_url_cover: str | Unset = ""
    launchbox_url_cover: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_id = self.platform_id

        name = self.name

        is_unidentified = self.is_unidentified

        is_identified = self.is_identified

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        igdb_id: int | None | Unset
        if isinstance(self.igdb_id, Unset):
            igdb_id = UNSET
        else:
            igdb_id = self.igdb_id

        moby_id: int | None | Unset
        if isinstance(self.moby_id, Unset):
            moby_id = UNSET
        else:
            moby_id = self.moby_id

        ss_id: int | None | Unset
        if isinstance(self.ss_id, Unset):
            ss_id = UNSET
        else:
            ss_id = self.ss_id

        sgdb_id: int | None | Unset
        if isinstance(self.sgdb_id, Unset):
            sgdb_id = UNSET
        else:
            sgdb_id = self.sgdb_id

        flashpoint_id: None | str | Unset
        if isinstance(self.flashpoint_id, Unset):
            flashpoint_id = UNSET
        else:
            flashpoint_id = self.flashpoint_id

        launchbox_id: int | None | Unset
        if isinstance(self.launchbox_id, Unset):
            launchbox_id = UNSET
        else:
            launchbox_id = self.launchbox_id

        slug = self.slug

        summary = self.summary

        igdb_url_cover = self.igdb_url_cover

        moby_url_cover = self.moby_url_cover

        ss_url_cover = self.ss_url_cover

        sgdb_url_cover = self.sgdb_url_cover

        flashpoint_url_cover = self.flashpoint_url_cover

        launchbox_url_cover = self.launchbox_url_cover

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform_id": platform_id,
                "name": name,
                "is_unidentified": is_unidentified,
                "is_identified": is_identified,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if igdb_id is not UNSET:
            field_dict["igdb_id"] = igdb_id
        if moby_id is not UNSET:
            field_dict["moby_id"] = moby_id
        if ss_id is not UNSET:
            field_dict["ss_id"] = ss_id
        if sgdb_id is not UNSET:
            field_dict["sgdb_id"] = sgdb_id
        if flashpoint_id is not UNSET:
            field_dict["flashpoint_id"] = flashpoint_id
        if launchbox_id is not UNSET:
            field_dict["launchbox_id"] = launchbox_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if summary is not UNSET:
            field_dict["summary"] = summary
        if igdb_url_cover is not UNSET:
            field_dict["igdb_url_cover"] = igdb_url_cover
        if moby_url_cover is not UNSET:
            field_dict["moby_url_cover"] = moby_url_cover
        if ss_url_cover is not UNSET:
            field_dict["ss_url_cover"] = ss_url_cover
        if sgdb_url_cover is not UNSET:
            field_dict["sgdb_url_cover"] = sgdb_url_cover
        if flashpoint_url_cover is not UNSET:
            field_dict["flashpoint_url_cover"] = flashpoint_url_cover
        if launchbox_url_cover is not UNSET:
            field_dict["launchbox_url_cover"] = launchbox_url_cover

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform_id = d.pop("platform_id")

        name = d.pop("name")

        is_unidentified = d.pop("is_unidentified")

        is_identified = d.pop("is_identified")

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_igdb_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        igdb_id = _parse_igdb_id(d.pop("igdb_id", UNSET))

        def _parse_moby_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        moby_id = _parse_moby_id(d.pop("moby_id", UNSET))

        def _parse_ss_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ss_id = _parse_ss_id(d.pop("ss_id", UNSET))

        def _parse_sgdb_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sgdb_id = _parse_sgdb_id(d.pop("sgdb_id", UNSET))

        def _parse_flashpoint_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flashpoint_id = _parse_flashpoint_id(d.pop("flashpoint_id", UNSET))

        def _parse_launchbox_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        launchbox_id = _parse_launchbox_id(d.pop("launchbox_id", UNSET))

        slug = d.pop("slug", UNSET)

        summary = d.pop("summary", UNSET)

        igdb_url_cover = d.pop("igdb_url_cover", UNSET)

        moby_url_cover = d.pop("moby_url_cover", UNSET)

        ss_url_cover = d.pop("ss_url_cover", UNSET)

        sgdb_url_cover = d.pop("sgdb_url_cover", UNSET)

        flashpoint_url_cover = d.pop("flashpoint_url_cover", UNSET)

        launchbox_url_cover = d.pop("launchbox_url_cover", UNSET)

        search_rom_schema = cls(
            platform_id=platform_id,
            name=name,
            is_unidentified=is_unidentified,
            is_identified=is_identified,
            id=id,
            igdb_id=igdb_id,
            moby_id=moby_id,
            ss_id=ss_id,
            sgdb_id=sgdb_id,
            flashpoint_id=flashpoint_id,
            launchbox_id=launchbox_id,
            slug=slug,
            summary=summary,
            igdb_url_cover=igdb_url_cover,
            moby_url_cover=moby_url_cover,
            ss_url_cover=ss_url_cover,
            sgdb_url_cover=sgdb_url_cover,
            flashpoint_url_cover=flashpoint_url_cover,
            launchbox_url_cover=launchbox_url_cover,
        )

        search_rom_schema.additional_properties = d
        return search_rom_schema

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
