from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firmware_schema import FirmwareSchema


T = TypeVar("T", bound="PlatformSchema")


@_attrs_define
class PlatformSchema:
    """
    Attributes:
        id (int):
        slug (str):
        fs_slug (str):
        rom_count (int):
        name (str):
        igdb_slug (None | str):
        moby_slug (None | str):
        hltb_slug (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        fs_size_bytes (int):
        is_unidentified (bool):
        is_identified (bool):
        missing_from_fs (bool):
        display_name (str):
        custom_name (None | str | Unset):
        igdb_id (int | None | Unset):
        sgdb_id (int | None | Unset):
        moby_id (int | None | Unset):
        launchbox_id (int | None | Unset):
        ss_id (int | None | Unset):
        ra_id (int | None | Unset):
        hasheous_id (int | None | Unset):
        tgdb_id (int | None | Unset):
        flashpoint_id (int | None | Unset):
        category (None | str | Unset):
        generation (int | None | Unset):
        family_name (None | str | Unset):
        family_slug (None | str | Unset):
        url (None | str | Unset):
        url_logo (None | str | Unset):
        firmware (list[FirmwareSchema] | Unset):
        aspect_ratio (str | Unset):  Default: '2 / 3'.
    """

    id: int
    slug: str
    fs_slug: str
    rom_count: int
    name: str
    igdb_slug: None | str
    moby_slug: None | str
    hltb_slug: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    fs_size_bytes: int
    is_unidentified: bool
    is_identified: bool
    missing_from_fs: bool
    display_name: str
    custom_name: None | str | Unset = UNSET
    igdb_id: int | None | Unset = UNSET
    sgdb_id: int | None | Unset = UNSET
    moby_id: int | None | Unset = UNSET
    launchbox_id: int | None | Unset = UNSET
    ss_id: int | None | Unset = UNSET
    ra_id: int | None | Unset = UNSET
    hasheous_id: int | None | Unset = UNSET
    tgdb_id: int | None | Unset = UNSET
    flashpoint_id: int | None | Unset = UNSET
    category: None | str | Unset = UNSET
    generation: int | None | Unset = UNSET
    family_name: None | str | Unset = UNSET
    family_slug: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    url_logo: None | str | Unset = UNSET
    firmware: list[FirmwareSchema] | Unset = UNSET
    aspect_ratio: str | Unset = "2 / 3"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        fs_slug = self.fs_slug

        rom_count = self.rom_count

        name = self.name

        igdb_slug: None | str
        igdb_slug = self.igdb_slug

        moby_slug: None | str
        moby_slug = self.moby_slug

        hltb_slug: None | str
        hltb_slug = self.hltb_slug

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        fs_size_bytes = self.fs_size_bytes

        is_unidentified = self.is_unidentified

        is_identified = self.is_identified

        missing_from_fs = self.missing_from_fs

        display_name = self.display_name

        custom_name: None | str | Unset
        if isinstance(self.custom_name, Unset):
            custom_name = UNSET
        else:
            custom_name = self.custom_name

        igdb_id: int | None | Unset
        if isinstance(self.igdb_id, Unset):
            igdb_id = UNSET
        else:
            igdb_id = self.igdb_id

        sgdb_id: int | None | Unset
        if isinstance(self.sgdb_id, Unset):
            sgdb_id = UNSET
        else:
            sgdb_id = self.sgdb_id

        moby_id: int | None | Unset
        if isinstance(self.moby_id, Unset):
            moby_id = UNSET
        else:
            moby_id = self.moby_id

        launchbox_id: int | None | Unset
        if isinstance(self.launchbox_id, Unset):
            launchbox_id = UNSET
        else:
            launchbox_id = self.launchbox_id

        ss_id: int | None | Unset
        if isinstance(self.ss_id, Unset):
            ss_id = UNSET
        else:
            ss_id = self.ss_id

        ra_id: int | None | Unset
        if isinstance(self.ra_id, Unset):
            ra_id = UNSET
        else:
            ra_id = self.ra_id

        hasheous_id: int | None | Unset
        if isinstance(self.hasheous_id, Unset):
            hasheous_id = UNSET
        else:
            hasheous_id = self.hasheous_id

        tgdb_id: int | None | Unset
        if isinstance(self.tgdb_id, Unset):
            tgdb_id = UNSET
        else:
            tgdb_id = self.tgdb_id

        flashpoint_id: int | None | Unset
        if isinstance(self.flashpoint_id, Unset):
            flashpoint_id = UNSET
        else:
            flashpoint_id = self.flashpoint_id

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        generation: int | None | Unset
        if isinstance(self.generation, Unset):
            generation = UNSET
        else:
            generation = self.generation

        family_name: None | str | Unset
        if isinstance(self.family_name, Unset):
            family_name = UNSET
        else:
            family_name = self.family_name

        family_slug: None | str | Unset
        if isinstance(self.family_slug, Unset):
            family_slug = UNSET
        else:
            family_slug = self.family_slug

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        url_logo: None | str | Unset
        if isinstance(self.url_logo, Unset):
            url_logo = UNSET
        else:
            url_logo = self.url_logo

        firmware: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.firmware, Unset):
            firmware = []
            for firmware_item_data in self.firmware:
                firmware_item = firmware_item_data.to_dict()
                firmware.append(firmware_item)

        aspect_ratio = self.aspect_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "fs_slug": fs_slug,
                "rom_count": rom_count,
                "name": name,
                "igdb_slug": igdb_slug,
                "moby_slug": moby_slug,
                "hltb_slug": hltb_slug,
                "created_at": created_at,
                "updated_at": updated_at,
                "fs_size_bytes": fs_size_bytes,
                "is_unidentified": is_unidentified,
                "is_identified": is_identified,
                "missing_from_fs": missing_from_fs,
                "display_name": display_name,
            }
        )
        if custom_name is not UNSET:
            field_dict["custom_name"] = custom_name
        if igdb_id is not UNSET:
            field_dict["igdb_id"] = igdb_id
        if sgdb_id is not UNSET:
            field_dict["sgdb_id"] = sgdb_id
        if moby_id is not UNSET:
            field_dict["moby_id"] = moby_id
        if launchbox_id is not UNSET:
            field_dict["launchbox_id"] = launchbox_id
        if ss_id is not UNSET:
            field_dict["ss_id"] = ss_id
        if ra_id is not UNSET:
            field_dict["ra_id"] = ra_id
        if hasheous_id is not UNSET:
            field_dict["hasheous_id"] = hasheous_id
        if tgdb_id is not UNSET:
            field_dict["tgdb_id"] = tgdb_id
        if flashpoint_id is not UNSET:
            field_dict["flashpoint_id"] = flashpoint_id
        if category is not UNSET:
            field_dict["category"] = category
        if generation is not UNSET:
            field_dict["generation"] = generation
        if family_name is not UNSET:
            field_dict["family_name"] = family_name
        if family_slug is not UNSET:
            field_dict["family_slug"] = family_slug
        if url is not UNSET:
            field_dict["url"] = url
        if url_logo is not UNSET:
            field_dict["url_logo"] = url_logo
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if aspect_ratio is not UNSET:
            field_dict["aspect_ratio"] = aspect_ratio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firmware_schema import FirmwareSchema

        d = dict(src_dict)
        id = d.pop("id")

        slug = d.pop("slug")

        fs_slug = d.pop("fs_slug")

        rom_count = d.pop("rom_count")

        name = d.pop("name")

        def _parse_igdb_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        igdb_slug = _parse_igdb_slug(d.pop("igdb_slug"))

        def _parse_moby_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        moby_slug = _parse_moby_slug(d.pop("moby_slug"))

        def _parse_hltb_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hltb_slug = _parse_hltb_slug(d.pop("hltb_slug"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        fs_size_bytes = d.pop("fs_size_bytes")

        is_unidentified = d.pop("is_unidentified")

        is_identified = d.pop("is_identified")

        missing_from_fs = d.pop("missing_from_fs")

        display_name = d.pop("display_name")

        def _parse_custom_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_name = _parse_custom_name(d.pop("custom_name", UNSET))

        def _parse_igdb_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        igdb_id = _parse_igdb_id(d.pop("igdb_id", UNSET))

        def _parse_sgdb_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sgdb_id = _parse_sgdb_id(d.pop("sgdb_id", UNSET))

        def _parse_moby_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        moby_id = _parse_moby_id(d.pop("moby_id", UNSET))

        def _parse_launchbox_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        launchbox_id = _parse_launchbox_id(d.pop("launchbox_id", UNSET))

        def _parse_ss_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ss_id = _parse_ss_id(d.pop("ss_id", UNSET))

        def _parse_ra_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ra_id = _parse_ra_id(d.pop("ra_id", UNSET))

        def _parse_hasheous_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hasheous_id = _parse_hasheous_id(d.pop("hasheous_id", UNSET))

        def _parse_tgdb_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tgdb_id = _parse_tgdb_id(d.pop("tgdb_id", UNSET))

        def _parse_flashpoint_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flashpoint_id = _parse_flashpoint_id(d.pop("flashpoint_id", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_generation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        generation = _parse_generation(d.pop("generation", UNSET))

        def _parse_family_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_name = _parse_family_name(d.pop("family_name", UNSET))

        def _parse_family_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_slug = _parse_family_slug(d.pop("family_slug", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_url_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_logo = _parse_url_logo(d.pop("url_logo", UNSET))

        _firmware = d.pop("firmware", UNSET)
        firmware: list[FirmwareSchema] | Unset = UNSET
        if _firmware is not UNSET:
            firmware = []
            for firmware_item_data in _firmware:
                firmware_item = FirmwareSchema.from_dict(firmware_item_data)

                firmware.append(firmware_item)

        aspect_ratio = d.pop("aspect_ratio", UNSET)

        platform_schema = cls(
            id=id,
            slug=slug,
            fs_slug=fs_slug,
            rom_count=rom_count,
            name=name,
            igdb_slug=igdb_slug,
            moby_slug=moby_slug,
            hltb_slug=hltb_slug,
            created_at=created_at,
            updated_at=updated_at,
            fs_size_bytes=fs_size_bytes,
            is_unidentified=is_unidentified,
            is_identified=is_identified,
            missing_from_fs=missing_from_fs,
            display_name=display_name,
            custom_name=custom_name,
            igdb_id=igdb_id,
            sgdb_id=sgdb_id,
            moby_id=moby_id,
            launchbox_id=launchbox_id,
            ss_id=ss_id,
            ra_id=ra_id,
            hasheous_id=hasheous_id,
            tgdb_id=tgdb_id,
            flashpoint_id=flashpoint_id,
            category=category,
            generation=generation,
            family_name=family_name,
            family_slug=family_slug,
            url=url,
            url_logo=url_logo,
            firmware=firmware,
            aspect_ratio=aspect_ratio,
        )

        platform_schema.additional_properties = d
        return platform_schema

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
