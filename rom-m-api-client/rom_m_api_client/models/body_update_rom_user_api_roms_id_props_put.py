from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyUpdateRomUserApiRomsIdPropsPut")


@_attrs_define
class BodyUpdateRomUserApiRomsIdPropsPut:
    """
    Attributes:
        update_last_played (bool | Unset): Whether to update the last played date. Default: False.
        remove_last_played (bool | Unset): Whether to remove the last played date. Default: False.
    """

    update_last_played: bool | Unset = False
    remove_last_played: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        update_last_played = self.update_last_played

        remove_last_played = self.remove_last_played

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if update_last_played is not UNSET:
            field_dict["update_last_played"] = update_last_played
        if remove_last_played is not UNSET:
            field_dict["remove_last_played"] = remove_last_played

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        update_last_played = d.pop("update_last_played", UNSET)

        remove_last_played = d.pop("remove_last_played", UNSET)

        body_update_rom_user_api_roms_id_props_put = cls(
            update_last_played=update_last_played,
            remove_last_played=remove_last_played,
        )

        body_update_rom_user_api_roms_id_props_put.additional_properties = d
        return body_update_rom_user_api_roms_id_props_put

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
