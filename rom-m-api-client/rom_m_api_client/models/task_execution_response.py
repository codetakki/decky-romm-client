from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_status import JobStatus

T = TypeVar("T", bound="TaskExecutionResponse")


@_attrs_define
class TaskExecutionResponse:
    """
    Attributes:
        task_name (str):
        task_id (str):
        status (JobStatus): The Status of Job within its lifecycle at any given time.
        created_at (None | str):
        enqueued_at (None | str):
    """

    task_name: str
    task_id: str
    status: JobStatus
    created_at: None | str
    enqueued_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_name = self.task_name

        task_id = self.task_id

        status = self.status.value

        created_at: None | str
        created_at = self.created_at

        enqueued_at: None | str
        enqueued_at = self.enqueued_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_name": task_name,
                "task_id": task_id,
                "status": status,
                "created_at": created_at,
                "enqueued_at": enqueued_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_name = d.pop("task_name")

        task_id = d.pop("task_id")

        status = JobStatus(d.pop("status"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))

        def _parse_enqueued_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        enqueued_at = _parse_enqueued_at(d.pop("enqueued_at"))

        task_execution_response = cls(
            task_name=task_name,
            task_id=task_id,
            status=status,
            created_at=created_at,
            enqueued_at=enqueued_at,
        )

        task_execution_response.additional_properties = d
        return task_execution_response

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
