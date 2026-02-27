from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetplayICEServer")


@_attrs_define
class NetplayICEServer:
    """
    Attributes:
        urls (str):
        username (str | Unset):
        credential (str | Unset):
    """

    urls: str
    username: str | Unset = UNSET
    credential: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        urls = self.urls

        username = self.username

        credential = self.credential

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "urls": urls,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if credential is not UNSET:
            field_dict["credential"] = credential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        urls = d.pop("urls")

        username = d.pop("username", UNSET)

        credential = d.pop("credential", UNSET)

        netplay_ice_server = cls(
            urls=urls,
            username=username,
            credential=credential,
        )

        netplay_ice_server.additional_properties = d
        return netplay_ice_server

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
