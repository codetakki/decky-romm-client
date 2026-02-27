from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.manual_metadata import ManualMetadata
    from ..models.rom_file_schema import RomFileSchema
    from ..models.rom_flashpoint_metadata import RomFlashpointMetadata
    from ..models.rom_gamelist_metadata import RomGamelistMetadata
    from ..models.rom_hasheous_metadata import RomHasheousMetadata
    from ..models.rom_hltb_metadata import RomHLTBMetadata
    from ..models.rom_igdb_metadata import RomIGDBMetadata
    from ..models.rom_launchbox_metadata import RomLaunchboxMetadata
    from ..models.rom_metadata_schema import RomMetadataSchema
    from ..models.rom_moby_metadata import RomMobyMetadata
    from ..models.rom_ra_metadata import RomRAMetadata
    from ..models.rom_ss_metadata import RomSSMetadata
    from ..models.rom_user_schema import RomUserSchema
    from ..models.save_schema import SaveSchema
    from ..models.screenshot_schema import ScreenshotSchema
    from ..models.sibling_rom_schema import SiblingRomSchema
    from ..models.state_schema import StateSchema
    from ..models.user_collection_schema import UserCollectionSchema
    from ..models.user_note_schema import UserNoteSchema


T = TypeVar("T", bound="DetailedRomSchema")


