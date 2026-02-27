from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyUpdateRomApiRomsIdPut")


@_attrs_define
class BodyUpdateRomApiRomsIdPut:
    """
    Attributes:
        artwork (File | None | Unset): Custom artwork to set as cover.
    """

    artwork: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artwork: FileTypes | None | Unset
        if isinstance(self.artwork, Unset):
            artwork = UNSET
        elif isinstance(self.artwork, File):
            artwork = self.artwork.to_tuple()

        else:
            artwork = self.artwork

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artwork is not UNSET:
            field_dict["artwork"] = artwork

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.artwork, Unset):
            if isinstance(self.artwork, File):
                files.append(("artwork", self.artwork.to_tuple()))
            else:
                files.append(("artwork", (None, str(self.artwork).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_artwork(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                artwork_type_0 = File(payload=BytesIO(data))

                return artwork_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        artwork = _parse_artwork(d.pop("artwork", UNSET))

        body_update_rom_api_roms_id_put = cls(
            artwork=artwork,
        )

        body_update_rom_api_roms_id_put.additional_properties = d
        return body_update_rom_api_roms_id_put

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
