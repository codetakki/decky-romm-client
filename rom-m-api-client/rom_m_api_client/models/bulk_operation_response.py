from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkOperationResponse")


@_attrs_define
class BulkOperationResponse:
    """
    Attributes:
        successful_items (int):
        failed_items (int):
        errors (list[str]):
    """

    successful_items: int
    failed_items: int
    errors: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        successful_items = self.successful_items

        failed_items = self.failed_items

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "successful_items": successful_items,
                "failed_items": failed_items,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        successful_items = d.pop("successful_items")

        failed_items = d.pop("failed_items")

        errors = cast(list[str], d.pop("errors"))

        bulk_operation_response = cls(
            successful_items=successful_items,
            failed_items=failed_items,
            errors=errors,
        )

        bulk_operation_response.additional_properties = d
        return bulk_operation_response

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
