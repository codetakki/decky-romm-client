from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.igdb_age_rating import IGDBAgeRating
    from ..models.igdb_metadata_multiplayer_mode import IGDBMetadataMultiplayerMode
    from ..models.igdb_metadata_platform import IGDBMetadataPlatform
    from ..models.igdb_related_game import IGDBRelatedGame


T = TypeVar("T", bound="RomIGDBMetadata")


@_attrs_define
class RomIGDBMetadata:
    """
    Attributes:
        total_rating (None | str | Unset):
        aggregated_rating (None | str | Unset):
        first_release_date (int | None | Unset):
        youtube_video_id (None | str | Unset):
        genres (list[str] | Unset):
        franchises (list[str] | Unset):
        alternative_names (list[str] | Unset):
        collections (list[str] | Unset):
        companies (list[str] | Unset):
        game_modes (list[str] | Unset):
        age_ratings (list[IGDBAgeRating] | Unset):
        platforms (list[IGDBMetadataPlatform] | Unset):
        multiplayer_modes (list[IGDBMetadataMultiplayerMode] | Unset):
        player_count (str | Unset):
        expansions (list[IGDBRelatedGame] | Unset):
        dlcs (list[IGDBRelatedGame] | Unset):
        remasters (list[IGDBRelatedGame] | Unset):
        remakes (list[IGDBRelatedGame] | Unset):
        expanded_games (list[IGDBRelatedGame] | Unset):
        ports (list[IGDBRelatedGame] | Unset):
        similar_games (list[IGDBRelatedGame] | Unset):
    """

    total_rating: None | str | Unset = UNSET
    aggregated_rating: None | str | Unset = UNSET
    first_release_date: int | None | Unset = UNSET
    youtube_video_id: None | str | Unset = UNSET
    genres: list[str] | Unset = UNSET
    franchises: list[str] | Unset = UNSET
    alternative_names: list[str] | Unset = UNSET
    collections: list[str] | Unset = UNSET
    companies: list[str] | Unset = UNSET
    game_modes: list[str] | Unset = UNSET
    age_ratings: list[IGDBAgeRating] | Unset = UNSET
    platforms: list[IGDBMetadataPlatform] | Unset = UNSET
    multiplayer_modes: list[IGDBMetadataMultiplayerMode] | Unset = UNSET
    player_count: str | Unset = UNSET
    expansions: list[IGDBRelatedGame] | Unset = UNSET
    dlcs: list[IGDBRelatedGame] | Unset = UNSET
    remasters: list[IGDBRelatedGame] | Unset = UNSET
    remakes: list[IGDBRelatedGame] | Unset = UNSET
    expanded_games: list[IGDBRelatedGame] | Unset = UNSET
    ports: list[IGDBRelatedGame] | Unset = UNSET
    similar_games: list[IGDBRelatedGame] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rating: None | str | Unset
        if isinstance(self.total_rating, Unset):
            total_rating = UNSET
        else:
            total_rating = self.total_rating

        aggregated_rating: None | str | Unset
        if isinstance(self.aggregated_rating, Unset):
            aggregated_rating = UNSET
        else:
            aggregated_rating = self.aggregated_rating

        first_release_date: int | None | Unset
        if isinstance(self.first_release_date, Unset):
            first_release_date = UNSET
        else:
            first_release_date = self.first_release_date

        youtube_video_id: None | str | Unset
        if isinstance(self.youtube_video_id, Unset):
            youtube_video_id = UNSET
        else:
            youtube_video_id = self.youtube_video_id

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        franchises: list[str] | Unset = UNSET
        if not isinstance(self.franchises, Unset):
            franchises = self.franchises

        alternative_names: list[str] | Unset = UNSET
        if not isinstance(self.alternative_names, Unset):
            alternative_names = self.alternative_names

        collections: list[str] | Unset = UNSET
        if not isinstance(self.collections, Unset):
            collections = self.collections

        companies: list[str] | Unset = UNSET
        if not isinstance(self.companies, Unset):
            companies = self.companies

        game_modes: list[str] | Unset = UNSET
        if not isinstance(self.game_modes, Unset):
            game_modes = self.game_modes

        age_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.age_ratings, Unset):
            age_ratings = []
            for age_ratings_item_data in self.age_ratings:
                age_ratings_item = age_ratings_item_data.to_dict()
                age_ratings.append(age_ratings_item)

        platforms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.to_dict()
                platforms.append(platforms_item)

        multiplayer_modes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multiplayer_modes, Unset):
            multiplayer_modes = []
            for multiplayer_modes_item_data in self.multiplayer_modes:
                multiplayer_modes_item = multiplayer_modes_item_data.to_dict()
                multiplayer_modes.append(multiplayer_modes_item)

        player_count = self.player_count

        expansions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expansions, Unset):
            expansions = []
            for expansions_item_data in self.expansions:
                expansions_item = expansions_item_data.to_dict()
                expansions.append(expansions_item)

        dlcs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dlcs, Unset):
            dlcs = []
            for dlcs_item_data in self.dlcs:
                dlcs_item = dlcs_item_data.to_dict()
                dlcs.append(dlcs_item)

        remasters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remasters, Unset):
            remasters = []
            for remasters_item_data in self.remasters:
                remasters_item = remasters_item_data.to_dict()
                remasters.append(remasters_item)

        remakes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remakes, Unset):
            remakes = []
            for remakes_item_data in self.remakes:
                remakes_item = remakes_item_data.to_dict()
                remakes.append(remakes_item)

        expanded_games: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expanded_games, Unset):
            expanded_games = []
            for expanded_games_item_data in self.expanded_games:
                expanded_games_item = expanded_games_item_data.to_dict()
                expanded_games.append(expanded_games_item)

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        similar_games: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.similar_games, Unset):
            similar_games = []
            for similar_games_item_data in self.similar_games:
                similar_games_item = similar_games_item_data.to_dict()
                similar_games.append(similar_games_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rating is not UNSET:
            field_dict["total_rating"] = total_rating
        if aggregated_rating is not UNSET:
            field_dict["aggregated_rating"] = aggregated_rating
        if first_release_date is not UNSET:
            field_dict["first_release_date"] = first_release_date
        if youtube_video_id is not UNSET:
            field_dict["youtube_video_id"] = youtube_video_id
        if genres is not UNSET:
            field_dict["genres"] = genres
        if franchises is not UNSET:
            field_dict["franchises"] = franchises
        if alternative_names is not UNSET:
            field_dict["alternative_names"] = alternative_names
        if collections is not UNSET:
            field_dict["collections"] = collections
        if companies is not UNSET:
            field_dict["companies"] = companies
        if game_modes is not UNSET:
            field_dict["game_modes"] = game_modes
        if age_ratings is not UNSET:
            field_dict["age_ratings"] = age_ratings
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if multiplayer_modes is not UNSET:
            field_dict["multiplayer_modes"] = multiplayer_modes
        if player_count is not UNSET:
            field_dict["player_count"] = player_count
        if expansions is not UNSET:
            field_dict["expansions"] = expansions
        if dlcs is not UNSET:
            field_dict["dlcs"] = dlcs
        if remasters is not UNSET:
            field_dict["remasters"] = remasters
        if remakes is not UNSET:
            field_dict["remakes"] = remakes
        if expanded_games is not UNSET:
            field_dict["expanded_games"] = expanded_games
        if ports is not UNSET:
            field_dict["ports"] = ports
        if similar_games is not UNSET:
            field_dict["similar_games"] = similar_games

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.igdb_age_rating import IGDBAgeRating
        from ..models.igdb_metadata_multiplayer_mode import IGDBMetadataMultiplayerMode
        from ..models.igdb_metadata_platform import IGDBMetadataPlatform
        from ..models.igdb_related_game import IGDBRelatedGame

        d = dict(src_dict)

        def _parse_total_rating(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_rating = _parse_total_rating(d.pop("total_rating", UNSET))

        def _parse_aggregated_rating(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aggregated_rating = _parse_aggregated_rating(d.pop("aggregated_rating", UNSET))

        def _parse_first_release_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_release_date = _parse_first_release_date(d.pop("first_release_date", UNSET))

        def _parse_youtube_video_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        youtube_video_id = _parse_youtube_video_id(d.pop("youtube_video_id", UNSET))

        genres = cast(list[str], d.pop("genres", UNSET))

        franchises = cast(list[str], d.pop("franchises", UNSET))

        alternative_names = cast(list[str], d.pop("alternative_names", UNSET))

        collections = cast(list[str], d.pop("collections", UNSET))

        companies = cast(list[str], d.pop("companies", UNSET))

        game_modes = cast(list[str], d.pop("game_modes", UNSET))

        _age_ratings = d.pop("age_ratings", UNSET)
        age_ratings: list[IGDBAgeRating] | Unset = UNSET
        if _age_ratings is not UNSET:
            age_ratings = []
            for age_ratings_item_data in _age_ratings:
                age_ratings_item = IGDBAgeRating.from_dict(age_ratings_item_data)

                age_ratings.append(age_ratings_item)

        _platforms = d.pop("platforms", UNSET)
        platforms: list[IGDBMetadataPlatform] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = IGDBMetadataPlatform.from_dict(platforms_item_data)

                platforms.append(platforms_item)

        _multiplayer_modes = d.pop("multiplayer_modes", UNSET)
        multiplayer_modes: list[IGDBMetadataMultiplayerMode] | Unset = UNSET
        if _multiplayer_modes is not UNSET:
            multiplayer_modes = []
            for multiplayer_modes_item_data in _multiplayer_modes:
                multiplayer_modes_item = IGDBMetadataMultiplayerMode.from_dict(multiplayer_modes_item_data)

                multiplayer_modes.append(multiplayer_modes_item)

        player_count = d.pop("player_count", UNSET)

        _expansions = d.pop("expansions", UNSET)
        expansions: list[IGDBRelatedGame] | Unset = UNSET
        if _expansions is not UNSET:
            expansions = []
            for expansions_item_data in _expansions:
                expansions_item = IGDBRelatedGame.from_dict(expansions_item_data)

                expansions.append(expansions_item)

        _dlcs = d.pop("dlcs", UNSET)
        dlcs: list[IGDBRelatedGame] | Unset = UNSET
        if _dlcs is not UNSET:
            dlcs = []
            for dlcs_item_data in _dlcs:
                dlcs_item = IGDBRelatedGame.from_dict(dlcs_item_data)

                dlcs.append(dlcs_item)

        _remasters = d.pop("remasters", UNSET)
        remasters: list[IGDBRelatedGame] | Unset = UNSET
        if _remasters is not UNSET:
            remasters = []
            for remasters_item_data in _remasters:
                remasters_item = IGDBRelatedGame.from_dict(remasters_item_data)

                remasters.append(remasters_item)

        _remakes = d.pop("remakes", UNSET)
        remakes: list[IGDBRelatedGame] | Unset = UNSET
        if _remakes is not UNSET:
            remakes = []
            for remakes_item_data in _remakes:
                remakes_item = IGDBRelatedGame.from_dict(remakes_item_data)

                remakes.append(remakes_item)

        _expanded_games = d.pop("expanded_games", UNSET)
        expanded_games: list[IGDBRelatedGame] | Unset = UNSET
        if _expanded_games is not UNSET:
            expanded_games = []
            for expanded_games_item_data in _expanded_games:
                expanded_games_item = IGDBRelatedGame.from_dict(expanded_games_item_data)

                expanded_games.append(expanded_games_item)

        _ports = d.pop("ports", UNSET)
        ports: list[IGDBRelatedGame] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = IGDBRelatedGame.from_dict(ports_item_data)

                ports.append(ports_item)

        _similar_games = d.pop("similar_games", UNSET)
        similar_games: list[IGDBRelatedGame] | Unset = UNSET
        if _similar_games is not UNSET:
            similar_games = []
            for similar_games_item_data in _similar_games:
                similar_games_item = IGDBRelatedGame.from_dict(similar_games_item_data)

                similar_games.append(similar_games_item)

        rom_igdb_metadata = cls(
            total_rating=total_rating,
            aggregated_rating=aggregated_rating,
            first_release_date=first_release_date,
            youtube_video_id=youtube_video_id,
            genres=genres,
            franchises=franchises,
            alternative_names=alternative_names,
            collections=collections,
            companies=companies,
            game_modes=game_modes,
            age_ratings=age_ratings,
            platforms=platforms,
            multiplayer_modes=multiplayer_modes,
            player_count=player_count,
            expansions=expansions,
            dlcs=dlcs,
            remasters=remasters,
            remakes=remakes,
            expanded_games=expanded_games,
            ports=ports,
            similar_games=similar_games,
        )

        rom_igdb_metadata.additional_properties = d
        return rom_igdb_metadata

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
