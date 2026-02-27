from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webrcade_feed_item_schema import WebrcadeFeedItemSchema


T = TypeVar("T", bound="WebrcadeFeedCategorySchema")


@_attrs_define
class WebrcadeFeedCategorySchema:
    """
    Attributes:
        title (str):
        items (list[WebrcadeFeedItemSchema]):
        long_title (str | Unset):
        background (str | Unset):
        thumbnail (str | Unset):
        description (str | Unset):
    """

    title: str
    items: list[WebrcadeFeedItemSchema]
    long_title: str | Unset = UNSET
    background: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        long_title = self.long_title

        background = self.background

        thumbnail = self.thumbnail

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "items": items,
            }
        )
        if long_title is not UNSET:
            field_dict["longTitle"] = long_title
        if background is not UNSET:
            field_dict["background"] = background
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webrcade_feed_item_schema import WebrcadeFeedItemSchema

        d = dict(src_dict)
        title = d.pop("title")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = WebrcadeFeedItemSchema.from_dict(items_item_data)

            items.append(items_item)

        long_title = d.pop("longTitle", UNSET)

        background = d.pop("background", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        description = d.pop("description", UNSET)

        webrcade_feed_category_schema = cls(
            title=title,
            items=items,
            long_title=long_title,
            background=background,
            thumbnail=thumbnail,
            description=description,
        )

        webrcade_feed_category_schema.additional_properties = d
        return webrcade_feed_category_schema

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
