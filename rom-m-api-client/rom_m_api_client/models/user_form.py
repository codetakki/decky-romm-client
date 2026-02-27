from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="UserForm")


@_attrs_define
class UserForm:
    """
    Attributes:
        username (None | str | Unset):
        password (None | str | Unset):
        email (None | str | Unset):
        role (None | str | Unset):
        enabled (bool | None | Unset):
        ra_username (None | str | Unset):
        avatar (File | None | Unset):
        ui_settings (None | str | Unset):
    """

    username: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    ra_username: None | str | Unset = UNSET
    avatar: File | None | Unset = UNSET
    ui_settings: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        ra_username: None | str | Unset
        if isinstance(self.ra_username, Unset):
            ra_username = UNSET
        else:
            ra_username = self.ra_username

        avatar: FileTypes | None | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        elif isinstance(self.avatar, File):
            avatar = self.avatar.to_tuple()

        else:
            avatar = self.avatar

        ui_settings: None | str | Unset
        if isinstance(self.ui_settings, Unset):
            ui_settings = UNSET
        else:
            ui_settings = self.ui_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if role is not UNSET:
            field_dict["role"] = role
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if ra_username is not UNSET:
            field_dict["ra_username"] = ra_username
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if ui_settings is not UNSET:
            field_dict["ui_settings"] = ui_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_ra_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ra_username = _parse_ra_username(d.pop("ra_username", UNSET))

        def _parse_avatar(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                avatar_type_0 = File(payload=BytesIO(data))

                return avatar_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        def _parse_ui_settings(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ui_settings = _parse_ui_settings(d.pop("ui_settings", UNSET))

        user_form = cls(
            username=username,
            password=password,
            email=email,
            role=role,
            enabled=enabled,
            ra_username=ra_username,
            avatar=avatar,
            ui_settings=ui_settings,
        )

        user_form.additional_properties = d
        return user_form

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
