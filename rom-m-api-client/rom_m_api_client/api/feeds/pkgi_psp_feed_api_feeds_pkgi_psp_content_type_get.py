from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    content_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/feeds/pkgi/psp/{content_type}".format(
            content_type=quote(str(content_type), safe=""),
        ),
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
    content_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
    """Pkgi Psp Feed

     Get PKGi PSP feed endpoint
    https://github.com/bucanero/pkgi-psp

    Args:
        request (Request): Fastapi Request object
        content_type (str): Content type (game, dlc, demo, update, patch, mod, translation, prototype)

    Returns:
        Response: txt file with PKGi PSP database format

    Args:
        content_type (str): Content type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    content_type: str,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
    """Pkgi Psp Feed

     Get PKGi PSP feed endpoint
    https://github.com/bucanero/pkgi-psp

    Args:
        request (Request): Fastapi Request object
        content_type (str): Content type (game, dlc, demo, update, patch, mod, translation, prototype)

    Returns:
        Response: txt file with PKGi PSP database format

    Args:
        content_type (str): Content type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        content_type=content_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    content_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
    """Pkgi Psp Feed

     Get PKGi PSP feed endpoint
    https://github.com/bucanero/pkgi-psp

    Args:
        request (Request): Fastapi Request object
        content_type (str): Content type (game, dlc, demo, update, patch, mod, translation, prototype)

    Returns:
        Response: txt file with PKGi PSP database format

    Args:
        content_type (str): Content type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    content_type: str,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
    """Pkgi Psp Feed

     Get PKGi PSP feed endpoint
    https://github.com/bucanero/pkgi-psp

    Args:
        request (Request): Fastapi Request object
        content_type (str): Content type (game, dlc, demo, update, patch, mod, translation, prototype)

    Returns:
        Response: txt file with PKGi PSP database format

    Args:
        content_type (str): Content type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            content_type=content_type,
            client=client,
        )
    ).parsed
