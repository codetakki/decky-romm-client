from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyUpdatePlatformApiPlatformsIdPut")


@_attrs_define
class BodyUpdatePlatformApiPlatformsIdPut:
    """
    Attributes:
        aspect_ratio (None | str | Unset): Cover aspect ratio.
        custom_name (None | str | Unset): Custom platform name.
    """

    aspect_ratio: None | str | Unset = UNSET
    custom_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aspect_ratio: None | str | Unset
        if isinstance(self.aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = self.aspect_ratio

        custom_name: None | str | Unset
        if isinstance(self.custom_name, Unset):
            custom_name = UNSET
        else:
            custom_name = self.custom_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_ratio is not UNSET:
            field_dict["aspect_ratio"] = aspect_ratio
        if custom_name is not UNSET:
            field_dict["custom_name"] = custom_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_aspect_ratio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aspect_ratio = _parse_aspect_ratio(d.pop("aspect_ratio", UNSET))

        def _parse_custom_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_name = _parse_custom_name(d.pop("custom_name", UNSET))

        body_update_platform_api_platforms_id_put = cls(
            aspect_ratio=aspect_ratio,
            custom_name=custom_name,
        )

        body_update_platform_api_platforms_id_put.additional_properties = d
        return body_update_platform_api_platforms_id_put

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
