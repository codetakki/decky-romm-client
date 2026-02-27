from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.screenshot_schema import ScreenshotSchema


T = TypeVar("T", bound="SaveSchema")


@_attrs_define
class SaveSchema:
    """
    Attributes:
        id (int):
        rom_id (int):
        user_id (int):
        file_name (str):
        file_name_no_tags (str):
        file_name_no_ext (str):
        file_extension (str):
        file_path (str):
        file_size_bytes (int):
        full_path (str):
        download_path (str):
        missing_from_fs (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        emulator (None | str):
        screenshot (None | ScreenshotSchema):
    """

    id: int
    rom_id: int
    user_id: int
    file_name: str
    file_name_no_tags: str
    file_name_no_ext: str
    file_extension: str
    file_path: str
    file_size_bytes: int
    full_path: str
    download_path: str
    missing_from_fs: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    emulator: None | str
    screenshot: None | ScreenshotSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.screenshot_schema import ScreenshotSchema

        id = self.id

        rom_id = self.rom_id

        user_id = self.user_id

        file_name = self.file_name

        file_name_no_tags = self.file_name_no_tags

        file_name_no_ext = self.file_name_no_ext

        file_extension = self.file_extension

        file_path = self.file_path

        file_size_bytes = self.file_size_bytes

        full_path = self.full_path

        download_path = self.download_path

        missing_from_fs = self.missing_from_fs

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        emulator: None | str
        emulator = self.emulator

        screenshot: dict[str, Any] | None
        if isinstance(self.screenshot, ScreenshotSchema):
            screenshot = self.screenshot.to_dict()
        else:
            screenshot = self.screenshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rom_id": rom_id,
                "user_id": user_id,
                "file_name": file_name,
                "file_name_no_tags": file_name_no_tags,
                "file_name_no_ext": file_name_no_ext,
                "file_extension": file_extension,
                "file_path": file_path,
                "file_size_bytes": file_size_bytes,
                "full_path": full_path,
                "download_path": download_path,
                "missing_from_fs": missing_from_fs,
                "created_at": created_at,
                "updated_at": updated_at,
                "emulator": emulator,
                "screenshot": screenshot,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.screenshot_schema import ScreenshotSchema

        d = dict(src_dict)
        id = d.pop("id")

        rom_id = d.pop("rom_id")

        user_id = d.pop("user_id")

        file_name = d.pop("file_name")

        file_name_no_tags = d.pop("file_name_no_tags")

        file_name_no_ext = d.pop("file_name_no_ext")

        file_extension = d.pop("file_extension")

        file_path = d.pop("file_path")

        file_size_bytes = d.pop("file_size_bytes")

        full_path = d.pop("full_path")

        download_path = d.pop("download_path")

        missing_from_fs = d.pop("missing_from_fs")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_emulator(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        emulator = _parse_emulator(d.pop("emulator"))

        def _parse_screenshot(data: object) -> None | ScreenshotSchema:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                screenshot_type_0 = ScreenshotSchema.from_dict(data)

                return screenshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScreenshotSchema, data)

        screenshot = _parse_screenshot(d.pop("screenshot"))

        save_schema = cls(
            id=id,
            rom_id=rom_id,
            user_id=user_id,
            file_name=file_name,
            file_name_no_tags=file_name_no_tags,
            file_name_no_ext=file_name_no_ext,
            file_extension=file_extension,
            file_path=file_path,
            file_size_bytes=file_size_bytes,
            full_path=full_path,
            download_path=download_path,
            missing_from_fs=missing_from_fs,
            created_at=created_at,
            updated_at=updated_at,
            emulator=emulator,
            screenshot=screenshot,
        )

        save_schema.additional_properties = d
        return save_schema

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
