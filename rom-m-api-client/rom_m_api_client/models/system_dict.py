from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemDict")


@_attrs_define
class SystemDict:
    """
    Attributes:
        version (str):
        show_setup_wizard (bool):
    """

    version: str
    show_setup_wizard: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        show_setup_wizard = self.show_setup_wizard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "VERSION": version,
                "SHOW_SETUP_WIZARD": show_setup_wizard,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("VERSION")

        show_setup_wizard = d.pop("SHOW_SETUP_WIZARD")

        system_dict = cls(
            version=version,
            show_setup_wizard=show_setup_wizard,
        )

        system_dict.additional_properties = d
        return system_dict

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
