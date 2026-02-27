from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.tinfoil_feed_schema import TinfoilFeedSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    slug: str | Unset = "switch",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["slug"] = slug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/feeds/tinfoil",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TinfoilFeedSchema | None:
    if response.status_code == 200:
        response_200 = TinfoilFeedSchema.from_dict(response.json())

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
) -> Response[HTTPValidationError | TinfoilFeedSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    slug: str | Unset = "switch",
) -> Response[HTTPValidationError | TinfoilFeedSchema]:
    r"""Tinfoil Index Feed

     Get tinfoil custom index feed endpoint
    https://blawar.github.io/tinfoil/custom_index/

    Args:
        request (Request): Fastapi Request object
        slug (str, optional): Platform slug. Defaults to \"switch\".

    Returns:
        TinfoilFeedSchema: Tinfoil feed object schema

    Args:
        slug (str | Unset):  Default: 'switch'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TinfoilFeedSchema]
    """

    kwargs = _get_kwargs(
        slug=slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    slug: str | Unset = "switch",
) -> HTTPValidationError | TinfoilFeedSchema | None:
    r"""Tinfoil Index Feed

     Get tinfoil custom index feed endpoint
    https://blawar.github.io/tinfoil/custom_index/

    Args:
        request (Request): Fastapi Request object
        slug (str, optional): Platform slug. Defaults to \"switch\".

    Returns:
        TinfoilFeedSchema: Tinfoil feed object schema

    Args:
        slug (str | Unset):  Default: 'switch'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TinfoilFeedSchema
    """

    return sync_detailed(
        client=client,
        slug=slug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    slug: str | Unset = "switch",
) -> Response[HTTPValidationError | TinfoilFeedSchema]:
    r"""Tinfoil Index Feed

     Get tinfoil custom index feed endpoint
    https://blawar.github.io/tinfoil/custom_index/

    Args:
        request (Request): Fastapi Request object
        slug (str, optional): Platform slug. Defaults to \"switch\".

    Returns:
        TinfoilFeedSchema: Tinfoil feed object schema

    Args:
        slug (str | Unset):  Default: 'switch'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TinfoilFeedSchema]
    """

    kwargs = _get_kwargs(
        slug=slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    slug: str | Unset = "switch",
) -> HTTPValidationError | TinfoilFeedSchema | None:
    r"""Tinfoil Index Feed

     Get tinfoil custom index feed endpoint
    https://blawar.github.io/tinfoil/custom_index/

    Args:
        request (Request): Fastapi Request object
        slug (str, optional): Platform slug. Defaults to \"switch\".

    Returns:
        TinfoilFeedSchema: Tinfoil feed object schema

    Args:
        slug (str | Unset):  Default: 'switch'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TinfoilFeedSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            slug=slug,
        )
    ).parsed
