from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detailed_rom_schema import DetailedRomSchema
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    igdb_id: int | None | Unset = UNSET,
    moby_id: int | None | Unset = UNSET,
    ss_id: int | None | Unset = UNSET,
    ra_id: int | None | Unset = UNSET,
    launchbox_id: int | None | Unset = UNSET,
    hasheous_id: int | None | Unset = UNSET,
    tgdb_id: int | None | Unset = UNSET,
    flashpoint_id: None | str | Unset = UNSET,
    hltb_id: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_igdb_id: int | None | Unset
    if isinstance(igdb_id, Unset):
        json_igdb_id = UNSET
    else:
        json_igdb_id = igdb_id
    params["igdb_id"] = json_igdb_id

    json_moby_id: int | None | Unset
    if isinstance(moby_id, Unset):
        json_moby_id = UNSET
    else:
        json_moby_id = moby_id
    params["moby_id"] = json_moby_id

    json_ss_id: int | None | Unset
    if isinstance(ss_id, Unset):
        json_ss_id = UNSET
    else:
        json_ss_id = ss_id
    params["ss_id"] = json_ss_id

    json_ra_id: int | None | Unset
    if isinstance(ra_id, Unset):
        json_ra_id = UNSET
    else:
        json_ra_id = ra_id
    params["ra_id"] = json_ra_id

    json_launchbox_id: int | None | Unset
    if isinstance(launchbox_id, Unset):
        json_launchbox_id = UNSET
    else:
        json_launchbox_id = launchbox_id
    params["launchbox_id"] = json_launchbox_id

    json_hasheous_id: int | None | Unset
    if isinstance(hasheous_id, Unset):
        json_hasheous_id = UNSET
    else:
        json_hasheous_id = hasheous_id
    params["hasheous_id"] = json_hasheous_id

    json_tgdb_id: int | None | Unset
    if isinstance(tgdb_id, Unset):
        json_tgdb_id = UNSET
    else:
        json_tgdb_id = tgdb_id
    params["tgdb_id"] = json_tgdb_id

    json_flashpoint_id: None | str | Unset
    if isinstance(flashpoint_id, Unset):
        json_flashpoint_id = UNSET
    else:
        json_flashpoint_id = flashpoint_id
    params["flashpoint_id"] = json_flashpoint_id

    json_hltb_id: int | None | Unset
    if isinstance(hltb_id, Unset):
        json_hltb_id = UNSET
    else:
        json_hltb_id = hltb_id
    params["hltb_id"] = json_hltb_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/roms/by-metadata-provider",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DetailedRomSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    igdb_id: int | None | Unset = UNSET,
    moby_id: int | None | Unset = UNSET,
    ss_id: int | None | Unset = UNSET,
    ra_id: int | None | Unset = UNSET,
    launchbox_id: int | None | Unset = UNSET,
    hasheous_id: int | None | Unset = UNSET,
    tgdb_id: int | None | Unset = UNSET,
    flashpoint_id: None | str | Unset = UNSET,
    hltb_id: int | None | Unset = UNSET,
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
    """Get Rom By Metadata Provider

     Retrieve a rom by metadata ID.

    Args:
        igdb_id (int | None | Unset): IGDB ID to search by
        moby_id (int | None | Unset): MobyGames ID to search by
        ss_id (int | None | Unset): ScreenScraper ID to search by
        ra_id (int | None | Unset): RetroAchievements ID to search by
        launchbox_id (int | None | Unset): LaunchBox ID to search by
        hasheous_id (int | None | Unset): Hasheous ID to search by
        tgdb_id (int | None | Unset): TGDB ID to search by
        flashpoint_id (None | str | Unset): Flashpoint ID to search by
        hltb_id (int | None | Unset): HLTB ID to search by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DetailedRomSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        igdb_id=igdb_id,
        moby_id=moby_id,
        ss_id=ss_id,
        ra_id=ra_id,
        launchbox_id=launchbox_id,
        hasheous_id=hasheous_id,
        tgdb_id=tgdb_id,
        flashpoint_id=flashpoint_id,
        hltb_id=hltb_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    igdb_id: int | None | Unset = UNSET,
    moby_id: int | None | Unset = UNSET,
    ss_id: int | None | Unset = UNSET,
    ra_id: int | None | Unset = UNSET,
    launchbox_id: int | None | Unset = UNSET,
    hasheous_id: int | None | Unset = UNSET,
    tgdb_id: int | None | Unset = UNSET,
    flashpoint_id: None | str | Unset = UNSET,
    hltb_id: int | None | Unset = UNSET,
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    """Get Rom By Metadata Provider

     Retrieve a rom by metadata ID.

    Args:
        igdb_id (int | None | Unset): IGDB ID to search by
        moby_id (int | None | Unset): MobyGames ID to search by
        ss_id (int | None | Unset): ScreenScraper ID to search by
        ra_id (int | None | Unset): RetroAchievements ID to search by
        launchbox_id (int | None | Unset): LaunchBox ID to search by
        hasheous_id (int | None | Unset): Hasheous ID to search by
        tgdb_id (int | None | Unset): TGDB ID to search by
        flashpoint_id (None | str | Unset): Flashpoint ID to search by
        hltb_id (int | None | Unset): HLTB ID to search by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DetailedRomSchema | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        igdb_id=igdb_id,
        moby_id=moby_id,
        ss_id=ss_id,
        ra_id=ra_id,
        launchbox_id=launchbox_id,
        hasheous_id=hasheous_id,
        tgdb_id=tgdb_id,
        flashpoint_id=flashpoint_id,
        hltb_id=hltb_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    igdb_id: int | None | Unset = UNSET,
    moby_id: int | None | Unset = UNSET,
    ss_id: int | None | Unset = UNSET,
    ra_id: int | None | Unset = UNSET,
    launchbox_id: int | None | Unset = UNSET,
    hasheous_id: int | None | Unset = UNSET,
    tgdb_id: int | None | Unset = UNSET,
    flashpoint_id: None | str | Unset = UNSET,
    hltb_id: int | None | Unset = UNSET,
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
    """Get Rom By Metadata Provider

     Retrieve a rom by metadata ID.

    Args:
        igdb_id (int | None | Unset): IGDB ID to search by
        moby_id (int | None | Unset): MobyGames ID to search by
        ss_id (int | None | Unset): ScreenScraper ID to search by
        ra_id (int | None | Unset): RetroAchievements ID to search by
        launchbox_id (int | None | Unset): LaunchBox ID to search by
        hasheous_id (int | None | Unset): Hasheous ID to search by
        tgdb_id (int | None | Unset): TGDB ID to search by
        flashpoint_id (None | str | Unset): Flashpoint ID to search by
        hltb_id (int | None | Unset): HLTB ID to search by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DetailedRomSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        igdb_id=igdb_id,
        moby_id=moby_id,
        ss_id=ss_id,
        ra_id=ra_id,
        launchbox_id=launchbox_id,
        hasheous_id=hasheous_id,
        tgdb_id=tgdb_id,
        flashpoint_id=flashpoint_id,
        hltb_id=hltb_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    igdb_id: int | None | Unset = UNSET,
    moby_id: int | None | Unset = UNSET,
    ss_id: int | None | Unset = UNSET,
    ra_id: int | None | Unset = UNSET,
    launchbox_id: int | None | Unset = UNSET,
    hasheous_id: int | None | Unset = UNSET,
    tgdb_id: int | None | Unset = UNSET,
    flashpoint_id: None | str | Unset = UNSET,
    hltb_id: int | None | Unset = UNSET,
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    """Get Rom By Metadata Provider

     Retrieve a rom by metadata ID.

    Args:
        igdb_id (int | None | Unset): IGDB ID to search by
        moby_id (int | None | Unset): MobyGames ID to search by
        ss_id (int | None | Unset): ScreenScraper ID to search by
        ra_id (int | None | Unset): RetroAchievements ID to search by
        launchbox_id (int | None | Unset): LaunchBox ID to search by
        hasheous_id (int | None | Unset): Hasheous ID to search by
        tgdb_id (int | None | Unset): TGDB ID to search by
        flashpoint_id (None | str | Unset): Flashpoint ID to search by
        hltb_id (int | None | Unset): HLTB ID to search by

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DetailedRomSchema | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            igdb_id=igdb_id,
            moby_id=moby_id,
            ss_id=ss_id,
            ra_id=ra_id,
            launchbox_id=launchbox_id,
            hasheous_id=hasheous_id,
            tgdb_id=tgdb_id,
            flashpoint_id=flashpoint_id,
            hltb_id=hltb_id,
        )
    ).parsed
