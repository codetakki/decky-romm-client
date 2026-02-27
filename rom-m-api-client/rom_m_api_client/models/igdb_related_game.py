from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IGDBRelatedGame")


@_attrs_define
class IGDBRelatedGame:
    """
    Attributes:
        id (int):
        name (str):
        slug (str):
        type_ (str):
        cover_url (str):
    """

    id: int
    name: str
    slug: str
    type_: str
    cover_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        type_ = self.type_

        cover_url = self.cover_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "type": type_,
                "cover_url": cover_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        type_ = d.pop("type")

        cover_url = d.pop("cover_url")

        igdb_related_game = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            cover_url=cover_url,
        )

        igdb_related_game.additional_properties = d
        return igdb_related_game

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
