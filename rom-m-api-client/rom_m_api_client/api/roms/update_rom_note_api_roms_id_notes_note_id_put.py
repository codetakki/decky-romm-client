from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.update_rom_note_api_roms_id_notes_note_id_put_note_data import (
    UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData,
)
from ...models.user_note_schema import UserNoteSchema
from ...types import Response


def _get_kwargs(
    id: int,
    note_id: int,
    *,
    body: UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/roms/{id}/notes/{note_id}".format(
            id=quote(str(id), safe=""),
            note_id=quote(str(note_id), safe=""),
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
    note_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData,
) -> Response[Any | HTTPValidationError | UserNoteSchema]:
    """Update Rom Note

     Update a ROM note.

    Args:
        id (int): Rom internal id.
        note_id (int): Note id.
        body (UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | UserNoteSchema]
    """

    kwargs = _get_kwargs(
        id=id,
        note_id=note_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    note_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData,
) -> Any | HTTPValidationError | UserNoteSchema | None:
    """Update Rom Note

     Update a ROM note.

    Args:
        id (int): Rom internal id.
        note_id (int): Note id.
        body (UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | UserNoteSchema
    """

    return sync_detailed(
        id=id,
        note_id=note_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    note_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData,
) -> Response[Any | HTTPValidationError | UserNoteSchema]:
    """Update Rom Note

     Update a ROM note.

    Args:
        id (int): Rom internal id.
        note_id (int): Note id.
        body (UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | UserNoteSchema]
    """

    kwargs = _get_kwargs(
        id=id,
        note_id=note_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    note_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData,
) -> Any | HTTPValidationError | UserNoteSchema | None:
    """Update Rom Note

     Update a ROM note.

    Args:
        id (int): Rom internal id.
        note_id (int): Note id.
        body (UpdateRomNoteApiRomsIdNotesNoteIdPutNoteData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | UserNoteSchema
    """

    return (
        await asyncio_detailed(
            id=id,
            note_id=note_id,
            client=client,
            body=body,
        )
    ).parsed
