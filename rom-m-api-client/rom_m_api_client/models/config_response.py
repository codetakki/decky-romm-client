from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.config_response_ejs_controls import ConfigResponseEjsControls
    from ..models.config_response_ejs_settings import ConfigResponseEjsSettings
    from ..models.config_response_platforms_binding import ConfigResponsePlatformsBinding
    from ..models.config_response_platforms_versions import ConfigResponsePlatformsVersions
    from ..models.netplay_ice_server import NetplayICEServer


T = TypeVar("T", bound="ConfigResponse")


@_attrs_define
class ConfigResponse:
    """
    Attributes:
        config_file_mounted (bool):
        config_file_writable (bool):
        excluded_platforms (list[str]):
        excluded_single_ext (list[str]):
        excluded_single_files (list[str]):
        excluded_multi_files (list[str]):
        excluded_multi_parts_ext (list[str]):
        excluded_multi_parts_files (list[str]):
        platforms_binding (ConfigResponsePlatformsBinding):
        platforms_versions (ConfigResponsePlatformsVersions):
        skip_hash_calculation (bool):
        ejs_debug (bool):
        ejs_cache_limit (int | None):
        ejs_disable_auto_unload (bool):
        ejs_disable_batch_bootup (bool):
        ejs_netplay_enabled (bool):
        ejs_netplay_ice_servers (list[NetplayICEServer]):
        ejs_settings (ConfigResponseEjsSettings):
        ejs_controls (ConfigResponseEjsControls):
        scan_metadata_priority (list[str]):
        scan_artwork_priority (list[str]):
        scan_region_priority (list[str]):
        scan_language_priority (list[str]):
        scan_media (list[str]):
    """

    config_file_mounted: bool
    config_file_writable: bool
    excluded_platforms: list[str]
    excluded_single_ext: list[str]
    excluded_single_files: list[str]
    excluded_multi_files: list[str]
    excluded_multi_parts_ext: list[str]
    excluded_multi_parts_files: list[str]
    platforms_binding: ConfigResponsePlatformsBinding
    platforms_versions: ConfigResponsePlatformsVersions
    skip_hash_calculation: bool
    ejs_debug: bool
    ejs_cache_limit: int | None
    ejs_disable_auto_unload: bool
    ejs_disable_batch_bootup: bool
    ejs_netplay_enabled: bool
    ejs_netplay_ice_servers: list[NetplayICEServer]
    ejs_settings: ConfigResponseEjsSettings
    ejs_controls: ConfigResponseEjsControls
    scan_metadata_priority: list[str]
    scan_artwork_priority: list[str]
    scan_region_priority: list[str]
    scan_language_priority: list[str]
    scan_media: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_file_mounted = self.config_file_mounted

        config_file_writable = self.config_file_writable

        excluded_platforms = self.excluded_platforms

        excluded_single_ext = self.excluded_single_ext

        excluded_single_files = self.excluded_single_files

        excluded_multi_files = self.excluded_multi_files

        excluded_multi_parts_ext = self.excluded_multi_parts_ext

        excluded_multi_parts_files = self.excluded_multi_parts_files

        platforms_binding = self.platforms_binding.to_dict()

        platforms_versions = self.platforms_versions.to_dict()

        skip_hash_calculation = self.skip_hash_calculation

        ejs_debug = self.ejs_debug

        ejs_cache_limit: int | None
        ejs_cache_limit = self.ejs_cache_limit

        ejs_disable_auto_unload = self.ejs_disable_auto_unload

        ejs_disable_batch_bootup = self.ejs_disable_batch_bootup

        ejs_netplay_enabled = self.ejs_netplay_enabled

        ejs_netplay_ice_servers = []
        for ejs_netplay_ice_servers_item_data in self.ejs_netplay_ice_servers:
            ejs_netplay_ice_servers_item = ejs_netplay_ice_servers_item_data.to_dict()
            ejs_netplay_ice_servers.append(ejs_netplay_ice_servers_item)

        ejs_settings = self.ejs_settings.to_dict()

        ejs_controls = self.ejs_controls.to_dict()

        scan_metadata_priority = self.scan_metadata_priority

        scan_artwork_priority = self.scan_artwork_priority

        scan_region_priority = self.scan_region_priority

        scan_language_priority = self.scan_language_priority

        scan_media = self.scan_media

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CONFIG_FILE_MOUNTED": config_file_mounted,
                "CONFIG_FILE_WRITABLE": config_file_writable,
                "EXCLUDED_PLATFORMS": excluded_platforms,
                "EXCLUDED_SINGLE_EXT": excluded_single_ext,
                "EXCLUDED_SINGLE_FILES": excluded_single_files,
                "EXCLUDED_MULTI_FILES": excluded_multi_files,
                "EXCLUDED_MULTI_PARTS_EXT": excluded_multi_parts_ext,
                "EXCLUDED_MULTI_PARTS_FILES": excluded_multi_parts_files,
                "PLATFORMS_BINDING": platforms_binding,
                "PLATFORMS_VERSIONS": platforms_versions,
                "SKIP_HASH_CALCULATION": skip_hash_calculation,
                "EJS_DEBUG": ejs_debug,
                "EJS_CACHE_LIMIT": ejs_cache_limit,
                "EJS_DISABLE_AUTO_UNLOAD": ejs_disable_auto_unload,
                "EJS_DISABLE_BATCH_BOOTUP": ejs_disable_batch_bootup,
                "EJS_NETPLAY_ENABLED": ejs_netplay_enabled,
                "EJS_NETPLAY_ICE_SERVERS": ejs_netplay_ice_servers,
                "EJS_SETTINGS": ejs_settings,
                "EJS_CONTROLS": ejs_controls,
                "SCAN_METADATA_PRIORITY": scan_metadata_priority,
                "SCAN_ARTWORK_PRIORITY": scan_artwork_priority,
                "SCAN_REGION_PRIORITY": scan_region_priority,
                "SCAN_LANGUAGE_PRIORITY": scan_language_priority,
                "SCAN_MEDIA": scan_media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_response_ejs_controls import ConfigResponseEjsControls
        from ..models.config_response_ejs_settings import ConfigResponseEjsSettings
        from ..models.config_response_platforms_binding import ConfigResponsePlatformsBinding
        from ..models.config_response_platforms_versions import ConfigResponsePlatformsVersions
        from ..models.netplay_ice_server import NetplayICEServer

        d = dict(src_dict)
        config_file_mounted = d.pop("CONFIG_FILE_MOUNTED")

        config_file_writable = d.pop("CONFIG_FILE_WRITABLE")

        excluded_platforms = cast(list[str], d.pop("EXCLUDED_PLATFORMS"))

        excluded_single_ext = cast(list[str], d.pop("EXCLUDED_SINGLE_EXT"))

        excluded_single_files = cast(list[str], d.pop("EXCLUDED_SINGLE_FILES"))

        excluded_multi_files = cast(list[str], d.pop("EXCLUDED_MULTI_FILES"))

        excluded_multi_parts_ext = cast(list[str], d.pop("EXCLUDED_MULTI_PARTS_EXT"))

        excluded_multi_parts_files = cast(list[str], d.pop("EXCLUDED_MULTI_PARTS_FILES"))

        platforms_binding = ConfigResponsePlatformsBinding.from_dict(d.pop("PLATFORMS_BINDING"))

        platforms_versions = ConfigResponsePlatformsVersions.from_dict(d.pop("PLATFORMS_VERSIONS"))

        skip_hash_calculation = d.pop("SKIP_HASH_CALCULATION")

        ejs_debug = d.pop("EJS_DEBUG")

        def _parse_ejs_cache_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ejs_cache_limit = _parse_ejs_cache_limit(d.pop("EJS_CACHE_LIMIT"))

        ejs_disable_auto_unload = d.pop("EJS_DISABLE_AUTO_UNLOAD")

        ejs_disable_batch_bootup = d.pop("EJS_DISABLE_BATCH_BOOTUP")

        ejs_netplay_enabled = d.pop("EJS_NETPLAY_ENABLED")

        ejs_netplay_ice_servers = []
        _ejs_netplay_ice_servers = d.pop("EJS_NETPLAY_ICE_SERVERS")
        for ejs_netplay_ice_servers_item_data in _ejs_netplay_ice_servers:
            ejs_netplay_ice_servers_item = NetplayICEServer.from_dict(ejs_netplay_ice_servers_item_data)

            ejs_netplay_ice_servers.append(ejs_netplay_ice_servers_item)

        ejs_settings = ConfigResponseEjsSettings.from_dict(d.pop("EJS_SETTINGS"))

        ejs_controls = ConfigResponseEjsControls.from_dict(d.pop("EJS_CONTROLS"))

        scan_metadata_priority = cast(list[str], d.pop("SCAN_METADATA_PRIORITY"))

        scan_artwork_priority = cast(list[str], d.pop("SCAN_ARTWORK_PRIORITY"))

        scan_region_priority = cast(list[str], d.pop("SCAN_REGION_PRIORITY"))

        scan_language_priority = cast(list[str], d.pop("SCAN_LANGUAGE_PRIORITY"))

        scan_media = cast(list[str], d.pop("SCAN_MEDIA"))

        config_response = cls(
            config_file_mounted=config_file_mounted,
            config_file_writable=config_file_writable,
            excluded_platforms=excluded_platforms,
            excluded_single_ext=excluded_single_ext,
            excluded_single_files=excluded_single_files,
            excluded_multi_files=excluded_multi_files,
            excluded_multi_parts_ext=excluded_multi_parts_ext,
            excluded_multi_parts_files=excluded_multi_parts_files,
            platforms_binding=platforms_binding,
            platforms_versions=platforms_versions,
            skip_hash_calculation=skip_hash_calculation,
            ejs_debug=ejs_debug,
            ejs_cache_limit=ejs_cache_limit,
            ejs_disable_auto_unload=ejs_disable_auto_unload,
            ejs_disable_batch_bootup=ejs_disable_batch_bootup,
            ejs_netplay_enabled=ejs_netplay_enabled,
            ejs_netplay_ice_servers=ejs_netplay_ice_servers,
            ejs_settings=ejs_settings,
            ejs_controls=ejs_controls,
            scan_metadata_priority=scan_metadata_priority,
            scan_artwork_priority=scan_artwork_priority,
            scan_region_priority=scan_region_priority,
            scan_language_priority=scan_language_priority,
            scan_media=scan_media,
        )

        config_response.additional_properties = d
        return config_response

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
