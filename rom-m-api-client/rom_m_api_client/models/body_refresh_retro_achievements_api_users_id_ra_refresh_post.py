from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyRefreshRetroAchievementsApiUsersIdRaRefreshPost")


@_attrs_define
class BodyRefreshRetroAchievementsApiUsersIdRaRefreshPost:
    """
    Attributes:
        incremental (bool | Unset): Whether to only retrieve RetroAchievements progression incrementally. Default:
            False.
    """

    incremental: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incremental = self.incremental

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incremental is not UNSET:
            field_dict["incremental"] = incremental

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incremental = d.pop("incremental", UNSET)

        body_refresh_retro_achievements_api_users_id_ra_refresh_post = cls(
            incremental=incremental,
        )

        body_refresh_retro_achievements_api_users_id_ra_refresh_post.additional_properties = d
        return body_refresh_retro_achievements_api_users_id_ra_refresh_post

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
