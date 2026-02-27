from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FrontendDict")


@_attrs_define
class FrontendDict:
    """
    Attributes:
        upload_timeout (int):
        disable_userpass_login (bool):
        youtube_base_url (str):
    """

    upload_timeout: int
    disable_userpass_login: bool
    youtube_base_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_timeout = self.upload_timeout

        disable_userpass_login = self.disable_userpass_login

        youtube_base_url = self.youtube_base_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "UPLOAD_TIMEOUT": upload_timeout,
                "DISABLE_USERPASS_LOGIN": disable_userpass_login,
                "YOUTUBE_BASE_URL": youtube_base_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_timeout = d.pop("UPLOAD_TIMEOUT")

        disable_userpass_login = d.pop("DISABLE_USERPASS_LOGIN")

        youtube_base_url = d.pop("YOUTUBE_BASE_URL")

        frontend_dict = cls(
            upload_timeout=upload_timeout,
            disable_userpass_login=disable_userpass_login,
            youtube_base_url=youtube_base_url,
        )

        frontend_dict.additional_properties = d
        return frontend_dict

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
