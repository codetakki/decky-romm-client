from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_add_collection_api_collections_post import BodyAddCollectionApiCollectionsPost
from ...models.collection_schema import CollectionSchema
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyAddCollectionApiCollectionsPost | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_is_public: bool | None | Unset
    if isinstance(is_public, Unset):
        json_is_public = UNSET
    else:
        json_is_public = is_public
    params["is_public"] = json_is_public

    json_is_favorite: bool | None | Unset
    if isinstance(is_favorite, Unset):
        json_is_favorite = UNSET
    else:
        json_is_favorite = is_favorite
    params["is_favorite"] = json_is_favorite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/collections",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CollectionSchema | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CollectionSchema.from_dict(response.json())

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
) -> Response[CollectionSchema | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyAddCollectionApiCollectionsPost | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> Response[CollectionSchema | HTTPValidationError]:
    """Add Collection

     Create collection endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        CollectionSchema: Just created collection

    Args:
        is_public (bool | None | Unset):
        is_favorite (bool | None | Unset):
        body (BodyAddCollectionApiCollectionsPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        is_public=is_public,
        is_favorite=is_favorite,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyAddCollectionApiCollectionsPost | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> CollectionSchema | HTTPValidationError | None:
    """Add Collection

     Create collection endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        CollectionSchema: Just created collection

    Args:
        is_public (bool | None | Unset):
        is_favorite (bool | None | Unset):
        body (BodyAddCollectionApiCollectionsPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionSchema | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        is_public=is_public,
        is_favorite=is_favorite,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyAddCollectionApiCollectionsPost | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> Response[CollectionSchema | HTTPValidationError]:
    """Add Collection

     Create collection endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        CollectionSchema: Just created collection

    Args:
        is_public (bool | None | Unset):
        is_favorite (bool | None | Unset):
        body (BodyAddCollectionApiCollectionsPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        is_public=is_public,
        is_favorite=is_favorite,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyAddCollectionApiCollectionsPost | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> CollectionSchema | HTTPValidationError | None:
    """Add Collection

     Create collection endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        CollectionSchema: Just created collection

    Args:
        is_public (bool | None | Unset):
        is_favorite (bool | None | Unset):
        body (BodyAddCollectionApiCollectionsPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionSchema | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            is_public=is_public,
            is_favorite=is_favorite,
        )
    ).parsed
