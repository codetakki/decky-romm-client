from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SiblingRomSchema")


@_attrs_define
class SiblingRomSchema:
    """
    Attributes:
        id (int):
        name (None | str):
        fs_name_no_tags (str):
        fs_name_no_ext (str):
        sort_comparator (str):
    """

    id: int
    name: None | str
    fs_name_no_tags: str
    fs_name_no_ext: str
    sort_comparator: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        fs_name_no_tags = self.fs_name_no_tags

        fs_name_no_ext = self.fs_name_no_ext

        sort_comparator = self.sort_comparator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "fs_name_no_tags": fs_name_no_tags,
                "fs_name_no_ext": fs_name_no_ext,
                "sort_comparator": sort_comparator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        fs_name_no_tags = d.pop("fs_name_no_tags")

        fs_name_no_ext = d.pop("fs_name_no_ext")

        sort_comparator = d.pop("sort_comparator")

        sibling_rom_schema = cls(
            id=id,
            name=name,
            fs_name_no_tags=fs_name_no_tags,
            fs_name_no_ext=fs_name_no_ext,
            sort_comparator=sort_comparator,
        )

        sibling_rom_schema.additional_properties = d
        return sibling_rom_schema

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
