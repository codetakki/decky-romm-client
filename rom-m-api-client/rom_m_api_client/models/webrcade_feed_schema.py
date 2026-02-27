from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webrcade_feed_category_schema import WebrcadeFeedCategorySchema


T = TypeVar("T", bound="WebrcadeFeedSchema")


@_attrs_define
class WebrcadeFeedSchema:
    """
    Attributes:
        title (str):
        categories (list[WebrcadeFeedCategorySchema]):
        long_title (str | Unset):
        description (str | Unset):
        thumbnail (str | Unset):
        background (str | Unset):
    """

    title: str
    categories: list[WebrcadeFeedCategorySchema]
    long_title: str | Unset = UNSET
    description: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    background: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        long_title = self.long_title

        description = self.description

        thumbnail = self.thumbnail

        background = self.background

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "categories": categories,
            }
        )
        if long_title is not UNSET:
            field_dict["longTitle"] = long_title
        if description is not UNSET:
            field_dict["description"] = description
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if background is not UNSET:
            field_dict["background"] = background

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webrcade_feed_category_schema import WebrcadeFeedCategorySchema

        d = dict(src_dict)
        title = d.pop("title")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = WebrcadeFeedCategorySchema.from_dict(categories_item_data)

            categories.append(categories_item)

        long_title = d.pop("longTitle", UNSET)

        description = d.pop("description", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        background = d.pop("background", UNSET)

        webrcade_feed_schema = cls(
            title=title,
            categories=categories,
            long_title=long_title,
            description=description,
            thumbnail=thumbnail,
            background=background,
        )

        webrcade_feed_schema.additional_properties = d
        return webrcade_feed_schema

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
