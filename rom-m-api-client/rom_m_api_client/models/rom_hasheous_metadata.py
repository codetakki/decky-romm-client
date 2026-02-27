from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RomHasheousMetadata")


@_attrs_define
class RomHasheousMetadata:
    """
    Attributes:
        tosec_match (bool | Unset):
        mame_arcade_match (bool | Unset):
        mame_mess_match (bool | Unset):
        nointro_match (bool | Unset):
        redump_match (bool | Unset):
        whdload_match (bool | Unset):
        ra_match (bool | Unset):
        fbneo_match (bool | Unset):
        puredos_match (bool | Unset):
    """

    tosec_match: bool | Unset = UNSET
    mame_arcade_match: bool | Unset = UNSET
    mame_mess_match: bool | Unset = UNSET
    nointro_match: bool | Unset = UNSET
    redump_match: bool | Unset = UNSET
    whdload_match: bool | Unset = UNSET
    ra_match: bool | Unset = UNSET
    fbneo_match: bool | Unset = UNSET
    puredos_match: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tosec_match = self.tosec_match

        mame_arcade_match = self.mame_arcade_match

        mame_mess_match = self.mame_mess_match

        nointro_match = self.nointro_match

        redump_match = self.redump_match

        whdload_match = self.whdload_match

        ra_match = self.ra_match

        fbneo_match = self.fbneo_match

        puredos_match = self.puredos_match

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tosec_match is not UNSET:
            field_dict["tosec_match"] = tosec_match
        if mame_arcade_match is not UNSET:
            field_dict["mame_arcade_match"] = mame_arcade_match
        if mame_mess_match is not UNSET:
            field_dict["mame_mess_match"] = mame_mess_match
        if nointro_match is not UNSET:
            field_dict["nointro_match"] = nointro_match
        if redump_match is not UNSET:
            field_dict["redump_match"] = redump_match
        if whdload_match is not UNSET:
            field_dict["whdload_match"] = whdload_match
        if ra_match is not UNSET:
            field_dict["ra_match"] = ra_match
        if fbneo_match is not UNSET:
            field_dict["fbneo_match"] = fbneo_match
        if puredos_match is not UNSET:
            field_dict["puredos_match"] = puredos_match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tosec_match = d.pop("tosec_match", UNSET)

        mame_arcade_match = d.pop("mame_arcade_match", UNSET)

        mame_mess_match = d.pop("mame_mess_match", UNSET)

        nointro_match = d.pop("nointro_match", UNSET)

        redump_match = d.pop("redump_match", UNSET)

        whdload_match = d.pop("whdload_match", UNSET)

        ra_match = d.pop("ra_match", UNSET)

        fbneo_match = d.pop("fbneo_match", UNSET)

        puredos_match = d.pop("puredos_match", UNSET)

        rom_hasheous_metadata = cls(
            tosec_match=tosec_match,
            mame_arcade_match=mame_arcade_match,
            mame_mess_match=mame_mess_match,
            nointro_match=nointro_match,
            redump_match=redump_match,
            whdload_match=whdload_match,
            ra_match=ra_match,
            fbneo_match=fbneo_match,
            puredos_match=puredos_match,
        )

        rom_hasheous_metadata.additional_properties = d
        return rom_hasheous_metadata

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
