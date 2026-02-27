from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detailed_rom_schema import DetailedRomSchema
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    crc_hash: None | str | Unset = UNSET,
    md5_hash: None | str | Unset = UNSET,
    sha1_hash: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_crc_hash: None | str | Unset
    if isinstance(crc_hash, Unset):
        json_crc_hash = UNSET
    else:
        json_crc_hash = crc_hash
    params["crc_hash"] = json_crc_hash

    json_md5_hash: None | str | Unset
    if isinstance(md5_hash, Unset):
        json_md5_hash = UNSET
    else:
        json_md5_hash = md5_hash
    params["md5_hash"] = json_md5_hash

    json_sha1_hash: None | str | Unset
    if isinstance(sha1_hash, Unset):
        json_sha1_hash = UNSET
    else:
        json_sha1_hash = sha1_hash
    params["sha1_hash"] = json_sha1_hash

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/roms/by-hash",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DetailedRomSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    crc_hash: None | str | Unset = UNSET,
    md5_hash: None | str | Unset = UNSET,
    sha1_hash: None | str | Unset = UNSET,
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
    """Get Rom By Hash

    Args:
        crc_hash (None | str | Unset): CRC hash value
        md5_hash (None | str | Unset): MD5 hash value
        sha1_hash (None | str | Unset): SHA1 hash value

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DetailedRomSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        crc_hash=crc_hash,
        md5_hash=md5_hash,
        sha1_hash=sha1_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    crc_hash: None | str | Unset = UNSET,
    md5_hash: None | str | Unset = UNSET,
    sha1_hash: None | str | Unset = UNSET,
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    """Get Rom By Hash

    Args:
        crc_hash (None | str | Unset): CRC hash value
        md5_hash (None | str | Unset): MD5 hash value
        sha1_hash (None | str | Unset): SHA1 hash value

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DetailedRomSchema | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        crc_hash=crc_hash,
        md5_hash=md5_hash,
        sha1_hash=sha1_hash,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    crc_hash: None | str | Unset = UNSET,
    md5_hash: None | str | Unset = UNSET,
    sha1_hash: None | str | Unset = UNSET,
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
    """Get Rom By Hash

    Args:
        crc_hash (None | str | Unset): CRC hash value
        md5_hash (None | str | Unset): MD5 hash value
        sha1_hash (None | str | Unset): SHA1 hash value

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DetailedRomSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        crc_hash=crc_hash,
        md5_hash=md5_hash,
        sha1_hash=sha1_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    crc_hash: None | str | Unset = UNSET,
    md5_hash: None | str | Unset = UNSET,
    sha1_hash: None | str | Unset = UNSET,
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    """Get Rom By Hash

    Args:
        crc_hash (None | str | Unset): CRC hash value
        md5_hash (None | str | Unset): MD5 hash value
        sha1_hash (None | str | Unset): SHA1 hash value

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DetailedRomSchema | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            crc_hash=crc_hash,
            md5_hash=md5_hash,
            sha1_hash=sha1_hash,
        )
    ).parsed
