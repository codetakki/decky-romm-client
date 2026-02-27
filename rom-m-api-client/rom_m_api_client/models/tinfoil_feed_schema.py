from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tinfoil_feed_file_schema import TinfoilFeedFileSchema
    from ..models.tinfoil_feed_schema_titledb import TinfoilFeedSchemaTitledb


T = TypeVar("T", bound="TinfoilFeedSchema")


@_attrs_define
class TinfoilFeedSchema:
    """
    Attributes:
        files (list[TinfoilFeedFileSchema]):
        directories (list[str]):
        titledb (TinfoilFeedSchemaTitledb | Unset):
        success (str | Unset):
        error (str | Unset):
    """

    files: list[TinfoilFeedFileSchema]
    directories: list[str]
    titledb: TinfoilFeedSchemaTitledb | Unset = UNSET
    success: str | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        directories = self.directories

        titledb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.titledb, Unset):
            titledb = self.titledb.to_dict()

        success = self.success

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "directories": directories,
            }
        )
        if titledb is not UNSET:
            field_dict["titledb"] = titledb
        if success is not UNSET:
            field_dict["success"] = success
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tinfoil_feed_file_schema import TinfoilFeedFileSchema
        from ..models.tinfoil_feed_schema_titledb import TinfoilFeedSchemaTitledb

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = TinfoilFeedFileSchema.from_dict(files_item_data)

            files.append(files_item)

        directories = cast(list[str], d.pop("directories"))

        _titledb = d.pop("titledb", UNSET)
        titledb: TinfoilFeedSchemaTitledb | Unset
        if isinstance(_titledb, Unset):
            titledb = UNSET
        else:
            titledb = TinfoilFeedSchemaTitledb.from_dict(_titledb)

        success = d.pop("success", UNSET)

        error = d.pop("error", UNSET)

        tinfoil_feed_schema = cls(
            files=files,
            directories=directories,
            titledb=titledb,
            success=success,
            error=error,
        )

        tinfoil_feed_schema.additional_properties = d
        return tinfoil_feed_schema

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
