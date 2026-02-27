from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.emulation_dict import EmulationDict
    from ..models.filesystem_dict import FilesystemDict
    from ..models.frontend_dict import FrontendDict
    from ..models.metadata_sources_dict import MetadataSourcesDict
    from ..models.oidc_dict import OIDCDict
    from ..models.system_dict import SystemDict
    from ..models.tasks_dict import TasksDict


T = TypeVar("T", bound="HeartbeatResponse")


@_attrs_define
class HeartbeatResponse:
    """
    Attributes:
        system (SystemDict):
        metadata_sources (MetadataSourcesDict):
        filesystem (FilesystemDict):
        emulation (EmulationDict):
        frontend (FrontendDict):
        oidc (OIDCDict):
        tasks (TasksDict):
    """

    system: SystemDict
    metadata_sources: MetadataSourcesDict
    filesystem: FilesystemDict
    emulation: EmulationDict
    frontend: FrontendDict
    oidc: OIDCDict
    tasks: TasksDict
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system = self.system.to_dict()

        metadata_sources = self.metadata_sources.to_dict()

        filesystem = self.filesystem.to_dict()

        emulation = self.emulation.to_dict()

        frontend = self.frontend.to_dict()

        oidc = self.oidc.to_dict()

        tasks = self.tasks.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SYSTEM": system,
                "METADATA_SOURCES": metadata_sources,
                "FILESYSTEM": filesystem,
                "EMULATION": emulation,
                "FRONTEND": frontend,
                "OIDC": oidc,
                "TASKS": tasks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.emulation_dict import EmulationDict
        from ..models.filesystem_dict import FilesystemDict
        from ..models.frontend_dict import FrontendDict
        from ..models.metadata_sources_dict import MetadataSourcesDict
        from ..models.oidc_dict import OIDCDict
        from ..models.system_dict import SystemDict
        from ..models.tasks_dict import TasksDict

        d = dict(src_dict)
        system = SystemDict.from_dict(d.pop("SYSTEM"))

        metadata_sources = MetadataSourcesDict.from_dict(d.pop("METADATA_SOURCES"))

        filesystem = FilesystemDict.from_dict(d.pop("FILESYSTEM"))

        emulation = EmulationDict.from_dict(d.pop("EMULATION"))

        frontend = FrontendDict.from_dict(d.pop("FRONTEND"))

        oidc = OIDCDict.from_dict(d.pop("OIDC"))

        tasks = TasksDict.from_dict(d.pop("TASKS"))

        heartbeat_response = cls(
            system=system,
            metadata_sources=metadata_sources,
            filesystem=filesystem,
            emulation=emulation,
            frontend=frontend,
            oidc=oidc,
            tasks=tasks,
        )

        heartbeat_response.additional_properties = d
        return heartbeat_response

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
