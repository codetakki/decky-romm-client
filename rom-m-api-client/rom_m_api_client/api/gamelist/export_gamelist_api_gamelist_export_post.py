from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform_ids: list[int],
    local_export: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_platform_ids = platform_ids

    params["platform_ids"] = json_platform_ids

    params["local_export"] = local_export

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/gamelist/export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    platform_ids: list[int],
    local_export: bool | Unset = False,
) -> Response[Any | HTTPValidationError]:
    """Export Gamelist

     Export platforms/ROMs to gamelist.xml format and write to platform directories

    Args:
        platform_ids (list[int]): List of platform IDs to export
        local_export (bool | Unset): Use local paths instead of URLs Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        platform_ids=platform_ids,
        local_export=local_export,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    platform_ids: list[int],
    local_export: bool | Unset = False,
) -> Any | HTTPValidationError | None:
    """Export Gamelist

     Export platforms/ROMs to gamelist.xml format and write to platform directories

    Args:
        platform_ids (list[int]): List of platform IDs to export
        local_export (bool | Unset): Use local paths instead of URLs Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        platform_ids=platform_ids,
        local_export=local_export,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    platform_ids: list[int],
    local_export: bool | Unset = False,
) -> Response[Any | HTTPValidationError]:
    """Export Gamelist

     Export platforms/ROMs to gamelist.xml format and write to platform directories

    Args:
        platform_ids (list[int]): List of platform IDs to export
        local_export (bool | Unset): Use local paths instead of URLs Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        platform_ids=platform_ids,
        local_export=local_export,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    platform_ids: list[int],
    local_export: bool | Unset = False,
) -> Any | HTTPValidationError | None:
    """Export Gamelist

     Export platforms/ROMs to gamelist.xml format and write to platform directories

    Args:
        platform_ids (list[int]): List of platform IDs to export
        local_export (bool | Unset): Use local paths instead of URLs Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            platform_ids=platform_ids,
            local_export=local_export,
        )
    ).parsed
