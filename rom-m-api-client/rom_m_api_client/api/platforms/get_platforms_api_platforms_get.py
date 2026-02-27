import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.platform_schema import PlatformSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    updated_after: datetime.datetime | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_updated_after: None | str | Unset
    if isinstance(updated_after, Unset):
        json_updated_after = UNSET
    elif isinstance(updated_after, datetime.datetime):
        json_updated_after = updated_after.isoformat()
    else:
        json_updated_after = updated_after
    params["updated_after"] = json_updated_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platforms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[PlatformSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PlatformSchema.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[PlatformSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    updated_after: datetime.datetime | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[PlatformSchema]]:
    """Get Platforms

     Retrieve platforms.

    Args:
        updated_after (datetime.datetime | None | Unset): Filter platforms updated after this
            datetime (ISO 8601 format with timezone information).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[PlatformSchema]]
    """

    kwargs = _get_kwargs(
        updated_after=updated_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    updated_after: datetime.datetime | None | Unset = UNSET,
) -> HTTPValidationError | list[PlatformSchema] | None:
    """Get Platforms

     Retrieve platforms.

    Args:
        updated_after (datetime.datetime | None | Unset): Filter platforms updated after this
            datetime (ISO 8601 format with timezone information).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[PlatformSchema]
    """

    return sync_detailed(
        client=client,
        updated_after=updated_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    updated_after: datetime.datetime | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[PlatformSchema]]:
    """Get Platforms

     Retrieve platforms.

    Args:
        updated_after (datetime.datetime | None | Unset): Filter platforms updated after this
            datetime (ISO 8601 format with timezone information).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[PlatformSchema]]
    """

    kwargs = _get_kwargs(
        updated_after=updated_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    updated_after: datetime.datetime | None | Unset = UNSET,
) -> HTTPValidationError | list[PlatformSchema] | None:
    """Get Platforms

     Retrieve platforms.

    Args:
        updated_after (datetime.datetime | None | Unset): Filter platforms updated after this
            datetime (ISO 8601 format with timezone information).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[PlatformSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            updated_after=updated_after,
        )
    ).parsed
