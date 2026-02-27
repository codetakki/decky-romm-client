from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_update_collection_api_collections_id_put import BodyUpdateCollectionApiCollectionsIdPut
from ...models.collection_schema import CollectionSchema
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: BodyUpdateCollectionApiCollectionsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    is_public: bool | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["remove_cover"] = remove_cover

    json_is_public: bool | None | Unset
    if isinstance(is_public, Unset):
        json_is_public = UNSET
    else:
        json_is_public = is_public
    params["is_public"] = json_is_public

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/collections/{id}".format(
            id=quote(str(id), safe=""),
        ),
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateCollectionApiCollectionsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    is_public: bool | None | Unset = UNSET,
) -> Response[CollectionSchema | HTTPValidationError]:
    """Update Collection

     Update collection endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        CollectionSchema: Updated collection

    Args:
        id (int):
        remove_cover (bool | Unset):  Default: False.
        is_public (bool | None | Unset):
        body (BodyUpdateCollectionApiCollectionsIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        remove_cover=remove_cover,
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
    body: BodyUpdateCollectionApiCollectionsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    is_public: bool | None | Unset = UNSET,
) -> CollectionSchema | HTTPValidationError | None:
    """Update Collection

     Update collection endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        CollectionSchema: Updated collection

    Args:
        id (int):
        remove_cover (bool | Unset):  Default: False.
        is_public (bool | None | Unset):
        body (BodyUpdateCollectionApiCollectionsIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionSchema | HTTPValidationError
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        remove_cover=remove_cover,
        is_public=is_public,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateCollectionApiCollectionsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    is_public: bool | None | Unset = UNSET,
) -> Response[CollectionSchema | HTTPValidationError]:
    """Update Collection

     Update collection endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        CollectionSchema: Updated collection

    Args:
        id (int):
        remove_cover (bool | Unset):  Default: False.
        is_public (bool | None | Unset):
        body (BodyUpdateCollectionApiCollectionsIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CollectionSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        remove_cover=remove_cover,
        is_public=is_public,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateCollectionApiCollectionsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    is_public: bool | None | Unset = UNSET,
) -> CollectionSchema | HTTPValidationError | None:
    """Update Collection

     Update collection endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        CollectionSchema: Updated collection

    Args:
        id (int):
        remove_cover (bool | Unset):  Default: False.
        is_public (bool | None | Unset):
        body (BodyUpdateCollectionApiCollectionsIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CollectionSchema | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            remove_cover=remove_cover,
            is_public=is_public,
        )
    ).parsed
