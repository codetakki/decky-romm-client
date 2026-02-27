from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.virtual_collection_schema import VirtualCollectionSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: str,
    limit: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/collections/virtual",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[VirtualCollectionSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VirtualCollectionSchema.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[VirtualCollectionSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: str,
    limit: int | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[VirtualCollectionSchema]]:
    """Get Virtual Collections

     Get virtual collections endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        list[VirtualCollectionSchema]: List of virtual collections

    Args:
        type_ (str):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[VirtualCollectionSchema]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: str,
    limit: int | None | Unset = UNSET,
) -> HTTPValidationError | list[VirtualCollectionSchema] | None:
    """Get Virtual Collections

     Get virtual collections endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        list[VirtualCollectionSchema]: List of virtual collections

    Args:
        type_ (str):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[VirtualCollectionSchema]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: str,
    limit: int | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[VirtualCollectionSchema]]:
    """Get Virtual Collections

     Get virtual collections endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        list[VirtualCollectionSchema]: List of virtual collections

    Args:
        type_ (str):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[VirtualCollectionSchema]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: str,
    limit: int | None | Unset = UNSET,
) -> HTTPValidationError | list[VirtualCollectionSchema] | None:
    """Get Virtual Collections

     Get virtual collections endpoint

    Args:
        request (Request): Fastapi Request object

    Returns:
        list[VirtualCollectionSchema]: List of virtual collections

    Args:
        type_ (str):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[VirtualCollectionSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            limit=limit,
        )
    ).parsed
