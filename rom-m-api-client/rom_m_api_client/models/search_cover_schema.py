from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sgdb_resource import SGDBResource


T = TypeVar("T", bound="SearchCoverSchema")


@_attrs_define
class SearchCoverSchema:
    """
    Attributes:
        name (str):
        resources (list[SGDBResource]):
    """

    name: str
    resources: list[SGDBResource]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sgdb_resource import SGDBResource

        d = dict(src_dict)
        name = d.pop("name")

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = SGDBResource.from_dict(resources_item_data)

            resources.append(resources_item)

        search_cover_schema = cls(
            name=name,
            resources=resources,
        )

        search_cover_schema.additional_properties = d
        return search_cover_schema

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
