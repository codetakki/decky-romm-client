from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.search_rom_schema import SearchRomSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rom_id: int,
    search_term: None | str | Unset = UNSET,
    search_by: str | Unset = "name",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["rom_id"] = rom_id

    json_search_term: None | str | Unset
    if isinstance(search_term, Unset):
        json_search_term = UNSET
    else:
        json_search_term = search_term
    params["search_term"] = json_search_term

    params["search_by"] = search_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/search/roms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[SearchRomSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SearchRomSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[SearchRomSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    rom_id: int,
    search_term: None | str | Unset = UNSET,
    search_by: str | Unset = "name",
) -> Response[HTTPValidationError | list[SearchRomSchema]]:
    r"""Search Rom

     Search for rom in metadata providers

    Args:
        request (Request): FastAPI request
        rom_id (int): Rom ID
        source (str): Source of the rom
        search_term (str, optional): Search term. Defaults to None.
        search_by (str, optional): Search by name or ID. Defaults to \"name\".
        search_extended (bool, optional): Search extended info. Defaults to False.

    Returns:
        list[SearchRomSchema]: List of matched roms

    Args:
        rom_id (int):
        search_term (None | str | Unset):
        search_by (str | Unset):  Default: 'name'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SearchRomSchema]]
    """

    kwargs = _get_kwargs(
        rom_id=rom_id,
        search_term=search_term,
        search_by=search_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    rom_id: int,
    search_term: None | str | Unset = UNSET,
    search_by: str | Unset = "name",
) -> HTTPValidationError | list[SearchRomSchema] | None:
    r"""Search Rom

     Search for rom in metadata providers

    Args:
        request (Request): FastAPI request
        rom_id (int): Rom ID
        source (str): Source of the rom
        search_term (str, optional): Search term. Defaults to None.
        search_by (str, optional): Search by name or ID. Defaults to \"name\".
        search_extended (bool, optional): Search extended info. Defaults to False.

    Returns:
        list[SearchRomSchema]: List of matched roms

    Args:
        rom_id (int):
        search_term (None | str | Unset):
        search_by (str | Unset):  Default: 'name'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SearchRomSchema]
    """

    return sync_detailed(
        client=client,
        rom_id=rom_id,
        search_term=search_term,
        search_by=search_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    rom_id: int,
    search_term: None | str | Unset = UNSET,
    search_by: str | Unset = "name",
) -> Response[HTTPValidationError | list[SearchRomSchema]]:
    r"""Search Rom

     Search for rom in metadata providers

    Args:
        request (Request): FastAPI request
        rom_id (int): Rom ID
        source (str): Source of the rom
        search_term (str, optional): Search term. Defaults to None.
        search_by (str, optional): Search by name or ID. Defaults to \"name\".
        search_extended (bool, optional): Search extended info. Defaults to False.

    Returns:
        list[SearchRomSchema]: List of matched roms

    Args:
        rom_id (int):
        search_term (None | str | Unset):
        search_by (str | Unset):  Default: 'name'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SearchRomSchema]]
    """

    kwargs = _get_kwargs(
        rom_id=rom_id,
        search_term=search_term,
        search_by=search_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    rom_id: int,
    search_term: None | str | Unset = UNSET,
    search_by: str | Unset = "name",
) -> HTTPValidationError | list[SearchRomSchema] | None:
    r"""Search Rom

     Search for rom in metadata providers

    Args:
        request (Request): FastAPI request
        rom_id (int): Rom ID
        source (str): Source of the rom
        search_term (str, optional): Search term. Defaults to None.
        search_by (str, optional): Search by name or ID. Defaults to \"name\".
        search_extended (bool, optional): Search extended info. Defaults to False.

    Returns:
        list[SearchRomSchema]: List of matched roms

    Args:
        rom_id (int):
        search_term (None | str | Unset):
        search_by (str | Unset):  Default: 'name'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SearchRomSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            rom_id=rom_id,
            search_term=search_term,
            search_by=search_by,
        )
    ).parsed
