from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.smart_collection_schema import SmartCollectionSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    is_public: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_is_public: bool | None | Unset
    if isinstance(is_public, Unset):
        json_is_public = UNSET
    else:
        json_is_public = is_public
    params["is_public"] = json_is_public

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/collections/smart/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SmartCollectionSchema | None:
    if response.status_code == 200:
        response_200 = SmartCollectionSchema.from_dict(response.json())

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
) -> Response[HTTPValidationError | SmartCollectionSchema]:
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
    is_public: bool | None | Unset = UNSET,
) -> Response[HTTPValidationError | SmartCollectionSchema]:
    """Update Smart Collection

     Update smart collection endpoint

    Args:
        request (Request): Fastapi Request object
        id (int): Smart collection id

    Returns:
        SmartCollectionSchema: Updated smart collection

    Args:
        id (int):
        is_public (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SmartCollectionSchema]
    """

    kwargs = _get_kwargs(
        id=id,
        is_public=is_public,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    is_public: bool | None | Unset = UNSET,
) -> HTTPValidationError | SmartCollectionSchema | None:
    """Update Smart Collection

     Update smart collection endpoint

    Args:
        request (Request): Fastapi Request object
        id (int): Smart collection id

    Returns:
        SmartCollectionSchema: Updated smart collection

    Args:
        id (int):
        is_public (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SmartCollectionSchema
    """

    return sync_detailed(
        id=id,
        client=client,
        is_public=is_public,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    is_public: bool | None | Unset = UNSET,
) -> Response[HTTPValidationError | SmartCollectionSchema]:
    """Update Smart Collection

     Update smart collection endpoint

    Args:
        request (Request): Fastapi Request object
        id (int): Smart collection id

    Returns:
        SmartCollectionSchema: Updated smart collection

    Args:
        id (int):
        is_public (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SmartCollectionSchema]
    """

    kwargs = _get_kwargs(
        id=id,
        is_public=is_public,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    is_public: bool | None | Unset = UNSET,
) -> HTTPValidationError | SmartCollectionSchema | None:
    """Update Smart Collection

     Update smart collection endpoint

    Args:
        request (Request): Fastapi Request object
        id (int): Smart collection id

    Returns:
        SmartCollectionSchema: Updated smart collection

    Args:
        id (int):
        is_public (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SmartCollectionSchema
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            is_public=is_public,
        )
    ).parsed
