from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MetadataSourcesDict")


@_attrs_define
class MetadataSourcesDict:
    """
    Attributes:
        any_source_enabled (bool):
        igdb_api_enabled (bool):
        ss_api_enabled (bool):
        moby_api_enabled (bool):
        steamgriddb_api_enabled (bool):
        ra_api_enabled (bool):
        launchbox_api_enabled (bool):
        hasheous_api_enabled (bool):
        playmatch_api_enabled (bool):
        tgdb_api_enabled (bool):
        flashpoint_api_enabled (bool):
        hltb_api_enabled (bool):
    """

    any_source_enabled: bool
    igdb_api_enabled: bool
    ss_api_enabled: bool
    moby_api_enabled: bool
    steamgriddb_api_enabled: bool
    ra_api_enabled: bool
    launchbox_api_enabled: bool
    hasheous_api_enabled: bool
    playmatch_api_enabled: bool
    tgdb_api_enabled: bool
    flashpoint_api_enabled: bool
    hltb_api_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        any_source_enabled = self.any_source_enabled

        igdb_api_enabled = self.igdb_api_enabled

        ss_api_enabled = self.ss_api_enabled

        moby_api_enabled = self.moby_api_enabled

        steamgriddb_api_enabled = self.steamgriddb_api_enabled

        ra_api_enabled = self.ra_api_enabled

        launchbox_api_enabled = self.launchbox_api_enabled

        hasheous_api_enabled = self.hasheous_api_enabled

        playmatch_api_enabled = self.playmatch_api_enabled

        tgdb_api_enabled = self.tgdb_api_enabled

        flashpoint_api_enabled = self.flashpoint_api_enabled

        hltb_api_enabled = self.hltb_api_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ANY_SOURCE_ENABLED": any_source_enabled,
                "IGDB_API_ENABLED": igdb_api_enabled,
                "SS_API_ENABLED": ss_api_enabled,
                "MOBY_API_ENABLED": moby_api_enabled,
                "STEAMGRIDDB_API_ENABLED": steamgriddb_api_enabled,
                "RA_API_ENABLED": ra_api_enabled,
                "LAUNCHBOX_API_ENABLED": launchbox_api_enabled,
                "HASHEOUS_API_ENABLED": hasheous_api_enabled,
                "PLAYMATCH_API_ENABLED": playmatch_api_enabled,
                "TGDB_API_ENABLED": tgdb_api_enabled,
                "FLASHPOINT_API_ENABLED": flashpoint_api_enabled,
                "HLTB_API_ENABLED": hltb_api_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        any_source_enabled = d.pop("ANY_SOURCE_ENABLED")

        igdb_api_enabled = d.pop("IGDB_API_ENABLED")

        ss_api_enabled = d.pop("SS_API_ENABLED")

        moby_api_enabled = d.pop("MOBY_API_ENABLED")

        steamgriddb_api_enabled = d.pop("STEAMGRIDDB_API_ENABLED")

        ra_api_enabled = d.pop("RA_API_ENABLED")

        launchbox_api_enabled = d.pop("LAUNCHBOX_API_ENABLED")

        hasheous_api_enabled = d.pop("HASHEOUS_API_ENABLED")

        playmatch_api_enabled = d.pop("PLAYMATCH_API_ENABLED")

        tgdb_api_enabled = d.pop("TGDB_API_ENABLED")

        flashpoint_api_enabled = d.pop("FLASHPOINT_API_ENABLED")

        hltb_api_enabled = d.pop("HLTB_API_ENABLED")

        metadata_sources_dict = cls(
            any_source_enabled=any_source_enabled,
            igdb_api_enabled=igdb_api_enabled,
            ss_api_enabled=ss_api_enabled,
            moby_api_enabled=moby_api_enabled,
            steamgriddb_api_enabled=steamgriddb_api_enabled,
            ra_api_enabled=ra_api_enabled,
            launchbox_api_enabled=launchbox_api_enabled,
            hasheous_api_enabled=hasheous_api_enabled,
            playmatch_api_enabled=playmatch_api_enabled,
            tgdb_api_enabled=tgdb_api_enabled,
            flashpoint_api_enabled=flashpoint_api_enabled,
            hltb_api_enabled=hltb_api_enabled,
        )

        metadata_sources_dict.additional_properties = d
        return metadata_sources_dict

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
