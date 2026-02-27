from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.igdb_metadata_platform import IGDBMetadataPlatform


T = TypeVar("T", bound="IGDBMetadataMultiplayerMode")


@_attrs_define
class IGDBMetadataMultiplayerMode:
    """
    Attributes:
        campaigncoop (bool):
        dropin (bool):
        lancoop (bool):
        offlinecoop (bool):
        offlinecoopmax (int):
        offlinemax (int):
        onlinecoop (int):
        onlinecoopmax (int):
        onlinemax (int):
        splitscreen (bool):
        splitscreenonline (bool):
        platform (IGDBMetadataPlatform):
    """

    campaigncoop: bool
    dropin: bool
    lancoop: bool
    offlinecoop: bool
    offlinecoopmax: int
    offlinemax: int
    onlinecoop: int
    onlinecoopmax: int
    onlinemax: int
    splitscreen: bool
    splitscreenonline: bool
    platform: IGDBMetadataPlatform
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaigncoop = self.campaigncoop

        dropin = self.dropin

        lancoop = self.lancoop

        offlinecoop = self.offlinecoop

        offlinecoopmax = self.offlinecoopmax

        offlinemax = self.offlinemax

        onlinecoop = self.onlinecoop

        onlinecoopmax = self.onlinecoopmax

        onlinemax = self.onlinemax

        splitscreen = self.splitscreen

        splitscreenonline = self.splitscreenonline

        platform = self.platform.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaigncoop": campaigncoop,
                "dropin": dropin,
                "lancoop": lancoop,
                "offlinecoop": offlinecoop,
                "offlinecoopmax": offlinecoopmax,
                "offlinemax": offlinemax,
                "onlinecoop": onlinecoop,
                "onlinecoopmax": onlinecoopmax,
                "onlinemax": onlinemax,
                "splitscreen": splitscreen,
                "splitscreenonline": splitscreenonline,
                "platform": platform,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.igdb_metadata_platform import IGDBMetadataPlatform

        d = dict(src_dict)
        campaigncoop = d.pop("campaigncoop")

        dropin = d.pop("dropin")

        lancoop = d.pop("lancoop")

        offlinecoop = d.pop("offlinecoop")

        offlinecoopmax = d.pop("offlinecoopmax")

        offlinemax = d.pop("offlinemax")

        onlinecoop = d.pop("onlinecoop")

        onlinecoopmax = d.pop("onlinecoopmax")

        onlinemax = d.pop("onlinemax")

        splitscreen = d.pop("splitscreen")

        splitscreenonline = d.pop("splitscreenonline")

        platform = IGDBMetadataPlatform.from_dict(d.pop("platform"))

        igdb_metadata_multiplayer_mode = cls(
            campaigncoop=campaigncoop,
            dropin=dropin,
            lancoop=lancoop,
            offlinecoop=offlinecoop,
            offlinecoopmax=offlinecoopmax,
            offlinemax=offlinemax,
            onlinecoop=onlinecoop,
            onlinecoopmax=onlinecoopmax,
            onlinemax=onlinemax,
            splitscreen=splitscreen,
            splitscreenonline=splitscreenonline,
            platform=platform,
        )

        igdb_metadata_multiplayer_mode.additional_properties = d
        return igdb_metadata_multiplayer_mode

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
