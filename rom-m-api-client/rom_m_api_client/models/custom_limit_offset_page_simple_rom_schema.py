from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_limit_offset_page_simple_rom_schema_char_index import (
        CustomLimitOffsetPageSimpleRomSchemaCharIndex,
    )
    from ..models.rom_filters_dict import RomFiltersDict
    from ..models.simple_rom_schema import SimpleRomSchema


T = TypeVar("T", bound="CustomLimitOffsetPageSimpleRomSchema")


@_attrs_define
class CustomLimitOffsetPageSimpleRomSchema:
    """
    Attributes:
        items (list[SimpleRomSchema]):
        total (int):
        limit (int):
        offset (int):
        char_index (CustomLimitOffsetPageSimpleRomSchemaCharIndex):
        rom_id_index (list[int]):
        filter_values (RomFiltersDict):
    """

    items: list[SimpleRomSchema]
    total: int
    limit: int
    offset: int
    char_index: CustomLimitOffsetPageSimpleRomSchemaCharIndex
    rom_id_index: list[int]
    filter_values: RomFiltersDict
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total = self.total

        limit = self.limit

        offset = self.offset

        char_index = self.char_index.to_dict()

        rom_id_index = self.rom_id_index

        filter_values = self.filter_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "total": total,
                "limit": limit,
                "offset": offset,
                "char_index": char_index,
                "rom_id_index": rom_id_index,
                "filter_values": filter_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_limit_offset_page_simple_rom_schema_char_index import (
            CustomLimitOffsetPageSimpleRomSchemaCharIndex,
        )
        from ..models.rom_filters_dict import RomFiltersDict
        from ..models.simple_rom_schema import SimpleRomSchema

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = SimpleRomSchema.from_dict(items_item_data)

            items.append(items_item)

        total = d.pop("total")

        limit = d.pop("limit")

        offset = d.pop("offset")

        char_index = CustomLimitOffsetPageSimpleRomSchemaCharIndex.from_dict(d.pop("char_index"))

        rom_id_index = cast(list[int], d.pop("rom_id_index"))

        filter_values = RomFiltersDict.from_dict(d.pop("filter_values"))

        custom_limit_offset_page_simple_rom_schema = cls(
            items=items,
            total=total,
            limit=limit,
            offset=offset,
            char_index=char_index,
            rom_id_index=rom_id_index,
            filter_values=filter_values,
        )

        custom_limit_offset_page_simple_rom_schema.additional_properties = d
        return custom_limit_offset_page_simple_rom_schema

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
