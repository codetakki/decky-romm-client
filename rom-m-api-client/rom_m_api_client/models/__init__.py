"""Contains all the data models used in inputs/outputs"""

from .add_firmware_response import AddFirmwareResponse
from .body_add_collection_api_collections_post import BodyAddCollectionApiCollectionsPost
from .body_add_firmware_api_firmware_post import BodyAddFirmwareApiFirmwarePost
from .body_add_platform_api_platforms_post import BodyAddPlatformApiPlatformsPost
from .body_add_user_api_users_post import BodyAddUserApiUsersPost
from .body_create_user_from_invite_api_users_register_post import BodyCreateUserFromInviteApiUsersRegisterPost
from .body_delete_firmware_api_firmware_delete_post import BodyDeleteFirmwareApiFirmwareDeletePost
from .body_delete_roms_api_roms_delete_post import BodyDeleteRomsApiRomsDeletePost
from .body_delete_saves_api_saves_delete_post import BodyDeleteSavesApiSavesDeletePost
from .body_delete_states_api_states_delete_post import BodyDeleteStatesApiStatesDeletePost
from .body_refresh_retro_achievements_api_users_id_ra_refresh_post import (
    BodyRefreshRetroAchievementsApiUsersIdRaRefreshPost,
)
from .body_request_password_reset_api_forgot_password_post import BodyRequestPasswordResetApiForgotPasswordPost
from .body_reset_password_api_reset_password_post import BodyResetPasswordApiResetPasswordPost
from .body_token_api_token_post import BodyTokenApiTokenPost
from .body_update_collection_api_collections_id_put import BodyUpdateCollectionApiCollectionsIdPut
from .body_update_platform_api_platforms_id_put import BodyUpdatePlatformApiPlatformsIdPut
from .body_update_rom_api_roms_id_put import BodyUpdateRomApiRomsIdPut
from .body_update_rom_user_api_roms_id_props_put import BodyUpdateRomUserApiRomsIdPropsPut
from .bulk_operation_response import BulkOperationResponse
from .cleanup_stats import CleanupStats
from .cleanup_task_meta import CleanupTaskMeta
from .cleanup_task_status_response import CleanupTaskStatusResponse
from .collection_schema import CollectionSchema
from .config_response import ConfigResponse
from .config_response_ejs_controls import ConfigResponseEjsControls
from .config_response_ejs_settings import ConfigResponseEjsSettings
from .config_response_ejs_settings_additional_property import ConfigResponseEjsSettingsAdditionalProperty
from .config_response_platforms_binding import ConfigResponsePlatformsBinding
from .config_response_platforms_versions import ConfigResponsePlatformsVersions
from .conversion_stats import ConversionStats
from .conversion_task_meta import ConversionTaskMeta
from .conversion_task_status_response import ConversionTaskStatusResponse
from .create_rom_note_api_roms_id_notes_post_note_data import CreateRomNoteApiRomsIdNotesPostNoteData
from .custom_limit_offset_page_simple_rom_schema import CustomLimitOffsetPageSimpleRomSchema
from .custom_limit_offset_page_simple_rom_schema_char_index import CustomLimitOffsetPageSimpleRomSchemaCharIndex
from .delete_rom_note_api_roms_id_notes_note_id_delete_response_delete_rom_note_api_roms_id_notes_note_id_delete import (
    DeleteRomNoteApiRomsIdNotesNoteIdDeleteResponseDeleteRomNoteApiRomsIdNotesNoteIdDelete,
)
from .detailed_rom_schema import DetailedRomSchema
from .earned_achievement import EarnedAchievement
from .ejs_controls import EjsControls
from .ejs_controls_0 import EjsControls0
from .ejs_controls_1 import EjsControls1
from .ejs_controls_2 import EjsControls2
from .ejs_controls_3 import EjsControls3
from .ejs_controls_button import EjsControlsButton
from .emulation_dict import EmulationDict
from .filesystem_dict import FilesystemDict
from .firmware_schema import FirmwareSchema
from .frontend_dict import FrontendDict
from .generic_task_meta import GenericTaskMeta
from .generic_task_status_response import GenericTaskStatusResponse
from .get_rooms_api_netplay_list_get_response_get_rooms_api_netplay_list_get import (
    GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet,
)
from .heartbeat_response import HeartbeatResponse
from .http_validation_error import HTTPValidationError
from .igdb_age_rating import IGDBAgeRating
from .igdb_metadata_multiplayer_mode import IGDBMetadataMultiplayerMode
from .igdb_metadata_platform import IGDBMetadataPlatform
from .igdb_related_game import IGDBRelatedGame
from .invite_link_schema import InviteLinkSchema
from .job_status import JobStatus
from .launchbox_image import LaunchboxImage
from .list_tasks_api_tasks_get_response_list_tasks_api_tasks_get import ListTasksApiTasksGetResponseListTasksApiTasksGet
from .manual_metadata import ManualMetadata
from .metadata_sources_dict import MetadataSourcesDict
from .moby_metadata_platform import MobyMetadataPlatform
from .netplay_ice_server import NetplayICEServer
from .oidc_dict import OIDCDict
from .platform_schema import PlatformSchema
from .ra_game_rom_achievement import RAGameRomAchievement
from .ra_progression import RAProgression
from .ra_user_game_progression import RAUserGameProgression
from .role import Role
from .rom_file_category import RomFileCategory
from .rom_file_schema import RomFileSchema
from .rom_filters_dict import RomFiltersDict
from .rom_flashpoint_metadata import RomFlashpointMetadata
from .rom_gamelist_metadata import RomGamelistMetadata
from .rom_hasheous_metadata import RomHasheousMetadata
from .rom_hltb_metadata import RomHLTBMetadata
from .rom_igdb_metadata import RomIGDBMetadata
from .rom_launchbox_metadata import RomLaunchboxMetadata
from .rom_metadata_schema import RomMetadataSchema
from .rom_moby_metadata import RomMobyMetadata
from .rom_ra_metadata import RomRAMetadata
from .rom_ss_metadata import RomSSMetadata
from .rom_user_schema import RomUserSchema
from .rom_user_status import RomUserStatus
from .rooms_response import RoomsResponse
from .save_schema import SaveSchema
from .scan_stats import ScanStats
from .scan_task_meta import ScanTaskMeta
from .scan_task_status_response import ScanTaskStatusResponse
from .screenshot_schema import ScreenshotSchema
from .search_cover_schema import SearchCoverSchema
from .search_rom_schema import SearchRomSchema
from .sgdb_resource import SGDBResource
from .sibling_rom_schema import SiblingRomSchema
from .simple_rom_schema import SimpleRomSchema
from .smart_collection_schema import SmartCollectionSchema
from .smart_collection_schema_filter_criteria import SmartCollectionSchemaFilterCriteria
from .state_schema import StateSchema
from .stats_return import StatsReturn
from .system_dict import SystemDict
from .task_execution_response import TaskExecutionResponse
from .task_info import TaskInfo
from .task_type import TaskType
from .tasks_dict import TasksDict
from .tinfoil_feed_file_schema import TinfoilFeedFileSchema
from .tinfoil_feed_schema import TinfoilFeedSchema
from .tinfoil_feed_schema_titledb import TinfoilFeedSchemaTitledb
from .tinfoil_feed_schema_titledb_additional_property import TinfoilFeedSchemaTitledbAdditionalProperty
from .token_response import TokenResponse
from .update_rom_note_api_roms_id_notes_note_id_put_note_data import UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData
from .update_stats import UpdateStats
from .update_task_meta import UpdateTaskMeta
from .update_task_status_response import UpdateTaskStatusResponse
from .user_collection_schema import UserCollectionSchema
from .user_form import UserForm
from .user_note_schema import UserNoteSchema
from .user_schema import UserSchema
from .user_schema_ui_settings_type_0 import UserSchemaUiSettingsType0
from .validation_error import ValidationError
from .virtual_collection_schema import VirtualCollectionSchema
from .watcher_task_meta import WatcherTaskMeta
from .watcher_task_status_response import WatcherTaskStatusResponse
from .webrcade_feed_category_schema import WebrcadeFeedCategorySchema
from .webrcade_feed_item_props_schema import WebrcadeFeedItemPropsSchema
from .webrcade_feed_item_schema import WebrcadeFeedItemSchema
from .webrcade_feed_schema import WebrcadeFeedSchema

