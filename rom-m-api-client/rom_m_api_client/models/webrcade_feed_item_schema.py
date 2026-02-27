from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webrcade_feed_item_props_schema import WebrcadeFeedItemPropsSchema


T = TypeVar("T", bound="WebrcadeFeedItemSchema")


@_attrs_define
class WebrcadeFeedItemSchema:
    """
    Attributes:
        title (str):
        type_ (str):
        props (WebrcadeFeedItemPropsSchema):
        long_title (str | Unset):
        description (str | Unset):
        thumbnail (str | Unset):
        background (str | Unset):
    """

    title: str
    type_: str
    props: WebrcadeFeedItemPropsSchema
    long_title: str | Unset = UNSET
    description: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    background: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        type_ = self.type_

        props = self.props.to_dict()

        long_title = self.long_title

        description = self.description

        thumbnail = self.thumbnail

        background = self.background

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "type": type_,
                "props": props,
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
        from ..models.webrcade_feed_item_props_schema import WebrcadeFeedItemPropsSchema

        d = dict(src_dict)
        title = d.pop("title")

        type_ = d.pop("type")

        props = WebrcadeFeedItemPropsSchema.from_dict(d.pop("props"))

        long_title = d.pop("longTitle", UNSET)

        description = d.pop("description", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        background = d.pop("background", UNSET)

        webrcade_feed_item_schema = cls(
            title=title,
            type_=type_,
            props=props,
            long_title=long_title,
            description=description,
            thumbnail=thumbnail,
            background=background,
        )

        webrcade_feed_item_schema.additional_properties = d
        return webrcade_feed_item_schema

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
