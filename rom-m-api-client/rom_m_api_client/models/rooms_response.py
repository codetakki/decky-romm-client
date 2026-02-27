from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RoomsResponse")


@_attrs_define
class RoomsResponse:
    """
    Attributes:
        room_name (str):
        current (int):
        max_ (int):
        player_name (str):
        has_password (bool):
    """

    room_name: str
    current: int
    max_: int
    player_name: str
    has_password: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        room_name = self.room_name

        current = self.current

        max_ = self.max_

        player_name = self.player_name

        has_password = self.has_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "room_name": room_name,
                "current": current,
                "max": max_,
                "player_name": player_name,
                "hasPassword": has_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_name = d.pop("room_name")

        current = d.pop("current")

        max_ = d.pop("max")

        player_name = d.pop("player_name")

        has_password = d.pop("hasPassword")

        rooms_response = cls(
            room_name=room_name,
            current=current,
            max_=max_,
            player_name=player_name,
            has_password=has_password,
        )

        rooms_response.additional_properties = d
        return rooms_response

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