@_attrs_define
class DetailedRomSchema:
    """
    Attributes:
        id (int):
        igdb_id (int | None):
        sgdb_id (int | None):
        moby_id (int | None):
        ss_id (int | None):
        ra_id (int | None):
        launchbox_id (int | None):
        hasheous_id (int | None):
        tgdb_id (int | None):
        flashpoint_id (None | str):
        hltb_id (int | None):
        gamelist_id (None | str):
        platform_id (int):
        platform_slug (str):
        platform_fs_slug (str):
        platform_custom_name (None | str):
        platform_display_name (str):
        fs_name (str):
        fs_name_no_tags (str):
        fs_name_no_ext (str):
        fs_extension (str):
        fs_path (str):
        fs_size_bytes (int):
        name (None | str):
        slug (None | str):
        summary (None | str):
        alternative_names (list[str]):
        youtube_video_id (None | str):
        metadatum (RomMetadataSchema):
        igdb_metadata (None | RomIGDBMetadata):
        moby_metadata (None | RomMobyMetadata):
        ss_metadata (None | RomSSMetadata):
        launchbox_metadata (None | RomLaunchboxMetadata):
        hasheous_metadata (None | RomHasheousMetadata):
        flashpoint_metadata (None | RomFlashpointMetadata):
        hltb_metadata (None | RomHLTBMetadata):
        gamelist_metadata (None | RomGamelistMetadata):
        manual_metadata (ManualMetadata | None):
        path_cover_small (None | str):
        path_cover_large (None | str):
        url_cover (None | str):
        has_manual (bool):
        path_manual (None | str):
        url_manual (None | str):
        is_unidentified (bool):
        is_identified (bool):
        revision (None | str):
        regions (list[str]):
        languages (list[str]):
        tags (list[str]):
        crc_hash (None | str):
        md5_hash (None | str):
        sha1_hash (None | str):
        has_simple_single_file (bool):
        has_nested_single_file (bool):
        has_multiple_files (bool):
        files (list[RomFileSchema]):
        full_path (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        missing_from_fs (bool):
        has_notes (bool):
        siblings (list[SiblingRomSchema]):
        rom_user (RomUserSchema):
        merged_screenshots (list[str]):
        merged_ra_metadata (None | RomRAMetadata):
        user_saves (list[SaveSchema]):
        user_states (list[StateSchema]):
        user_screenshots (list[ScreenshotSchema]):
        user_collections (list[UserCollectionSchema]):
        all_user_notes (list[UserNoteSchema]):
        is_identifying (bool | Unset):  Default: False.
    """

    id: int
    igdb_id: int | None
    sgdb_id: int | None
    moby_id: int | None
    ss_id: int | None
    ra_id: int | None
    launchbox_id: int | None
    hasheous_id: int | None
    tgdb_id: int | None
    flashpoint_id: None | str
    hltb_id: int | None
    gamelist_id: None | str
    platform_id: int
    platform_slug: str
    platform_fs_slug: str
    platform_custom_name: None | str
    platform_display_name: str
    fs_name: str
    fs_name_no_tags: str
    fs_name_no_ext: str
    fs_extension: str
    fs_path: str
    fs_size_bytes: int
    name: None | str
    slug: None | str
    summary: None | str
    alternative_names: list[str]
    youtube_video_id: None | str
    metadatum: RomMetadataSchema
    igdb_metadata: None | RomIGDBMetadata
    moby_metadata: None | RomMobyMetadata
    ss_metadata: None | RomSSMetadata
    launchbox_metadata: None | RomLaunchboxMetadata
    hasheous_metadata: None | RomHasheousMetadata
    flashpoint_metadata: None | RomFlashpointMetadata
    hltb_metadata: None | RomHLTBMetadata
    gamelist_metadata: None | RomGamelistMetadata
    manual_metadata: ManualMetadata | None
    path_cover_small: None | str
    path_cover_large: None | str
    url_cover: None | str
    has_manual: bool
    path_manual: None | str
    url_manual: None | str
    is_unidentified: bool
    is_identified: bool
    revision: None | str
    regions: list[str]
    languages: list[str]
    tags: list[str]
    crc_hash: None | str
    md5_hash: None | str
    sha1_hash: None | str
    has_simple_single_file: bool
    has_nested_single_file: bool
    has_multiple_files: bool
    files: list[RomFileSchema]
    full_path: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    missing_from_fs: bool
    has_notes: bool
    siblings: list[SiblingRomSchema]
    rom_user: RomUserSchema
    merged_screenshots: list[str]
    merged_ra_metadata: None | RomRAMetadata
    user_saves: list[SaveSchema]
    user_states: list[StateSchema]
    user_screenshots: list[ScreenshotSchema]
    user_collections: list[UserCollectionSchema]
    all_user_notes: list[UserNoteSchema]
    is_identifying: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.manual_metadata import ManualMetadata
        from ..models.rom_flashpoint_metadata import RomFlashpointMetadata
        from ..models.rom_gamelist_metadata import RomGamelistMetadata
        from ..models.rom_hasheous_metadata import RomHasheousMetadata
        from ..models.rom_hltb_metadata import RomHLTBMetadata
        from ..models.rom_igdb_metadata import RomIGDBMetadata
        from ..models.rom_launchbox_metadata import RomLaunchboxMetadata
        from ..models.rom_moby_metadata import RomMobyMetadata
        from ..models.rom_ra_metadata import RomRAMetadata
        from ..models.rom_ss_metadata import RomSSMetadata

        id = self.id

        igdb_id: int | None
        igdb_id = self.igdb_id

        sgdb_id: int | None
        sgdb_id = self.sgdb_id

        moby_id: int | None
        moby_id = self.moby_id

        ss_id: int | None
        ss_id = self.ss_id

        ra_id: int | None
        ra_id = self.ra_id

        launchbox_id: int | None
        launchbox_id = self.launchbox_id

        hasheous_id: int | None
        hasheous_id = self.hasheous_id

        tgdb_id: int | None
        tgdb_id = self.tgdb_id

        flashpoint_id: None | str
        flashpoint_id = self.flashpoint_id

        hltb_id: int | None
        hltb_id = self.hltb_id

        gamelist_id: None | str
        gamelist_id = self.gamelist_id

        platform_id = self.platform_id

        platform_slug = self.platform_slug

        platform_fs_slug = self.platform_fs_slug

        platform_custom_name: None | str
        platform_custom_name = self.platform_custom_name

        platform_display_name = self.platform_display_name

        fs_name = self.fs_name

        fs_name_no_tags = self.fs_name_no_tags

        fs_name_no_ext = self.fs_name_no_ext

        fs_extension = self.fs_extension

        fs_path = self.fs_path

        fs_size_bytes = self.fs_size_bytes

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        summary: None | str
        summary = self.summary

        alternative_names = self.alternative_names

        youtube_video_id: None | str
        youtube_video_id = self.youtube_video_id

        metadatum = self.metadatum.to_dict()

        igdb_metadata: dict[str, Any] | None
        if isinstance(self.igdb_metadata, RomIGDBMetadata):
            igdb_metadata = self.igdb_metadata.to_dict()
        else:
            igdb_metadata = self.igdb_metadata

        moby_metadata: dict[str, Any] | None
        if isinstance(self.moby_metadata, RomMobyMetadata):
            moby_metadata = self.moby_metadata.to_dict()
        else:
            moby_metadata = self.moby_metadata

        ss_metadata: dict[str, Any] | None
        if isinstance(self.ss_metadata, RomSSMetadata):
            ss_metadata = self.ss_metadata.to_dict()
        else:
            ss_metadata = self.ss_metadata

        launchbox_metadata: dict[str, Any] | None
        if isinstance(self.launchbox_metadata, RomLaunchboxMetadata):
            launchbox_metadata = self.launchbox_metadata.to_dict()
        else:
            launchbox_metadata = self.launchbox_metadata

        hasheous_metadata: dict[str, Any] | None
        if isinstance(self.hasheous_metadata, RomHasheousMetadata):
            hasheous_metadata = self.hasheous_metadata.to_dict()
        else:
            hasheous_metadata = self.hasheous_metadata

        flashpoint_metadata: dict[str, Any] | None
        if isinstance(self.flashpoint_metadata, RomFlashpointMetadata):
            flashpoint_metadata = self.flashpoint_metadata.to_dict()
        else:
            flashpoint_metadata = self.flashpoint_metadata

        hltb_metadata: dict[str, Any] | None
        if isinstance(self.hltb_metadata, RomHLTBMetadata):
            hltb_metadata = self.hltb_metadata.to_dict()
        else:
            hltb_metadata = self.hltb_metadata

        gamelist_metadata: dict[str, Any] | None
        if isinstance(self.gamelist_metadata, RomGamelistMetadata):
            gamelist_metadata = self.gamelist_metadata.to_dict()
        else:
            gamelist_metadata = self.gamelist_metadata

        manual_metadata: dict[str, Any] | None
        if isinstance(self.manual_metadata, ManualMetadata):
            manual_metadata = self.manual_metadata.to_dict()
        else:
            manual_metadata = self.manual_metadata

        path_cover_small: None | str
        path_cover_small = self.path_cover_small

        path_cover_large: None | str
        path_cover_large = self.path_cover_large

        url_cover: None | str
        url_cover = self.url_cover

        has_manual = self.has_manual

        path_manual: None | str
        path_manual = self.path_manual

        url_manual: None | str
        url_manual = self.url_manual

        is_unidentified = self.is_unidentified

        is_identified = self.is_identified

        revision: None | str
        revision = self.revision

        regions = self.regions

        languages = self.languages

        tags = self.tags

        crc_hash: None | str
        crc_hash = self.crc_hash

        md5_hash: None | str
        md5_hash = self.md5_hash

        sha1_hash: None | str
        sha1_hash = self.sha1_hash

        has_simple_single_file = self.has_simple_single_file

        has_nested_single_file = self.has_nested_single_file

        has_multiple_files = self.has_multiple_files

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        full_path = self.full_path

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        missing_from_fs = self.missing_from_fs

        has_notes = self.has_notes

        siblings = []
        for siblings_item_data in self.siblings:
            siblings_item = siblings_item_data.to_dict()
            siblings.append(siblings_item)

        rom_user = self.rom_user.to_dict()

        merged_screenshots = self.merged_screenshots

        merged_ra_metadata: dict[str, Any] | None
        if isinstance(self.merged_ra_metadata, RomRAMetadata):
            merged_ra_metadata = self.merged_ra_metadata.to_dict()
        else:
            merged_ra_metadata = self.merged_ra_metadata

        user_saves = []
        for user_saves_item_data in self.user_saves:
            user_saves_item = user_saves_item_data.to_dict()
            user_saves.append(user_saves_item)

        user_states = []
        for user_states_item_data in self.user_states:
            user_states_item = user_states_item_data.to_dict()
            user_states.append(user_states_item)

        user_screenshots = []
        for user_screenshots_item_data in self.user_screenshots:
            user_screenshots_item = user_screenshots_item_data.to_dict()
            user_screenshots.append(user_screenshots_item)

        user_collections = []
        for user_collections_item_data in self.user_collections:
            user_collections_item = user_collections_item_data.to_dict()
            user_collections.append(user_collections_item)

        all_user_notes = []
        for all_user_notes_item_data in self.all_user_notes:
            all_user_notes_item = all_user_notes_item_data.to_dict()
            all_user_notes.append(all_user_notes_item)

        is_identifying = self.is_identifying

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "igdb_id": igdb_id,
                "sgdb_id": sgdb_id,
                "moby_id": moby_id,
                "ss_id": ss_id,
                "ra_id": ra_id,
                "launchbox_id": launchbox_id,
                "hasheous_id": hasheous_id,
                "tgdb_id": tgdb_id,
                "flashpoint_id": flashpoint_id,
                "hltb_id": hltb_id,
                "gamelist_id": gamelist_id,
                "platform_id": platform_id,
                "platform_slug": platform_slug,
                "platform_fs_slug": platform_fs_slug,
                "platform_custom_name": platform_custom_name,
                "platform_display_name": platform_display_name,
                "fs_name": fs_name,
                "fs_name_no_tags": fs_name_no_tags,
                "fs_name_no_ext": fs_name_no_ext,
                "fs_extension": fs_extension,
                "fs_path": fs_path,
                "fs_size_bytes": fs_size_bytes,
                "name": name,
                "slug": slug,
                "summary": summary,
                "alternative_names": alternative_names,
                "youtube_video_id": youtube_video_id,
                "metadatum": metadatum,
                "igdb_metadata": igdb_metadata,
                "moby_metadata": moby_metadata,
                "ss_metadata": ss_metadata,
                "launchbox_metadata": launchbox_metadata,
                "hasheous_metadata": hasheous_metadata,
                "flashpoint_metadata": flashpoint_metadata,
                "hltb_metadata": hltb_metadata,
                "gamelist_metadata": gamelist_metadata,
                "manual_metadata": manual_metadata,
                "path_cover_small": path_cover_small,
                "path_cover_large": path_cover_large,
                "url_cover": url_cover,
                "has_manual": has_manual,
                "path_manual": path_manual,
                "url_manual": url_manual,
                "is_unidentified": is_unidentified,
                "is_identified": is_identified,
                "revision": revision,
                "regions": regions,
                "languages": languages,
                "tags": tags,
                "crc_hash": crc_hash,
                "md5_hash": md5_hash,
                "sha1_hash": sha1_hash,
                "has_simple_single_file": has_simple_single_file,
                "has_nested_single_file": has_nested_single_file,
                "has_multiple_files": has_multiple_files,
                "files": files,
                "full_path": full_path,
                "created_at": created_at,
                "updated_at": updated_at,
                "missing_from_fs": missing_from_fs,
                "has_notes": has_notes,
                "siblings": siblings,
                "rom_user": rom_user,
                "merged_screenshots": merged_screenshots,
                "merged_ra_metadata": merged_ra_metadata,
                "user_saves": user_saves,
                "user_states": user_states,
                "user_screenshots": user_screenshots,
                "user_collections": user_collections,
                "all_user_notes": all_user_notes,
            }
        )
        if is_identifying is not UNSET:
            field_dict["is_identifying"] = is_identifying

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.manual_metadata import ManualMetadata
        from ..models.rom_file_schema import RomFileSchema
        from ..models.rom_flashpoint_metadata import RomFlashpointMetadata
        from ..models.rom_gamelist_metadata import RomGamelistMetadata
        from ..models.rom_hasheous_metadata import RomHasheousMetadata
        from ..models.rom_hltb_metadata import RomHLTBMetadata
        from ..models.rom_igdb_metadata import RomIGDBMetadata
        from ..models.rom_launchbox_metadata import RomLaunchboxMetadata
        from ..models.rom_metadata_schema import RomMetadataSchema
        from ..models.rom_moby_metadata import RomMobyMetadata
        from ..models.rom_ra_metadata import RomRAMetadata
        from ..models.rom_ss_metadata import RomSSMetadata
        from ..models.rom_user_schema import RomUserSchema
        from ..models.save_schema import SaveSchema
        from ..models.screenshot_schema import ScreenshotSchema
        from ..models.sibling_rom_schema import SiblingRomSchema
        from ..models.state_schema import StateSchema
        from ..models.user_collection_schema import UserCollectionSchema
        from ..models.user_note_schema import UserNoteSchema

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_igdb_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        igdb_id = _parse_igdb_id(d.pop("igdb_id"))

        def _parse_sgdb_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sgdb_id = _parse_sgdb_id(d.pop("sgdb_id"))

        def _parse_moby_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        moby_id = _parse_moby_id(d.pop("moby_id"))

        def _parse_ss_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ss_id = _parse_ss_id(d.pop("ss_id"))

        def _parse_ra_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ra_id = _parse_ra_id(d.pop("ra_id"))

        def _parse_launchbox_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        launchbox_id = _parse_launchbox_id(d.pop("launchbox_id"))

        def _parse_hasheous_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        hasheous_id = _parse_hasheous_id(d.pop("hasheous_id"))

        def _parse_tgdb_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        tgdb_id = _parse_tgdb_id(d.pop("tgdb_id"))

        def _parse_flashpoint_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        flashpoint_id = _parse_flashpoint_id(d.pop("flashpoint_id"))

        def _parse_hltb_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        hltb_id = _parse_hltb_id(d.pop("hltb_id"))

        def _parse_gamelist_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gamelist_id = _parse_gamelist_id(d.pop("gamelist_id"))

        platform_id = d.pop("platform_id")

        platform_slug = d.pop("platform_slug")

        platform_fs_slug = d.pop("platform_fs_slug")

        def _parse_platform_custom_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        platform_custom_name = _parse_platform_custom_name(d.pop("platform_custom_name"))

        platform_display_name = d.pop("platform_display_name")

        fs_name = d.pop("fs_name")

        fs_name_no_tags = d.pop("fs_name_no_tags")

        fs_name_no_ext = d.pop("fs_name_no_ext")

        fs_extension = d.pop("fs_extension")

        fs_path = d.pop("fs_path")

        fs_size_bytes = d.pop("fs_size_bytes")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        alternative_names = cast(list[str], d.pop("alternative_names"))

        def _parse_youtube_video_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        youtube_video_id = _parse_youtube_video_id(d.pop("youtube_video_id"))

        metadatum = RomMetadataSchema.from_dict(d.pop("metadatum"))

        def _parse_igdb_metadata(data: object) -> None | RomIGDBMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                igdb_metadata_type_0 = RomIGDBMetadata.from_dict(data)

                return igdb_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomIGDBMetadata, data)

        igdb_metadata = _parse_igdb_metadata(d.pop("igdb_metadata"))

        def _parse_moby_metadata(data: object) -> None | RomMobyMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                moby_metadata_type_0 = RomMobyMetadata.from_dict(data)

                return moby_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomMobyMetadata, data)

        moby_metadata = _parse_moby_metadata(d.pop("moby_metadata"))

        def _parse_ss_metadata(data: object) -> None | RomSSMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ss_metadata_type_0 = RomSSMetadata.from_dict(data)

                return ss_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomSSMetadata, data)

        ss_metadata = _parse_ss_metadata(d.pop("ss_metadata"))

        def _parse_launchbox_metadata(data: object) -> None | RomLaunchboxMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                launchbox_metadata_type_0 = RomLaunchboxMetadata.from_dict(data)

                return launchbox_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomLaunchboxMetadata, data)

        launchbox_metadata = _parse_launchbox_metadata(d.pop("launchbox_metadata"))

        def _parse_hasheous_metadata(data: object) -> None | RomHasheousMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hasheous_metadata_type_0 = RomHasheousMetadata.from_dict(data)

                return hasheous_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomHasheousMetadata, data)

        hasheous_metadata = _parse_hasheous_metadata(d.pop("hasheous_metadata"))

        def _parse_flashpoint_metadata(data: object) -> None | RomFlashpointMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                flashpoint_metadata_type_0 = RomFlashpointMetadata.from_dict(data)

                return flashpoint_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomFlashpointMetadata, data)

        flashpoint_metadata = _parse_flashpoint_metadata(d.pop("flashpoint_metadata"))

        def _parse_hltb_metadata(data: object) -> None | RomHLTBMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hltb_metadata_type_0 = RomHLTBMetadata.from_dict(data)

                return hltb_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomHLTBMetadata, data)

        hltb_metadata = _parse_hltb_metadata(d.pop("hltb_metadata"))

        def _parse_gamelist_metadata(data: object) -> None | RomGamelistMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                gamelist_metadata_type_0 = RomGamelistMetadata.from_dict(data)

                return gamelist_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomGamelistMetadata, data)

        gamelist_metadata = _parse_gamelist_metadata(d.pop("gamelist_metadata"))

        def _parse_manual_metadata(data: object) -> ManualMetadata | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manual_metadata_type_0 = ManualMetadata.from_dict(data)

                return manual_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ManualMetadata | None, data)

        manual_metadata = _parse_manual_metadata(d.pop("manual_metadata"))

        def _parse_path_cover_small(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path_cover_small = _parse_path_cover_small(d.pop("path_cover_small"))

        def _parse_path_cover_large(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path_cover_large = _parse_path_cover_large(d.pop("path_cover_large"))

        def _parse_url_cover(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url_cover = _parse_url_cover(d.pop("url_cover"))

        has_manual = d.pop("has_manual")

        def _parse_path_manual(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path_manual = _parse_path_manual(d.pop("path_manual"))

        def _parse_url_manual(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url_manual = _parse_url_manual(d.pop("url_manual"))

        is_unidentified = d.pop("is_unidentified")

        is_identified = d.pop("is_identified")

        def _parse_revision(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        revision = _parse_revision(d.pop("revision"))

        regions = cast(list[str], d.pop("regions"))

        languages = cast(list[str], d.pop("languages"))

        tags = cast(list[str], d.pop("tags"))

        def _parse_crc_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        crc_hash = _parse_crc_hash(d.pop("crc_hash"))

        def _parse_md5_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        md5_hash = _parse_md5_hash(d.pop("md5_hash"))

        def _parse_sha1_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sha1_hash = _parse_sha1_hash(d.pop("sha1_hash"))

        has_simple_single_file = d.pop("has_simple_single_file")

        has_nested_single_file = d.pop("has_nested_single_file")

        has_multiple_files = d.pop("has_multiple_files")

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = RomFileSchema.from_dict(files_item_data)

            files.append(files_item)

        full_path = d.pop("full_path")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        missing_from_fs = d.pop("missing_from_fs")

        has_notes = d.pop("has_notes")

        siblings = []
        _siblings = d.pop("siblings")
        for siblings_item_data in _siblings:
            siblings_item = SiblingRomSchema.from_dict(siblings_item_data)

            siblings.append(siblings_item)

        rom_user = RomUserSchema.from_dict(d.pop("rom_user"))

        merged_screenshots = cast(list[str], d.pop("merged_screenshots"))

        def _parse_merged_ra_metadata(data: object) -> None | RomRAMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                merged_ra_metadata_type_0 = RomRAMetadata.from_dict(data)

                return merged_ra_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RomRAMetadata, data)

        merged_ra_metadata = _parse_merged_ra_metadata(d.pop("merged_ra_metadata"))

        user_saves = []
        _user_saves = d.pop("user_saves")
        for user_saves_item_data in _user_saves:
            user_saves_item = SaveSchema.from_dict(user_saves_item_data)

            user_saves.append(user_saves_item)

        user_states = []
        _user_states = d.pop("user_states")
        for user_states_item_data in _user_states:
            user_states_item = StateSchema.from_dict(user_states_item_data)

            user_states.append(user_states_item)

        user_screenshots = []
        _user_screenshots = d.pop("user_screenshots")
        for user_screenshots_item_data in _user_screenshots:
            user_screenshots_item = ScreenshotSchema.from_dict(user_screenshots_item_data)

            user_screenshots.append(user_screenshots_item)

        user_collections = []
        _user_collections = d.pop("user_collections")
        for user_collections_item_data in _user_collections:
            user_collections_item = UserCollectionSchema.from_dict(user_collections_item_data)

            user_collections.append(user_collections_item)

        all_user_notes = []
        _all_user_notes = d.pop("all_user_notes")
        for all_user_notes_item_data in _all_user_notes:
            all_user_notes_item = UserNoteSchema.from_dict(all_user_notes_item_data)

            all_user_notes.append(all_user_notes_item)

        is_identifying = d.pop("is_identifying", UNSET)

        detailed_rom_schema = cls(
            id=id,
            igdb_id=igdb_id,
            sgdb_id=sgdb_id,
            moby_id=moby_id,
            ss_id=ss_id,
            ra_id=ra_id,
            launchbox_id=launchbox_id,
            hasheous_id=hasheous_id,
            tgdb_id=tgdb_id,
            flashpoint_id=flashpoint_id,
            hltb_id=hltb_id,
            gamelist_id=gamelist_id,
            platform_id=platform_id,
            platform_slug=platform_slug,
            platform_fs_slug=platform_fs_slug,
            platform_custom_name=platform_custom_name,
            platform_display_name=platform_display_name,
            fs_name=fs_name,
            fs_name_no_tags=fs_name_no_tags,
            fs_name_no_ext=fs_name_no_ext,
            fs_extension=fs_extension,
            fs_path=fs_path,
            fs_size_bytes=fs_size_bytes,
            name=name,
            slug=slug,
            summary=summary,
            alternative_names=alternative_names,
            youtube_video_id=youtube_video_id,
            metadatum=metadatum,
            igdb_metadata=igdb_metadata,
            moby_metadata=moby_metadata,
            ss_metadata=ss_metadata,
            launchbox_metadata=launchbox_metadata,
            hasheous_metadata=hasheous_metadata,
            flashpoint_metadata=flashpoint_metadata,
            hltb_metadata=hltb_metadata,
            gamelist_metadata=gamelist_metadata,
            manual_metadata=manual_metadata,
            path_cover_small=path_cover_small,
            path_cover_large=path_cover_large,
            url_cover=url_cover,
            has_manual=has_manual,
            path_manual=path_manual,
            url_manual=url_manual,
            is_unidentified=is_unidentified,
            is_identified=is_identified,
            revision=revision,
            regions=regions,
            languages=languages,
            tags=tags,
            crc_hash=crc_hash,
            md5_hash=md5_hash,
            sha1_hash=sha1_hash,
            has_simple_single_file=has_simple_single_file,
            has_nested_single_file=has_nested_single_file,
            has_multiple_files=has_multiple_files,
            files=files,
            full_path=full_path,
            created_at=created_at,
            updated_at=updated_at,
            missing_from_fs=missing_from_fs,
            has_notes=has_notes,
            siblings=siblings,
            rom_user=rom_user,
            merged_screenshots=merged_screenshots,
            merged_ra_metadata=merged_ra_metadata,
            user_saves=user_saves,
            user_states=user_states,
            user_screenshots=user_screenshots,
            user_collections=user_collections,
            all_user_notes=all_user_notes,
            is_identifying=is_identifying,
        )

        detailed_rom_schema.additional_properties = d
        return detailed_rom_schema

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