__all__ = (
    "AddFirmwareResponse",
    "BodyAddCollectionApiCollectionsPost",
    "BodyAddFirmwareApiFirmwarePost",
    "BodyAddPlatformApiPlatformsPost",
    "BodyAddUserApiUsersPost",
    "BodyCreateUserFromInviteApiUsersRegisterPost",
    "BodyDeleteFirmwareApiFirmwareDeletePost",
    "BodyDeleteRomsApiRomsDeletePost",
    "BodyDeleteSavesApiSavesDeletePost",
    "BodyDeleteStatesApiStatesDeletePost",
    "BodyRefreshRetroAchievementsApiUsersIdRaRefreshPost",
    "BodyRequestPasswordResetApiForgotPasswordPost",
    "BodyResetPasswordApiResetPasswordPost",
    "BodyTokenApiTokenPost",
    "BodyUpdateCollectionApiCollectionsIdPut",
    "BodyUpdatePlatformApiPlatformsIdPut",
    "BodyUpdateRomApiRomsIdPut",
    "BodyUpdateRomUserApiRomsIdPropsPut",
    "BulkOperationResponse",
    "CleanupStats",
    "CleanupTaskMeta",
    "CleanupTaskStatusResponse",
    "CollectionSchema",
    "ConfigResponse",
    "ConfigResponseEjsControls",
    "ConfigResponseEjsSettings",
    "ConfigResponseEjsSettingsAdditionalProperty",
    "ConfigResponsePlatformsBinding",
    "ConfigResponsePlatformsVersions",
    "ConversionStats",
    "ConversionTaskMeta",
    "ConversionTaskStatusResponse",
    "CreateRomNoteApiRomsIdNotesPostNoteData",
    "CustomLimitOffsetPageSimpleRomSchema",
    "CustomLimitOffsetPageSimpleRomSchemaCharIndex",
    "DeleteRomNoteApiRomsIdNotesNoteIdDeleteResponseDeleteRomNoteApiRomsIdNotesNoteIdDelete",
    "DetailedRomSchema",
    "EarnedAchievement",
    "EjsControls",
    "EjsControls0",
    "EjsControls1",
    "EjsControls2",
    "EjsControls3",
    "EjsControlsButton",
    "EmulationDict",
    "FilesystemDict",
    "FirmwareSchema",
    "FrontendDict",
    "GenericTaskMeta",
    "GenericTaskStatusResponse",
    "GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet",
    "HeartbeatResponse",
    "HTTPValidationError",
    "IGDBAgeRating",
    "IGDBMetadataMultiplayerMode",
    "IGDBMetadataPlatform",
    "IGDBRelatedGame",
    "InviteLinkSchema",
    "JobStatus",
    "LaunchboxImage",
    "ListTasksApiTasksGetResponseListTasksApiTasksGet",
    "ManualMetadata",
    "MetadataSourcesDict",
    "MobyMetadataPlatform",
    "NetplayICEServer",
    "OIDCDict",
    "PlatformSchema",
    "RAGameRomAchievement",
    "RAProgression",
    "RAUserGameProgression",
    "Role",
    "RomFileCategory",
    "RomFileSchema",
    "RomFiltersDict",
    "RomFlashpointMetadata",
    "RomGamelistMetadata",
    "RomHasheousMetadata",
    "RomHLTBMetadata",
    "RomIGDBMetadata",
    "RomLaunchboxMetadata",
    "RomMetadataSchema",
    "RomMobyMetadata",
    "RomRAMetadata",
    "RomSSMetadata",
    "RomUserSchema",
    "RomUserStatus",
    "RoomsResponse",
    "SaveSchema",
    "ScanStats",
    "ScanTaskMeta",
    "ScanTaskStatusResponse",
    "ScreenshotSchema",
    "SearchCoverSchema",
    "SearchRomSchema",
    "SGDBResource",
    "SiblingRomSchema",
    "SimpleRomSchema",
    "SmartCollectionSchema",
    "SmartCollectionSchemaFilterCriteria",
    "StateSchema",
    "StatsReturn",
    "SystemDict",
    "TaskExecutionResponse",
    "TaskInfo",
    "TasksDict",
    "TaskType",
    "TinfoilFeedFileSchema",
    "TinfoilFeedSchema",
    "TinfoilFeedSchemaTitledb",
    "TinfoilFeedSchemaTitledbAdditionalProperty",
    "TokenResponse",
    "UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData",
    "UpdateStats",
    "UpdateTaskMeta",
    "UpdateTaskStatusResponse",
    "UserCollectionSchema",
    "UserForm",
    "UserNoteSchema",
    "UserSchema",
    "UserSchemaUiSettingsType0",
    "ValidationError",
    "VirtualCollectionSchema",
    "WatcherTaskMeta",
    "WatcherTaskStatusResponse",
    "WebrcadeFeedCategorySchema",
    "WebrcadeFeedItemPropsSchema",
    "WebrcadeFeedItemSchema",
    "WebrcadeFeedSchema",
)
