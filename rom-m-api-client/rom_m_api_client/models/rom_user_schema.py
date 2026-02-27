from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rom_user_status import RomUserStatus

T = TypeVar("T", bound="RomUserSchema")


@_attrs_define
class RomUserSchema:
    """
    Attributes:
        id (int):
        user_id (int):
        rom_id (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_played (datetime.datetime | None):
        is_main_sibling (bool):
        backlogged (bool):
        now_playing (bool):
        hidden (bool):
        rating (int):
        difficulty (int):
        completion (int):
        status (None | RomUserStatus):
        user_username (str):
    """

    id: int
    user_id: int
    rom_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_played: datetime.datetime | None
    is_main_sibling: bool
    backlogged: bool
    now_playing: bool
    hidden: bool
    rating: int
    difficulty: int
    completion: int
    status: None | RomUserStatus
    user_username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        rom_id = self.rom_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_played: None | str
        if isinstance(self.last_played, datetime.datetime):
            last_played = self.last_played.isoformat()
        else:
            last_played = self.last_played

        is_main_sibling = self.is_main_sibling

        backlogged = self.backlogged

        now_playing = self.now_playing

        hidden = self.hidden

        rating = self.rating

        difficulty = self.difficulty

        completion = self.completion

        status: None | str
        if isinstance(self.status, RomUserStatus):
            status = self.status.value
        else:
            status = self.status

        user_username = self.user_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "rom_id": rom_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_played": last_played,
                "is_main_sibling": is_main_sibling,
                "backlogged": backlogged,
                "now_playing": now_playing,
                "hidden": hidden,
                "rating": rating,
                "difficulty": difficulty,
                "completion": completion,
                "status": status,
                "user__username": user_username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        rom_id = d.pop("rom_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_last_played(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_played_type_0 = isoparse(data)

                return last_played_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_played = _parse_last_played(d.pop("last_played"))

        is_main_sibling = d.pop("is_main_sibling")

        backlogged = d.pop("backlogged")

        now_playing = d.pop("now_playing")

        hidden = d.pop("hidden")

        rating = d.pop("rating")

        difficulty = d.pop("difficulty")

        completion = d.pop("completion")

        def _parse_status(data: object) -> None | RomUserStatus:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = RomUserStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomUserStatus, data)

        status = _parse_status(d.pop("status"))

        user_username = d.pop("user__username")

        rom_user_schema = cls(
            id=id,
            user_id=user_id,
            rom_id=rom_id,
            created_at=created_at,
            updated_at=updated_at,
            last_played=last_played,
            is_main_sibling=is_main_sibling,
            backlogged=backlogged,
            now_playing=now_playing,
            hidden=hidden,
            rating=rating,
            difficulty=difficulty,
            completion=completion,
            status=status,
            user_username=user_username,
        )

        rom_user_schema.additional_properties = d
        return rom_user_schema

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
