from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    file_name: str,
    *,
    file_ids: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_file_ids: None | str | Unset
    if isinstance(file_ids, Unset):
        json_file_ids = UNSET
    else:
        json_file_ids = file_ids
    params["file_ids"] = json_file_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/roms/{id}/content/{file_name}".format(
            id=quote(str(id), safe=""),
            file_name=quote(str(file_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    file_name: str,
    *,
    client: AuthenticatedClient,
    file_ids: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Head Rom Content

     Retrieve head information for a rom file download.

    Args:
        id (int): Rom internal id.
        file_name (str): File name to download
        file_ids (None | str | Unset): Comma-separated list of file ids to download for multi-part
            roms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        file_name=file_name,
        file_ids=file_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    file_name: str,
    *,
    client: AuthenticatedClient,
    file_ids: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Head Rom Content

     Retrieve head information for a rom file download.

    Args:
        id (int): Rom internal id.
        file_name (str): File name to download
        file_ids (None | str | Unset): Comma-separated list of file ids to download for multi-part
            roms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        id=id,
        file_name=file_name,
        client=client,
        file_ids=file_ids,
    ).parsed


async def asyncio_detailed(
    id: int,
    file_name: str,
    *,
    client: AuthenticatedClient,
    file_ids: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Head Rom Content

     Retrieve head information for a rom file download.

    Args:
        id (int): Rom internal id.
        file_name (str): File name to download
        file_ids (None | str | Unset): Comma-separated list of file ids to download for multi-part
            roms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        file_name=file_name,
        file_ids=file_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    file_name: str,
    *,
    client: AuthenticatedClient,
    file_ids: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Head Rom Content

     Retrieve head information for a rom file download.

    Args:
        id (int): Rom internal id.
        file_name (str): File name to download
        file_ids (None | str | Unset): Comma-separated list of file ids to download for multi-part
            roms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            file_name=file_name,
            client=client,
            file_ids=file_ids,
        )
    ).parsed
