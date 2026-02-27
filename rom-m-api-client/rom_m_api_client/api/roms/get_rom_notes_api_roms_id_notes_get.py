from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_note_schema import UserNoteSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    public_only: bool | Unset = False,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["public_only"] = public_only

    params["search"] = search

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/roms/{id}/notes".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[UserNoteSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserNoteSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | HTTPValidationError | list[UserNoteSchema]]:
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
    public_only: bool | Unset = False,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[UserNoteSchema]]:
    """Get Rom Notes

     Get all notes for a ROM.

    Args:
        id (int): Rom internal id.
        public_only (bool | Unset): Only return public notes Default: False.
        search (str | Unset): Search notes by title or content
        tags (list[str] | Unset): Filter by tags

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[UserNoteSchema]]
    """

    kwargs = _get_kwargs(
        id=id,
        public_only=public_only,
        search=search,
        tags=tags,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    public_only: bool | Unset = False,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
) -> Any | HTTPValidationError | list[UserNoteSchema] | None:
    """Get Rom Notes

     Get all notes for a ROM.

    Args:
        id (int): Rom internal id.
        public_only (bool | Unset): Only return public notes Default: False.
        search (str | Unset): Search notes by title or content
        tags (list[str] | Unset): Filter by tags

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[UserNoteSchema]
    """

    return sync_detailed(
        id=id,
        client=client,
        public_only=public_only,
        search=search,
        tags=tags,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    public_only: bool | Unset = False,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[UserNoteSchema]]:
    """Get Rom Notes

     Get all notes for a ROM.

    Args:
        id (int): Rom internal id.
        public_only (bool | Unset): Only return public notes Default: False.
        search (str | Unset): Search notes by title or content
        tags (list[str] | Unset): Filter by tags

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[UserNoteSchema]]
    """

    kwargs = _get_kwargs(
        id=id,
        public_only=public_only,
        search=search,
        tags=tags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    public_only: bool | Unset = False,
    search: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
) -> Any | HTTPValidationError | list[UserNoteSchema] | None:
    """Get Rom Notes

     Get all notes for a ROM.

    Args:
        id (int): Rom internal id.
        public_only (bool | Unset): Only return public notes Default: False.
        search (str | Unset): Search notes by title or content
        tags (list[str] | Unset): Filter by tags

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[UserNoteSchema]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            public_only=public_only,
            search=search,
            tags=tags,
        )
    ).parsed
