import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_limit_offset_page_simple_rom_schema import CustomLimitOffsetPageSimpleRomSchema
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    with_char_index: bool | Unset = True,
    with_filter_values: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
    platform_ids: list[int] | None | Unset = UNSET,
    collection_id: int | None | Unset = UNSET,
    virtual_collection_id: None | str | Unset = UNSET,
    smart_collection_id: int | None | Unset = UNSET,
    matched: bool | None | Unset = UNSET,
    favorite: bool | None | Unset = UNSET,
    duplicate: bool | None | Unset = UNSET,
    last_played: bool | None | Unset = UNSET,
    playable: bool | None | Unset = UNSET,
    missing: bool | None | Unset = UNSET,
    has_ra: bool | None | Unset = UNSET,
    verified: bool | None | Unset = UNSET,
    group_by_meta_id: bool | Unset = False,
    genres: list[str] | None | Unset = UNSET,
    franchises: list[str] | None | Unset = UNSET,
    collections: list[str] | None | Unset = UNSET,
    companies: list[str] | None | Unset = UNSET,
    age_ratings: list[str] | None | Unset = UNSET,
    statuses: list[str] | None | Unset = UNSET,
    regions: list[str] | None | Unset = UNSET,
    languages: list[str] | None | Unset = UNSET,
    player_counts: list[str] | None | Unset = UNSET,
    genres_logic: str | Unset = "any",
    franchises_logic: str | Unset = "any",
    collections_logic: str | Unset = "any",
    companies_logic: str | Unset = "any",
    age_ratings_logic: str | Unset = "any",
    regions_logic: str | Unset = "any",
    languages_logic: str | Unset = "any",
    statuses_logic: str | Unset = "any",
    player_counts_logic: str | Unset = "any",
    order_by: str | Unset = "name",
    order_dir: str | Unset = "asc",
    updated_after: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["with_char_index"] = with_char_index

    params["with_filter_values"] = with_filter_values

    json_search_term: None | str | Unset
    if isinstance(search_term, Unset):
        json_search_term = UNSET
    else:
        json_search_term = search_term
    params["search_term"] = json_search_term

    json_platform_ids: list[int] | None | Unset
    if isinstance(platform_ids, Unset):
        json_platform_ids = UNSET
    elif isinstance(platform_ids, list):
        json_platform_ids = platform_ids

    else:
        json_platform_ids = platform_ids
    params["platform_ids"] = json_platform_ids

    json_collection_id: int | None | Unset
    if isinstance(collection_id, Unset):
        json_collection_id = UNSET
    else:
        json_collection_id = collection_id
    params["collection_id"] = json_collection_id

    json_virtual_collection_id: None | str | Unset
    if isinstance(virtual_collection_id, Unset):
        json_virtual_collection_id = UNSET
    else:
        json_virtual_collection_id = virtual_collection_id
    params["virtual_collection_id"] = json_virtual_collection_id

    json_smart_collection_id: int | None | Unset
    if isinstance(smart_collection_id, Unset):
        json_smart_collection_id = UNSET
    else:
        json_smart_collection_id = smart_collection_id
    params["smart_collection_id"] = json_smart_collection_id

    json_matched: bool | None | Unset
    if isinstance(matched, Unset):
        json_matched = UNSET
    else:
        json_matched = matched
    params["matched"] = json_matched

    json_favorite: bool | None | Unset
    if isinstance(favorite, Unset):
        json_favorite = UNSET
    else:
        json_favorite = favorite
    params["favorite"] = json_favorite

    json_duplicate: bool | None | Unset
    if isinstance(duplicate, Unset):
        json_duplicate = UNSET
    else:
        json_duplicate = duplicate
    params["duplicate"] = json_duplicate

    json_last_played: bool | None | Unset
    if isinstance(last_played, Unset):
        json_last_played = UNSET
    else:
        json_last_played = last_played
    params["last_played"] = json_last_played

    json_playable: bool | None | Unset
    if isinstance(playable, Unset):
        json_playable = UNSET
    else:
        json_playable = playable
    params["playable"] = json_playable

    json_missing: bool | None | Unset
    if isinstance(missing, Unset):
        json_missing = UNSET
    else:
        json_missing = missing
    params["missing"] = json_missing

    json_has_ra: bool | None | Unset
    if isinstance(has_ra, Unset):
        json_has_ra = UNSET
    else:
        json_has_ra = has_ra
    params["has_ra"] = json_has_ra

    json_verified: bool | None | Unset
    if isinstance(verified, Unset):
        json_verified = UNSET
    else:
        json_verified = verified
    params["verified"] = json_verified

    params["group_by_meta_id"] = group_by_meta_id

    json_genres: list[str] | None | Unset
    if isinstance(genres, Unset):
        json_genres = UNSET
    elif isinstance(genres, list):
        json_genres = genres

    else:
        json_genres = genres
    params["genres"] = json_genres

    json_franchises: list[str] | None | Unset
    if isinstance(franchises, Unset):
        json_franchises = UNSET
    elif isinstance(franchises, list):
        json_franchises = franchises

    else:
        json_franchises = franchises
    params["franchises"] = json_franchises

    json_collections: list[str] | None | Unset
    if isinstance(collections, Unset):
        json_collections = UNSET
    elif isinstance(collections, list):
        json_collections = collections

    else:
        json_collections = collections
    params["collections"] = json_collections

    json_companies: list[str] | None | Unset
    if isinstance(companies, Unset):
        json_companies = UNSET
    elif isinstance(companies, list):
        json_companies = companies

    else:
        json_companies = companies
    params["companies"] = json_companies

    json_age_ratings: list[str] | None | Unset
    if isinstance(age_ratings, Unset):
        json_age_ratings = UNSET
    elif isinstance(age_ratings, list):
        json_age_ratings = age_ratings

    else:
        json_age_ratings = age_ratings
    params["age_ratings"] = json_age_ratings

    json_statuses: list[str] | None | Unset
    if isinstance(statuses, Unset):
        json_statuses = UNSET
    elif isinstance(statuses, list):
        json_statuses = statuses

    else:
        json_statuses = statuses
    params["statuses"] = json_statuses

    json_regions: list[str] | None | Unset
    if isinstance(regions, Unset):
        json_regions = UNSET
    elif isinstance(regions, list):
        json_regions = regions

    else:
        json_regions = regions
    params["regions"] = json_regions

    json_languages: list[str] | None | Unset
    if isinstance(languages, Unset):
        json_languages = UNSET
    elif isinstance(languages, list):
        json_languages = languages

    else:
        json_languages = languages
    params["languages"] = json_languages

    json_player_counts: list[str] | None | Unset
    if isinstance(player_counts, Unset):
        json_player_counts = UNSET
    elif isinstance(player_counts, list):
        json_player_counts = player_counts

    else:
        json_player_counts = player_counts
    params["player_counts"] = json_player_counts

    params["genres_logic"] = genres_logic

    params["franchises_logic"] = franchises_logic

    params["collections_logic"] = collections_logic

    params["companies_logic"] = companies_logic

    params["age_ratings_logic"] = age_ratings_logic

    params["regions_logic"] = regions_logic

    params["languages_logic"] = languages_logic

    params["statuses_logic"] = statuses_logic

    params["player_counts_logic"] = player_counts_logic

    params["order_by"] = order_by

    params["order_dir"] = order_dir

    json_updated_after: None | str | Unset
    if isinstance(updated_after, Unset):
        json_updated_after = UNSET
    elif isinstance(updated_after, datetime.datetime):
        json_updated_after = updated_after.isoformat()
    else:
        json_updated_after = updated_after
    params["updated_after"] = json_updated_after

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/roms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CustomLimitOffsetPageSimpleRomSchema.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    with_char_index: bool | Unset = True,
    with_filter_values: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
    platform_ids: list[int] | None | Unset = UNSET,
    collection_id: int | None | Unset = UNSET,
    virtual_collection_id: None | str | Unset = UNSET,
    smart_collection_id: int | None | Unset = UNSET,
    matched: bool | None | Unset = UNSET,
    favorite: bool | None | Unset = UNSET,
    duplicate: bool | None | Unset = UNSET,
    last_played: bool | None | Unset = UNSET,
    playable: bool | None | Unset = UNSET,
    missing: bool | None | Unset = UNSET,
    has_ra: bool | None | Unset = UNSET,
    verified: bool | None | Unset = UNSET,
    group_by_meta_id: bool | Unset = False,
    genres: list[str] | None | Unset = UNSET,
    franchises: list[str] | None | Unset = UNSET,
    collections: list[str] | None | Unset = UNSET,
    companies: list[str] | None | Unset = UNSET,
    age_ratings: list[str] | None | Unset = UNSET,
    statuses: list[str] | None | Unset = UNSET,
    regions: list[str] | None | Unset = UNSET,
    languages: list[str] | None | Unset = UNSET,
    player_counts: list[str] | None | Unset = UNSET,
    genres_logic: str | Unset = "any",
    franchises_logic: str | Unset = "any",
    collections_logic: str | Unset = "any",
    companies_logic: str | Unset = "any",
    age_ratings_logic: str | Unset = "any",
    regions_logic: str | Unset = "any",
    languages_logic: str | Unset = "any",
    statuses_logic: str | Unset = "any",
    player_counts_logic: str | Unset = "any",
    order_by: str | Unset = "name",
    order_dir: str | Unset = "asc",
    updated_after: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError]:
    """Get Roms

     Retrieve roms.

    Args:
        with_char_index (bool | Unset): Whether to get the char index. Default: True.
        with_filter_values (bool | Unset): Whether to return filter values. Default: True.
        search_term (None | str | Unset): Search term to filter roms.
        platform_ids (list[int] | None | Unset): Platform internal ids. Multiple values are
            allowed by repeating the parameter, and results that match any of the values will be
            returned.
        collection_id (int | None | Unset): Collection internal id.
        virtual_collection_id (None | str | Unset): Virtual collection internal id.
        smart_collection_id (int | None | Unset): Smart collection internal id.
        matched (bool | None | Unset): Whether the rom matched at least one metadata source.
        favorite (bool | None | Unset): Whether the rom is marked as favorite.
        duplicate (bool | None | Unset): Whether the rom is marked as duplicate.
        last_played (bool | None | Unset): Whether the rom has a last played value for the current
            user.
        playable (bool | None | Unset): Whether the rom is playable from the browser.
        missing (bool | None | Unset): Whether the rom is missing from the filesystem.
        has_ra (bool | None | Unset): Whether the rom has RetroAchievements data.
        verified (bool | None | Unset): Whether the rom is verified by Hasheous.
        group_by_meta_id (bool | Unset): Whether to group roms by metadata ID (IGDB / Moby /
            ScreenScraper / RetroAchievements / LaunchBox). Default: False.
        genres (list[str] | None | Unset): Associated genre. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        franchises (list[str] | None | Unset): Associated franchise. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        collections (list[str] | None | Unset): Associated collection. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        companies (list[str] | None | Unset): Associated company. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        age_ratings (list[str] | None | Unset): Associated age rating. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        statuses (list[str] | None | Unset): Game status, set by the current user. Multiple values
            are allowed by repeating the parameter, and results that match any of the values will be
            returned.
        regions (list[str] | None | Unset): Associated region tag. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        languages (list[str] | None | Unset): Associated language tag. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        player_counts (list[str] | None | Unset): Associated player count. Multiple values are
            allowed by repeating the parameter, and results that match any of the values will be
            returned.
        genres_logic (str | Unset): Logic operator for genres filter: 'any' (OR), 'all' (AND) or
            'none' (NOT). Default: 'any'.
        franchises_logic (str | Unset): Logic operator for franchises filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        collections_logic (str | Unset): Logic operator for collections filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        companies_logic (str | Unset): Logic operator for companies filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        age_ratings_logic (str | Unset): Logic operator for age ratings filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        regions_logic (str | Unset): Logic operator for regions filter: 'any' (OR), 'all' (AND) or
            'none' (NOT). Default: 'any'.
        languages_logic (str | Unset): Logic operator for languages filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        statuses_logic (str | Unset): Logic operator for statuses filter: 'any' (OR), 'all' (AND)
            or 'none' (NOT). Default: 'any'.
        player_counts_logic (str | Unset): Logic operator for player counts filter: 'any' (OR),
            'all' (AND) or 'none' (NOT). Default: 'any'.
        order_by (str | Unset): Field to order results by. Default: 'name'.
        order_dir (str | Unset): Order direction, either 'asc' or 'desc'. Default: 'asc'.
        updated_after (datetime.datetime | None | Unset): Filter roms updated after this datetime
            (ISO 8601 format with timezone information).
        limit (int | Unset): Page size limit Default: 50.
        offset (int | Unset): Page offset Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        with_char_index=with_char_index,
        with_filter_values=with_filter_values,
        search_term=search_term,
        platform_ids=platform_ids,
        collection_id=collection_id,
        virtual_collection_id=virtual_collection_id,
        smart_collection_id=smart_collection_id,
        matched=matched,
        favorite=favorite,
        duplicate=duplicate,
        last_played=last_played,
        playable=playable,
        missing=missing,
        has_ra=has_ra,
        verified=verified,
        group_by_meta_id=group_by_meta_id,
        genres=genres,
        franchises=franchises,
        collections=collections,
        companies=companies,
        age_ratings=age_ratings,
        statuses=statuses,
        regions=regions,
        languages=languages,
        player_counts=player_counts,
        genres_logic=genres_logic,
        franchises_logic=franchises_logic,
        collections_logic=collections_logic,
        companies_logic=companies_logic,
        age_ratings_logic=age_ratings_logic,
        regions_logic=regions_logic,
        languages_logic=languages_logic,
        statuses_logic=statuses_logic,
        player_counts_logic=player_counts_logic,
        order_by=order_by,
        order_dir=order_dir,
        updated_after=updated_after,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    with_char_index: bool | Unset = True,
    with_filter_values: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
    platform_ids: list[int] | None | Unset = UNSET,
    collection_id: int | None | Unset = UNSET,
    virtual_collection_id: None | str | Unset = UNSET,
    smart_collection_id: int | None | Unset = UNSET,
    matched: bool | None | Unset = UNSET,
    favorite: bool | None | Unset = UNSET,
    duplicate: bool | None | Unset = UNSET,
    last_played: bool | None | Unset = UNSET,
    playable: bool | None | Unset = UNSET,
    missing: bool | None | Unset = UNSET,
    has_ra: bool | None | Unset = UNSET,
    verified: bool | None | Unset = UNSET,
    group_by_meta_id: bool | Unset = False,
    genres: list[str] | None | Unset = UNSET,
    franchises: list[str] | None | Unset = UNSET,
    collections: list[str] | None | Unset = UNSET,
    companies: list[str] | None | Unset = UNSET,
    age_ratings: list[str] | None | Unset = UNSET,
    statuses: list[str] | None | Unset = UNSET,
    regions: list[str] | None | Unset = UNSET,
    languages: list[str] | None | Unset = UNSET,
    player_counts: list[str] | None | Unset = UNSET,
    genres_logic: str | Unset = "any",
    franchises_logic: str | Unset = "any",
    collections_logic: str | Unset = "any",
    companies_logic: str | Unset = "any",
    age_ratings_logic: str | Unset = "any",
    regions_logic: str | Unset = "any",
    languages_logic: str | Unset = "any",
    statuses_logic: str | Unset = "any",
    player_counts_logic: str | Unset = "any",
    order_by: str | Unset = "name",
    order_dir: str | Unset = "asc",
    updated_after: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError | None:
    """Get Roms

     Retrieve roms.

    Args:
        with_char_index (bool | Unset): Whether to get the char index. Default: True.
        with_filter_values (bool | Unset): Whether to return filter values. Default: True.
        search_term (None | str | Unset): Search term to filter roms.
        platform_ids (list[int] | None | Unset): Platform internal ids. Multiple values are
            allowed by repeating the parameter, and results that match any of the values will be
            returned.
        collection_id (int | None | Unset): Collection internal id.
        virtual_collection_id (None | str | Unset): Virtual collection internal id.
        smart_collection_id (int | None | Unset): Smart collection internal id.
        matched (bool | None | Unset): Whether the rom matched at least one metadata source.
        favorite (bool | None | Unset): Whether the rom is marked as favorite.
        duplicate (bool | None | Unset): Whether the rom is marked as duplicate.
        last_played (bool | None | Unset): Whether the rom has a last played value for the current
            user.
        playable (bool | None | Unset): Whether the rom is playable from the browser.
        missing (bool | None | Unset): Whether the rom is missing from the filesystem.
        has_ra (bool | None | Unset): Whether the rom has RetroAchievements data.
        verified (bool | None | Unset): Whether the rom is verified by Hasheous.
        group_by_meta_id (bool | Unset): Whether to group roms by metadata ID (IGDB / Moby /
            ScreenScraper / RetroAchievements / LaunchBox). Default: False.
        genres (list[str] | None | Unset): Associated genre. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        franchises (list[str] | None | Unset): Associated franchise. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        collections (list[str] | None | Unset): Associated collection. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        companies (list[str] | None | Unset): Associated company. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        age_ratings (list[str] | None | Unset): Associated age rating. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        statuses (list[str] | None | Unset): Game status, set by the current user. Multiple values
            are allowed by repeating the parameter, and results that match any of the values will be
            returned.
        regions (list[str] | None | Unset): Associated region tag. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        languages (list[str] | None | Unset): Associated language tag. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        player_counts (list[str] | None | Unset): Associated player count. Multiple values are
            allowed by repeating the parameter, and results that match any of the values will be
            returned.
        genres_logic (str | Unset): Logic operator for genres filter: 'any' (OR), 'all' (AND) or
            'none' (NOT). Default: 'any'.
        franchises_logic (str | Unset): Logic operator for franchises filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        collections_logic (str | Unset): Logic operator for collections filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        companies_logic (str | Unset): Logic operator for companies filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        age_ratings_logic (str | Unset): Logic operator for age ratings filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        regions_logic (str | Unset): Logic operator for regions filter: 'any' (OR), 'all' (AND) or
            'none' (NOT). Default: 'any'.
        languages_logic (str | Unset): Logic operator for languages filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        statuses_logic (str | Unset): Logic operator for statuses filter: 'any' (OR), 'all' (AND)
            or 'none' (NOT). Default: 'any'.
        player_counts_logic (str | Unset): Logic operator for player counts filter: 'any' (OR),
            'all' (AND) or 'none' (NOT). Default: 'any'.
        order_by (str | Unset): Field to order results by. Default: 'name'.
        order_dir (str | Unset): Order direction, either 'asc' or 'desc'. Default: 'asc'.
        updated_after (datetime.datetime | None | Unset): Filter roms updated after this datetime
            (ISO 8601 format with timezone information).
        limit (int | Unset): Page size limit Default: 50.
        offset (int | Unset): Page offset Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        with_char_index=with_char_index,
        with_filter_values=with_filter_values,
        search_term=search_term,
        platform_ids=platform_ids,
        collection_id=collection_id,
        virtual_collection_id=virtual_collection_id,
        smart_collection_id=smart_collection_id,
        matched=matched,
        favorite=favorite,
        duplicate=duplicate,
        last_played=last_played,
        playable=playable,
        missing=missing,
        has_ra=has_ra,
        verified=verified,
        group_by_meta_id=group_by_meta_id,
        genres=genres,
        franchises=franchises,
        collections=collections,
        companies=companies,
        age_ratings=age_ratings,
        statuses=statuses,
        regions=regions,
        languages=languages,
        player_counts=player_counts,
        genres_logic=genres_logic,
        franchises_logic=franchises_logic,
        collections_logic=collections_logic,
        companies_logic=companies_logic,
        age_ratings_logic=age_ratings_logic,
        regions_logic=regions_logic,
        languages_logic=languages_logic,
        statuses_logic=statuses_logic,
        player_counts_logic=player_counts_logic,
        order_by=order_by,
        order_dir=order_dir,
        updated_after=updated_after,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    with_char_index: bool | Unset = True,
    with_filter_values: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
    platform_ids: list[int] | None | Unset = UNSET,
    collection_id: int | None | Unset = UNSET,
    virtual_collection_id: None | str | Unset = UNSET,
    smart_collection_id: int | None | Unset = UNSET,
    matched: bool | None | Unset = UNSET,
    favorite: bool | None | Unset = UNSET,
    duplicate: bool | None | Unset = UNSET,
    last_played: bool | None | Unset = UNSET,
    playable: bool | None | Unset = UNSET,
    missing: bool | None | Unset = UNSET,
    has_ra: bool | None | Unset = UNSET,
    verified: bool | None | Unset = UNSET,
    group_by_meta_id: bool | Unset = False,
    genres: list[str] | None | Unset = UNSET,
    franchises: list[str] | None | Unset = UNSET,
    collections: list[str] | None | Unset = UNSET,
    companies: list[str] | None | Unset = UNSET,
    age_ratings: list[str] | None | Unset = UNSET,
    statuses: list[str] | None | Unset = UNSET,
    regions: list[str] | None | Unset = UNSET,
    languages: list[str] | None | Unset = UNSET,
    player_counts: list[str] | None | Unset = UNSET,
    genres_logic: str | Unset = "any",
    franchises_logic: str | Unset = "any",
    collections_logic: str | Unset = "any",
    companies_logic: str | Unset = "any",
    age_ratings_logic: str | Unset = "any",
    regions_logic: str | Unset = "any",
    languages_logic: str | Unset = "any",
    statuses_logic: str | Unset = "any",
    player_counts_logic: str | Unset = "any",
    order_by: str | Unset = "name",
    order_dir: str | Unset = "asc",
    updated_after: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError]:
    """Get Roms

     Retrieve roms.

    Args:
        with_char_index (bool | Unset): Whether to get the char index. Default: True.
        with_filter_values (bool | Unset): Whether to return filter values. Default: True.
        search_term (None | str | Unset): Search term to filter roms.
        platform_ids (list[int] | None | Unset): Platform internal ids. Multiple values are
            allowed by repeating the parameter, and results that match any of the values will be
            returned.
        collection_id (int | None | Unset): Collection internal id.
        virtual_collection_id (None | str | Unset): Virtual collection internal id.
        smart_collection_id (int | None | Unset): Smart collection internal id.
        matched (bool | None | Unset): Whether the rom matched at least one metadata source.
        favorite (bool | None | Unset): Whether the rom is marked as favorite.
        duplicate (bool | None | Unset): Whether the rom is marked as duplicate.
        last_played (bool | None | Unset): Whether the rom has a last played value for the current
            user.
        playable (bool | None | Unset): Whether the rom is playable from the browser.
        missing (bool | None | Unset): Whether the rom is missing from the filesystem.
        has_ra (bool | None | Unset): Whether the rom has RetroAchievements data.
        verified (bool | None | Unset): Whether the rom is verified by Hasheous.
        group_by_meta_id (bool | Unset): Whether to group roms by metadata ID (IGDB / Moby /
            ScreenScraper / RetroAchievements / LaunchBox). Default: False.
        genres (list[str] | None | Unset): Associated genre. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        franchises (list[str] | None | Unset): Associated franchise. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        collections (list[str] | None | Unset): Associated collection. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        companies (list[str] | None | Unset): Associated company. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        age_ratings (list[str] | None | Unset): Associated age rating. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        statuses (list[str] | None | Unset): Game status, set by the current user. Multiple values
            are allowed by repeating the parameter, and results that match any of the values will be
            returned.
        regions (list[str] | None | Unset): Associated region tag. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        languages (list[str] | None | Unset): Associated language tag. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        player_counts (list[str] | None | Unset): Associated player count. Multiple values are
            allowed by repeating the parameter, and results that match any of the values will be
            returned.
        genres_logic (str | Unset): Logic operator for genres filter: 'any' (OR), 'all' (AND) or
            'none' (NOT). Default: 'any'.
        franchises_logic (str | Unset): Logic operator for franchises filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        collections_logic (str | Unset): Logic operator for collections filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        companies_logic (str | Unset): Logic operator for companies filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        age_ratings_logic (str | Unset): Logic operator for age ratings filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        regions_logic (str | Unset): Logic operator for regions filter: 'any' (OR), 'all' (AND) or
            'none' (NOT). Default: 'any'.
        languages_logic (str | Unset): Logic operator for languages filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        statuses_logic (str | Unset): Logic operator for statuses filter: 'any' (OR), 'all' (AND)
            or 'none' (NOT). Default: 'any'.
        player_counts_logic (str | Unset): Logic operator for player counts filter: 'any' (OR),
            'all' (AND) or 'none' (NOT). Default: 'any'.
        order_by (str | Unset): Field to order results by. Default: 'name'.
        order_dir (str | Unset): Order direction, either 'asc' or 'desc'. Default: 'asc'.
        updated_after (datetime.datetime | None | Unset): Filter roms updated after this datetime
            (ISO 8601 format with timezone information).
        limit (int | Unset): Page size limit Default: 50.
        offset (int | Unset): Page offset Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        with_char_index=with_char_index,
        with_filter_values=with_filter_values,
        search_term=search_term,
        platform_ids=platform_ids,
        collection_id=collection_id,
        virtual_collection_id=virtual_collection_id,
        smart_collection_id=smart_collection_id,
        matched=matched,
        favorite=favorite,
        duplicate=duplicate,
        last_played=last_played,
        playable=playable,
        missing=missing,
        has_ra=has_ra,
        verified=verified,
        group_by_meta_id=group_by_meta_id,
        genres=genres,
        franchises=franchises,
        collections=collections,
        companies=companies,
        age_ratings=age_ratings,
        statuses=statuses,
        regions=regions,
        languages=languages,
        player_counts=player_counts,
        genres_logic=genres_logic,
        franchises_logic=franchises_logic,
        collections_logic=collections_logic,
        companies_logic=companies_logic,
        age_ratings_logic=age_ratings_logic,
        regions_logic=regions_logic,
        languages_logic=languages_logic,
        statuses_logic=statuses_logic,
        player_counts_logic=player_counts_logic,
        order_by=order_by,
        order_dir=order_dir,
        updated_after=updated_after,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    with_char_index: bool | Unset = True,
    with_filter_values: bool | Unset = True,
    search_term: None | str | Unset = UNSET,
    platform_ids: list[int] | None | Unset = UNSET,
    collection_id: int | None | Unset = UNSET,
    virtual_collection_id: None | str | Unset = UNSET,
    smart_collection_id: int | None | Unset = UNSET,
    matched: bool | None | Unset = UNSET,
    favorite: bool | None | Unset = UNSET,
    duplicate: bool | None | Unset = UNSET,
    last_played: bool | None | Unset = UNSET,
    playable: bool | None | Unset = UNSET,
    missing: bool | None | Unset = UNSET,
    has_ra: bool | None | Unset = UNSET,
    verified: bool | None | Unset = UNSET,
    group_by_meta_id: bool | Unset = False,
    genres: list[str] | None | Unset = UNSET,
    franchises: list[str] | None | Unset = UNSET,
    collections: list[str] | None | Unset = UNSET,
    companies: list[str] | None | Unset = UNSET,
    age_ratings: list[str] | None | Unset = UNSET,
    statuses: list[str] | None | Unset = UNSET,
    regions: list[str] | None | Unset = UNSET,
    languages: list[str] | None | Unset = UNSET,
    player_counts: list[str] | None | Unset = UNSET,
    genres_logic: str | Unset = "any",
    franchises_logic: str | Unset = "any",
    collections_logic: str | Unset = "any",
    companies_logic: str | Unset = "any",
    age_ratings_logic: str | Unset = "any",
    regions_logic: str | Unset = "any",
    languages_logic: str | Unset = "any",
    statuses_logic: str | Unset = "any",
    player_counts_logic: str | Unset = "any",
    order_by: str | Unset = "name",
    order_dir: str | Unset = "asc",
    updated_after: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError | None:
    """Get Roms

     Retrieve roms.

    Args:
        with_char_index (bool | Unset): Whether to get the char index. Default: True.
        with_filter_values (bool | Unset): Whether to return filter values. Default: True.
        search_term (None | str | Unset): Search term to filter roms.
        platform_ids (list[int] | None | Unset): Platform internal ids. Multiple values are
            allowed by repeating the parameter, and results that match any of the values will be
            returned.
        collection_id (int | None | Unset): Collection internal id.
        virtual_collection_id (None | str | Unset): Virtual collection internal id.
        smart_collection_id (int | None | Unset): Smart collection internal id.
        matched (bool | None | Unset): Whether the rom matched at least one metadata source.
        favorite (bool | None | Unset): Whether the rom is marked as favorite.
        duplicate (bool | None | Unset): Whether the rom is marked as duplicate.
        last_played (bool | None | Unset): Whether the rom has a last played value for the current
            user.
        playable (bool | None | Unset): Whether the rom is playable from the browser.
        missing (bool | None | Unset): Whether the rom is missing from the filesystem.
        has_ra (bool | None | Unset): Whether the rom has RetroAchievements data.
        verified (bool | None | Unset): Whether the rom is verified by Hasheous.
        group_by_meta_id (bool | Unset): Whether to group roms by metadata ID (IGDB / Moby /
            ScreenScraper / RetroAchievements / LaunchBox). Default: False.
        genres (list[str] | None | Unset): Associated genre. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        franchises (list[str] | None | Unset): Associated franchise. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        collections (list[str] | None | Unset): Associated collection. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        companies (list[str] | None | Unset): Associated company. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        age_ratings (list[str] | None | Unset): Associated age rating. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        statuses (list[str] | None | Unset): Game status, set by the current user. Multiple values
            are allowed by repeating the parameter, and results that match any of the values will be
            returned.
        regions (list[str] | None | Unset): Associated region tag. Multiple values are allowed by
            repeating the parameter, and results that match any of the values will be returned.
        languages (list[str] | None | Unset): Associated language tag. Multiple values are allowed
            by repeating the parameter, and results that match any of the values will be returned.
        player_counts (list[str] | None | Unset): Associated player count. Multiple values are
            allowed by repeating the parameter, and results that match any of the values will be
            returned.
        genres_logic (str | Unset): Logic operator for genres filter: 'any' (OR), 'all' (AND) or
            'none' (NOT). Default: 'any'.
        franchises_logic (str | Unset): Logic operator for franchises filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        collections_logic (str | Unset): Logic operator for collections filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        companies_logic (str | Unset): Logic operator for companies filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        age_ratings_logic (str | Unset): Logic operator for age ratings filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        regions_logic (str | Unset): Logic operator for regions filter: 'any' (OR), 'all' (AND) or
            'none' (NOT). Default: 'any'.
        languages_logic (str | Unset): Logic operator for languages filter: 'any' (OR), 'all'
            (AND) or 'none' (NOT). Default: 'any'.
        statuses_logic (str | Unset): Logic operator for statuses filter: 'any' (OR), 'all' (AND)
            or 'none' (NOT). Default: 'any'.
        player_counts_logic (str | Unset): Logic operator for player counts filter: 'any' (OR),
            'all' (AND) or 'none' (NOT). Default: 'any'.
        order_by (str | Unset): Field to order results by. Default: 'name'.
        order_dir (str | Unset): Order direction, either 'asc' or 'desc'. Default: 'asc'.
        updated_after (datetime.datetime | None | Unset): Filter roms updated after this datetime
            (ISO 8601 format with timezone information).
        limit (int | Unset): Page size limit Default: 50.
        offset (int | Unset): Page offset Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomLimitOffsetPageSimpleRomSchema | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            with_char_index=with_char_index,
            with_filter_values=with_filter_values,
            search_term=search_term,
            platform_ids=platform_ids,
            collection_id=collection_id,
            virtual_collection_id=virtual_collection_id,
            smart_collection_id=smart_collection_id,
            matched=matched,
            favorite=favorite,
            duplicate=duplicate,
            last_played=last_played,
            playable=playable,
            missing=missing,
            has_ra=has_ra,
            verified=verified,
            group_by_meta_id=group_by_meta_id,
            genres=genres,
            franchises=franchises,
            collections=collections,
            companies=companies,
            age_ratings=age_ratings,
            statuses=statuses,
            regions=regions,
            languages=languages,
            player_counts=player_counts,
            genres_logic=genres_logic,
            franchises_logic=franchises_logic,
            collections_logic=collections_logic,
            companies_logic=companies_logic,
            age_ratings_logic=age_ratings_logic,
            regions_logic=regions_logic,
            languages_logic=languages_logic,
            statuses_logic=statuses_logic,
            player_counts_logic=player_counts_logic,
            order_by=order_by,
            order_dir=order_dir,
            updated_after=updated_after,
            limit=limit,
            offset=offset,
        )
    ).parsed
