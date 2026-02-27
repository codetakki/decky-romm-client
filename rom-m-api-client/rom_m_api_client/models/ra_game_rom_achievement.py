from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RAGameRomAchievement")


@_attrs_define
class RAGameRomAchievement:
    """
    Attributes:
        ra_id (int | None):
        title (None | str):
        description (None | str):
        points (int | None):
        num_awarded (int | None):
        num_awarded_hardcore (int | None):
        badge_id (None | str):
        badge_url_lock (None | str):
        badge_path_lock (None | str):
        badge_url (None | str):
        badge_path (None | str):
        display_order (int | None):
        type_ (None | str):
    """

    ra_id: int | None
    title: None | str
    description: None | str
    points: int | None
    num_awarded: int | None
    num_awarded_hardcore: int | None
    badge_id: None | str
    badge_url_lock: None | str
    badge_path_lock: None | str
    badge_url: None | str
    badge_path: None | str
    display_order: int | None
    type_: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ra_id: int | None
        ra_id = self.ra_id

        title: None | str
        title = self.title

        description: None | str
        description = self.description

        points: int | None
        points = self.points

        num_awarded: int | None
        num_awarded = self.num_awarded

        num_awarded_hardcore: int | None
        num_awarded_hardcore = self.num_awarded_hardcore

        badge_id: None | str
        badge_id = self.badge_id

        badge_url_lock: None | str
        badge_url_lock = self.badge_url_lock

        badge_path_lock: None | str
        badge_path_lock = self.badge_path_lock

        badge_url: None | str
        badge_url = self.badge_url

        badge_path: None | str
        badge_path = self.badge_path

        display_order: int | None
        display_order = self.display_order

        type_: None | str
        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ra_id": ra_id,
                "title": title,
                "description": description,
                "points": points,
                "num_awarded": num_awarded,
                "num_awarded_hardcore": num_awarded_hardcore,
                "badge_id": badge_id,
                "badge_url_lock": badge_url_lock,
                "badge_path_lock": badge_path_lock,
                "badge_url": badge_url,
                "badge_path": badge_path,
                "display_order": display_order,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ra_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ra_id = _parse_ra_id(d.pop("ra_id"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_points(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        points = _parse_points(d.pop("points"))

        def _parse_num_awarded(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        num_awarded = _parse_num_awarded(d.pop("num_awarded"))

        def _parse_num_awarded_hardcore(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        num_awarded_hardcore = _parse_num_awarded_hardcore(d.pop("num_awarded_hardcore"))

        def _parse_badge_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        badge_id = _parse_badge_id(d.pop("badge_id"))

        def _parse_badge_url_lock(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        badge_url_lock = _parse_badge_url_lock(d.pop("badge_url_lock"))

        def _parse_badge_path_lock(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        badge_path_lock = _parse_badge_path_lock(d.pop("badge_path_lock"))

        def _parse_badge_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        badge_url = _parse_badge_url(d.pop("badge_url"))

        def _parse_badge_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        badge_path = _parse_badge_path(d.pop("badge_path"))

        def _parse_display_order(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        display_order = _parse_display_order(d.pop("display_order"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        ra_game_rom_achievement = cls(
            ra_id=ra_id,
            title=title,
            description=description,
            points=points,
            num_awarded=num_awarded,
            num_awarded_hardcore=num_awarded_hardcore,
            badge_id=badge_id,
            badge_url_lock=badge_url_lock,
            badge_path_lock=badge_path_lock,
            badge_url=badge_url,
            badge_path=badge_path,
            display_order=display_order,
            type_=type_,
        )

        ra_game_rom_achievement.additional_properties = d
        return ra_game_rom_achievement

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
