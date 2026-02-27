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
    rom_id: int,
    emulator: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["rom_id"] = rom_id

    json_emulator: None | str | Unset
    if isinstance(emulator, Unset):
        json_emulator = UNSET
    else:
        json_emulator = emulator
    params["emulator"] = json_emulator

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/states",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | StateSchema | None:
    if response.status_code == 200:
        response_200 = StateSchema.from_dict(response.json())

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
) -> Response[HTTPValidationError | StateSchema]:
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
    emulator: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | StateSchema]:
    """Add State

    Args:
        rom_id (int):
        emulator (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StateSchema]
    """

    kwargs = _get_kwargs(
        rom_id=rom_id,
        emulator=emulator,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    rom_id: int,
    emulator: None | str | Unset = UNSET,
) -> HTTPValidationError | StateSchema | None:
    """Add State

    Args:
        rom_id (int):
        emulator (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StateSchema
    """

    return sync_detailed(
        client=client,
        rom_id=rom_id,
        emulator=emulator,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    rom_id: int,
    emulator: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | StateSchema]:
    """Add State

    Args:
        rom_id (int):
        emulator (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StateSchema]
    """

    kwargs = _get_kwargs(
        rom_id=rom_id,
        emulator=emulator,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    rom_id: int,
    emulator: None | str | Unset = UNSET,
) -> HTTPValidationError | StateSchema | None:
    """Add State

    Args:
        rom_id (int):
        emulator (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StateSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            rom_id=rom_id,
            emulator=emulator,
        )
    ).parsed
