from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.role import Role
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ra_progression import RAProgression
    from ..models.user_schema_ui_settings_type_0 import UserSchemaUiSettingsType0


T = TypeVar("T", bound="UserSchema")


@_attrs_define
class UserSchema:
    """
    Attributes:
        id (int):
        username (str):
        email (None | str):
        enabled (bool):
        role (Role):
        oauth_scopes (list[str]):
        avatar_path (str):
        last_login (datetime.datetime | None):
        last_active (datetime.datetime | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        ra_username (None | str | Unset):
        ra_progression (None | RAProgression | Unset):
        ui_settings (None | Unset | UserSchemaUiSettingsType0):
    """

    id: int
    username: str
    email: None | str
    enabled: bool
    role: Role
    oauth_scopes: list[str]
    avatar_path: str
    last_login: datetime.datetime | None
    last_active: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    ra_username: None | str | Unset = UNSET
    ra_progression: None | RAProgression | Unset = UNSET
    ui_settings: None | Unset | UserSchemaUiSettingsType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ra_progression import RAProgression
        from ..models.user_schema_ui_settings_type_0 import UserSchemaUiSettingsType0

        id = self.id

        username = self.username

        email: None | str
        email = self.email

        enabled = self.enabled

        role = self.role.value

        oauth_scopes = self.oauth_scopes

        avatar_path = self.avatar_path

        last_login: None | str
        if isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        last_active: None | str
        if isinstance(self.last_active, datetime.datetime):
            last_active = self.last_active.isoformat()
        else:
            last_active = self.last_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        ra_username: None | str | Unset
        if isinstance(self.ra_username, Unset):
            ra_username = UNSET
        else:
            ra_username = self.ra_username

        ra_progression: dict[str, Any] | None | Unset
        if isinstance(self.ra_progression, Unset):
            ra_progression = UNSET
        elif isinstance(self.ra_progression, RAProgression):
            ra_progression = self.ra_progression.to_dict()
        else:
            ra_progression = self.ra_progression

        ui_settings: dict[str, Any] | None | Unset
        if isinstance(self.ui_settings, Unset):
            ui_settings = UNSET
        elif isinstance(self.ui_settings, UserSchemaUiSettingsType0):
            ui_settings = self.ui_settings.to_dict()
        else:
            ui_settings = self.ui_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "email": email,
                "enabled": enabled,
                "role": role,
                "oauth_scopes": oauth_scopes,
                "avatar_path": avatar_path,
                "last_login": last_login,
                "last_active": last_active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if ra_username is not UNSET:
            field_dict["ra_username"] = ra_username
        if ra_progression is not UNSET:
            field_dict["ra_progression"] = ra_progression
        if ui_settings is not UNSET:
            field_dict["ui_settings"] = ui_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ra_progression import RAProgression
        from ..models.user_schema_ui_settings_type_0 import UserSchemaUiSettingsType0

        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        enabled = d.pop("enabled")

        role = Role(d.pop("role"))

        oauth_scopes = cast(list[str], d.pop("oauth_scopes"))

        avatar_path = d.pop("avatar_path")

        def _parse_last_login(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = isoparse(data)

                return last_login_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_login = _parse_last_login(d.pop("last_login"))

        def _parse_last_active(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_active_type_0 = isoparse(data)

                return last_active_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_active = _parse_last_active(d.pop("last_active"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_ra_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ra_username = _parse_ra_username(d.pop("ra_username", UNSET))

        def _parse_ra_progression(data: object) -> None | RAProgression | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ra_progression_type_0 = RAProgression.from_dict(data)

                return ra_progression_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RAProgression | Unset, data)

        ra_progression = _parse_ra_progression(d.pop("ra_progression", UNSET))

        def _parse_ui_settings(data: object) -> None | Unset | UserSchemaUiSettingsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ui_settings_type_0 = UserSchemaUiSettingsType0.from_dict(data)

                return ui_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserSchemaUiSettingsType0, data)

        ui_settings = _parse_ui_settings(d.pop("ui_settings", UNSET))

        user_schema = cls(
            id=id,
            username=username,
            email=email,
            enabled=enabled,
            role=role,
            oauth_scopes=oauth_scopes,
            avatar_path=avatar_path,
            last_login=last_login,
            last_active=last_active,
            created_at=created_at,
            updated_at=updated_at,
            ra_username=ra_username,
            ra_progression=ra_progression,
            ui_settings=ui_settings,
        )

        user_schema.additional_properties = d
        return user_schema

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
