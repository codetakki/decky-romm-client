from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_rom_note_api_roms_id_notes_post_note_data import CreateRomNoteApiRomsIdNotesPostNoteData
from ...models.http_validation_error import HTTPValidationError
from ...models.user_note_schema import UserNoteSchema
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: CreateRomNoteApiRomsIdNotesPostNoteData,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/roms/{id}/notes".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | UserNoteSchema | None:
    if response.status_code == 200:
        response_200 = UserNoteSchema.from_dict(response.json())

        return response_200

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
) -> Response[Any | HTTPValidationError | UserNoteSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: CreateRomNoteApiRomsIdNotesPostNoteData,
) -> Response[Any | HTTPValidationError | UserNoteSchema]:
    """Create Rom Note

     Create a new note for a ROM.

    Args:
        id (int): Rom internal id.
        body (CreateRomNoteApiRomsIdNotesPostNoteData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | UserNoteSchema]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: CreateRomNoteApiRomsIdNotesPostNoteData,
) -> Any | HTTPValidationError | UserNoteSchema | None:
    """Create Rom Note

     Create a new note for a ROM.

    Args:
        id (int): Rom internal id.
        body (CreateRomNoteApiRomsIdNotesPostNoteData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | UserNoteSchema
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: CreateRomNoteApiRomsIdNotesPostNoteData,
) -> Response[Any | HTTPValidationError | UserNoteSchema]:
    """Create Rom Note

     Create a new note for a ROM.

    Args:
        id (int): Rom internal id.
        body (CreateRomNoteApiRomsIdNotesPostNoteData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | UserNoteSchema]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: CreateRomNoteApiRomsIdNotesPostNoteData,
) -> Any | HTTPValidationError | UserNoteSchema | None:
    """Create Rom Note

     Create a new note for a ROM.

    Args:
        id (int): Rom internal id.
        body (CreateRomNoteApiRomsIdNotesPostNoteData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | UserNoteSchema
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
