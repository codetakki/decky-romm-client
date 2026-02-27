from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_type import TaskType

T = TypeVar("T", bound="TaskInfo")


@_attrs_define
class TaskInfo:
    """
    Attributes:
        name (str):
        type_ (TaskType): Enumeration of task types for categorization and UI display.
        manual_run (bool):
        title (str):
        description (str):
        enabled (bool):
        cron_string (str):
    """

    name: str
    type_: TaskType
    manual_run: bool
    title: str
    description: str
    enabled: bool
    cron_string: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        manual_run = self.manual_run

        title = self.title

        description = self.description

        enabled = self.enabled

        cron_string = self.cron_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "manual_run": manual_run,
                "title": title,
                "description": description,
                "enabled": enabled,
                "cron_string": cron_string,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = TaskType(d.pop("type"))

        manual_run = d.pop("manual_run")

        title = d.pop("title")

        description = d.pop("description")

        enabled = d.pop("enabled")

        cron_string = d.pop("cron_string")

        task_info = cls(
            name=name,
            type_=type_,
            manual_run=manual_run,
            title=title,
            description=description,
            enabled=enabled,
            cron_string=cron_string,
        )

        task_info.additional_properties = d
        return task_info

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
