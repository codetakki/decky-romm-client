from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.state_schema import StateSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rom_id: int | None | Unset = UNSET,
    platform_id: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_rom_id: int | None | Unset
    if isinstance(rom_id, Unset):
        json_rom_id = UNSET
    else:
        json_rom_id = rom_id
    params["rom_id"] = json_rom_id

    json_platform_id: int | None | Unset
    if isinstance(platform_id, Unset):
        json_platform_id = UNSET
    else:
        json_platform_id = platform_id
    params["platform_id"] = json_platform_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/states",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[StateSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StateSchema.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[StateSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    rom_id: int | None | Unset = UNSET,
    platform_id: int | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[StateSchema]]:
    """Get States

    Args:
        rom_id (int | None | Unset):
        platform_id (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[StateSchema]]
    """

    kwargs = _get_kwargs(
        rom_id=rom_id,
        platform_id=platform_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    rom_id: int | None | Unset = UNSET,
    platform_id: int | None | Unset = UNSET,
) -> HTTPValidationError | list[StateSchema] | None:
    """Get States

    Args:
        rom_id (int | None | Unset):
        platform_id (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[StateSchema]
    """

    return sync_detailed(
        client=client,
        rom_id=rom_id,
        platform_id=platform_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    rom_id: int | None | Unset = UNSET,
    platform_id: int | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[StateSchema]]:
    """Get States

    Args:
        rom_id (int | None | Unset):
        platform_id (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[StateSchema]]
    """

    kwargs = _get_kwargs(
        rom_id=rom_id,
        platform_id=platform_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    rom_id: int | None | Unset = UNSET,
    platform_id: int | None | Unset = UNSET,
) -> HTTPValidationError | list[StateSchema] | None:
    """Get States

    Args:
        rom_id (int | None | Unset):
        platform_id (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[StateSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            rom_id=rom_id,
            platform_id=platform_id,
        )
    ).parsed
