from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_rooms_api_netplay_list_get_response_get_rooms_api_netplay_list_get import (
    GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    game_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["game_id"] = game_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/netplay/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet.from_dict(response.json())

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
) -> Response[GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    game_id: str,
) -> Response[GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError]:
    """Get Rooms

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    game_id: str,
) -> GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError | None:
    """Get Rooms

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        game_id=game_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    game_id: str,
) -> Response[GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError]:
    """Get Rooms

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    game_id: str,
) -> GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError | None:
    """Get Rooms

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRoomsApiNetplayListGetResponseGetRoomsApiNetplayListGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            game_id=game_id,
        )
    ).parsed
