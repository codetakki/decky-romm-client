from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TasksDict")


@_attrs_define
class TasksDict:
    """
    Attributes:
        enable_scheduled_rescan (bool):
        scheduled_rescan_cron (str):
        enable_scheduled_update_switch_titledb (bool):
        scheduled_update_switch_titledb_cron (str):
        enable_scheduled_update_launchbox_metadata (bool):
        scheduled_update_launchbox_metadata_cron (str):
        enable_scheduled_convert_images_to_webp (bool):
        scheduled_convert_images_to_webp_cron (str):
    """

    enable_scheduled_rescan: bool
    scheduled_rescan_cron: str
    enable_scheduled_update_switch_titledb: bool
    scheduled_update_switch_titledb_cron: str
    enable_scheduled_update_launchbox_metadata: bool
    scheduled_update_launchbox_metadata_cron: str
    enable_scheduled_convert_images_to_webp: bool
    scheduled_convert_images_to_webp_cron: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_scheduled_rescan = self.enable_scheduled_rescan

        scheduled_rescan_cron = self.scheduled_rescan_cron

        enable_scheduled_update_switch_titledb = self.enable_scheduled_update_switch_titledb

        scheduled_update_switch_titledb_cron = self.scheduled_update_switch_titledb_cron

        enable_scheduled_update_launchbox_metadata = self.enable_scheduled_update_launchbox_metadata

        scheduled_update_launchbox_metadata_cron = self.scheduled_update_launchbox_metadata_cron

        enable_scheduled_convert_images_to_webp = self.enable_scheduled_convert_images_to_webp

        scheduled_convert_images_to_webp_cron = self.scheduled_convert_images_to_webp_cron

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ENABLE_SCHEDULED_RESCAN": enable_scheduled_rescan,
                "SCHEDULED_RESCAN_CRON": scheduled_rescan_cron,
                "ENABLE_SCHEDULED_UPDATE_SWITCH_TITLEDB": enable_scheduled_update_switch_titledb,
                "SCHEDULED_UPDATE_SWITCH_TITLEDB_CRON": scheduled_update_switch_titledb_cron,
                "ENABLE_SCHEDULED_UPDATE_LAUNCHBOX_METADATA": enable_scheduled_update_launchbox_metadata,
                "SCHEDULED_UPDATE_LAUNCHBOX_METADATA_CRON": scheduled_update_launchbox_metadata_cron,
                "ENABLE_SCHEDULED_CONVERT_IMAGES_TO_WEBP": enable_scheduled_convert_images_to_webp,
                "SCHEDULED_CONVERT_IMAGES_TO_WEBP_CRON": scheduled_convert_images_to_webp_cron,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_scheduled_rescan = d.pop("ENABLE_SCHEDULED_RESCAN")

        scheduled_rescan_cron = d.pop("SCHEDULED_RESCAN_CRON")

        enable_scheduled_update_switch_titledb = d.pop("ENABLE_SCHEDULED_UPDATE_SWITCH_TITLEDB")

        scheduled_update_switch_titledb_cron = d.pop("SCHEDULED_UPDATE_SWITCH_TITLEDB_CRON")

        enable_scheduled_update_launchbox_metadata = d.pop("ENABLE_SCHEDULED_UPDATE_LAUNCHBOX_METADATA")

        scheduled_update_launchbox_metadata_cron = d.pop("SCHEDULED_UPDATE_LAUNCHBOX_METADATA_CRON")

        enable_scheduled_convert_images_to_webp = d.pop("ENABLE_SCHEDULED_CONVERT_IMAGES_TO_WEBP")

        scheduled_convert_images_to_webp_cron = d.pop("SCHEDULED_CONVERT_IMAGES_TO_WEBP_CRON")

        tasks_dict = cls(
            enable_scheduled_rescan=enable_scheduled_rescan,
            scheduled_rescan_cron=scheduled_rescan_cron,
            enable_scheduled_update_switch_titledb=enable_scheduled_update_switch_titledb,
            scheduled_update_switch_titledb_cron=scheduled_update_switch_titledb_cron,
            enable_scheduled_update_launchbox_metadata=enable_scheduled_update_launchbox_metadata,
            scheduled_update_launchbox_metadata_cron=scheduled_update_launchbox_metadata_cron,
            enable_scheduled_convert_images_to_webp=enable_scheduled_convert_images_to_webp,
            scheduled_convert_images_to_webp_cron=scheduled_convert_images_to_webp_cron,
        )

        tasks_dict.additional_properties = d
        return tasks_dict

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
