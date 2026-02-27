from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    source: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/heartbeat/metadata/{source}".format(
            source=quote(str(source), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
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
) -> Response[HTTPValidationError | bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | bool]:
    """Metadata Heartbeat

     Endpoint to return the heartbeat of the metadata sources

    Args:
        source (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | bool]
    """

    kwargs = _get_kwargs(
        source=source,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | bool | None:
    """Metadata Heartbeat

     Endpoint to return the heartbeat of the metadata sources

    Args:
        source (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | bool
    """

    return sync_detailed(
        source=source,
        client=client,
    ).parsed


async def asyncio_detailed(
    source: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | bool]:
    """Metadata Heartbeat

     Endpoint to return the heartbeat of the metadata sources

    Args:
        source (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | bool]
    """

    kwargs = _get_kwargs(
        source=source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | bool | None:
    """Metadata Heartbeat

     Endpoint to return the heartbeat of the metadata sources

    Args:
        source (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | bool
    """

    return (
        await asyncio_detailed(
            source=source,
            client=client,
        )
    ).parsed
