from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserNoteSchema")


@_attrs_define
class UserNoteSchema:
    """
    Attributes:
        id (int):
        title (str):
        content (str):
        is_public (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        user_id (int):
        username (str):
        tags (list[str] | None | Unset):
    """

    id: int
    title: str
    content: str
    is_public: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_id: int
    username: str
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        content = self.content

        is_public = self.is_public

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        username = self.username

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "content": content,
                "is_public": is_public,
                "created_at": created_at,
                "updated_at": updated_at,
                "user_id": user_id,
                "username": username,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        content = d.pop("content")

        is_public = d.pop("is_public")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        user_id = d.pop("user_id")

        username = d.pop("username")

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        user_note_schema = cls(
            id=id,
            title=title,
            content=content,
            is_public=is_public,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            username=username,
            tags=tags,
        )

        user_note_schema.additional_properties = d
        return user_note_schema

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
