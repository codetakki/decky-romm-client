from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.smart_collection_schema_filter_criteria import SmartCollectionSchemaFilterCriteria


T = TypeVar("T", bound="SmartCollectionSchema")


@_attrs_define
class SmartCollectionSchema:
    """
    Attributes:
        name (str):
        rom_ids (list[int]):
        rom_count (int):
        path_cover_small (None | str):
        path_cover_large (None | str):
        path_covers_small (list[str]):
        path_covers_large (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        id (int):
        filter_criteria (SmartCollectionSchemaFilterCriteria):
        filter_summary (str):
        user_id (int):
        user_username (str):
        description (str | Unset):  Default: ''.
        is_public (bool | Unset):  Default: False.
        is_favorite (bool | Unset):  Default: False.
        is_virtual (bool | Unset):  Default: False.
        is_smart (bool | Unset):  Default: True.
    """

    name: str
    rom_ids: list[int]
    rom_count: int
    path_cover_small: None | str
    path_cover_large: None | str
    path_covers_small: list[str]
    path_covers_large: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: int
    filter_criteria: SmartCollectionSchemaFilterCriteria
    filter_summary: str
    user_id: int
    user_username: str
    description: str | Unset = ""
    is_public: bool | Unset = False
    is_favorite: bool | Unset = False
    is_virtual: bool | Unset = False
    is_smart: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        rom_ids = self.rom_ids

        rom_count = self.rom_count

        path_cover_small: None | str
        path_cover_small = self.path_cover_small

        path_cover_large: None | str
        path_cover_large = self.path_cover_large

        path_covers_small = self.path_covers_small

        path_covers_large = self.path_covers_large

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id

        filter_criteria = self.filter_criteria.to_dict()

        filter_summary = self.filter_summary

        user_id = self.user_id

        user_username = self.user_username

        description = self.description

        is_public = self.is_public

        is_favorite = self.is_favorite

        is_virtual = self.is_virtual

        is_smart = self.is_smart

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "rom_ids": rom_ids,
                "rom_count": rom_count,
                "path_cover_small": path_cover_small,
                "path_cover_large": path_cover_large,
                "path_covers_small": path_covers_small,
                "path_covers_large": path_covers_large,
                "created_at": created_at,
                "updated_at": updated_at,
                "id": id,
                "filter_criteria": filter_criteria,
                "filter_summary": filter_summary,
                "user_id": user_id,
                "user__username": user_username,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if is_favorite is not UNSET:
            field_dict["is_favorite"] = is_favorite
        if is_virtual is not UNSET:
            field_dict["is_virtual"] = is_virtual
        if is_smart is not UNSET:
            field_dict["is_smart"] = is_smart

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.smart_collection_schema_filter_criteria import SmartCollectionSchemaFilterCriteria

        d = dict(src_dict)
        name = d.pop("name")

        rom_ids = cast(list[int], d.pop("rom_ids"))

        rom_count = d.pop("rom_count")

        def _parse_path_cover_small(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path_cover_small = _parse_path_cover_small(d.pop("path_cover_small"))

        def _parse_path_cover_large(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path_cover_large = _parse_path_cover_large(d.pop("path_cover_large"))

        path_covers_small = cast(list[str], d.pop("path_covers_small"))

        path_covers_large = cast(list[str], d.pop("path_covers_large"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        id = d.pop("id")

        filter_criteria = SmartCollectionSchemaFilterCriteria.from_dict(d.pop("filter_criteria"))

        filter_summary = d.pop("filter_summary")

        user_id = d.pop("user_id")

        user_username = d.pop("user__username")

        description = d.pop("description", UNSET)

        is_public = d.pop("is_public", UNSET)

        is_favorite = d.pop("is_favorite", UNSET)

        is_virtual = d.pop("is_virtual", UNSET)

        is_smart = d.pop("is_smart", UNSET)

        smart_collection_schema = cls(
            name=name,
            rom_ids=rom_ids,
            rom_count=rom_count,
            path_cover_small=path_cover_small,
            path_cover_large=path_cover_large,
            path_covers_small=path_covers_small,
            path_covers_large=path_covers_large,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            filter_criteria=filter_criteria,
            filter_summary=filter_summary,
            user_id=user_id,
            user_username=user_username,
            description=description,
            is_public=is_public,
            is_favorite=is_favorite,
            is_virtual=is_virtual,
            is_smart=is_smart,
        )

        smart_collection_schema.additional_properties = d
        return smart_collection_schema

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
