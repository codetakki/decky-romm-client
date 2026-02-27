from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmulationDict")


@_attrs_define
class EmulationDict:
    """
    Attributes:
        disable_emulator_js (bool):
        disable_ruffle_rs (bool):
    """

    disable_emulator_js: bool
    disable_ruffle_rs: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_emulator_js = self.disable_emulator_js

        disable_ruffle_rs = self.disable_ruffle_rs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DISABLE_EMULATOR_JS": disable_emulator_js,
                "DISABLE_RUFFLE_RS": disable_ruffle_rs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disable_emulator_js = d.pop("DISABLE_EMULATOR_JS")

        disable_ruffle_rs = d.pop("DISABLE_RUFFLE_RS")

        emulation_dict = cls(
            disable_emulator_js=disable_emulator_js,
            disable_ruffle_rs=disable_ruffle_rs,
        )

        emulation_dict.additional_properties = d
        return emulation_dict

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
