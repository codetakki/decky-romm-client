from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyDeleteRomsApiRomsDeletePost")


@_attrs_define
class BodyDeleteRomsApiRomsDeletePost:
    """
    Attributes:
        roms (list[int]): List of rom ids to delete from database.
        delete_from_fs (list[int] | Unset): List of rom ids to delete from filesystem.
    """

    roms: list[int]
    delete_from_fs: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roms = self.roms

        delete_from_fs: list[int] | Unset = UNSET
        if not isinstance(self.delete_from_fs, Unset):
            delete_from_fs = self.delete_from_fs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roms": roms,
            }
        )
        if delete_from_fs is not UNSET:
            field_dict["delete_from_fs"] = delete_from_fs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        roms = cast(list[int], d.pop("roms"))

        delete_from_fs = cast(list[int], d.pop("delete_from_fs", UNSET))

        body_delete_roms_api_roms_delete_post = cls(
            roms=roms,
            delete_from_fs=delete_from_fs,
        )

        body_delete_roms_api_roms_delete_post.additional_properties = d
        return body_delete_roms_api_roms_delete_post

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
