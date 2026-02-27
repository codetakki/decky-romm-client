from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.firmware_schema import FirmwareSchema


T = TypeVar("T", bound="AddFirmwareResponse")


@_attrs_define
class AddFirmwareResponse:
    """
    Attributes:
        uploaded (int):
        firmware (list[FirmwareSchema]):
    """

    uploaded: int
    firmware: list[FirmwareSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uploaded = self.uploaded

        firmware = []
        for firmware_item_data in self.firmware:
            firmware_item = firmware_item_data.to_dict()
            firmware.append(firmware_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploaded": uploaded,
                "firmware": firmware,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firmware_schema import FirmwareSchema

        d = dict(src_dict)
        uploaded = d.pop("uploaded")

        firmware = []
        _firmware = d.pop("firmware")
        for firmware_item_data in _firmware:
            firmware_item = FirmwareSchema.from_dict(firmware_item_data)

            firmware.append(firmware_item)

        add_firmware_response = cls(
            uploaded=uploaded,
            firmware=firmware,
        )

        add_firmware_response.additional_properties = d
        return add_firmware_response

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
