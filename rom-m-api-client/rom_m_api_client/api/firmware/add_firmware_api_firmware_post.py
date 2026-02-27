from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_firmware_response import AddFirmwareResponse
from ...models.body_add_firmware_api_firmware_post import BodyAddFirmwareApiFirmwarePost
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: BodyAddFirmwareApiFirmwarePost,
    platform_id: int,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["platform_id"] = platform_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/firmware",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddFirmwareResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AddFirmwareResponse.from_dict(response.json())

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
) -> Response[AddFirmwareResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyAddFirmwareApiFirmwarePost,
    platform_id: int,
) -> Response[AddFirmwareResponse | HTTPValidationError]:
    """Add Firmware

     Upload firmware files endpoint

    Args:
        request (Request): Fastapi Request object
        platform_slug (str): Slug of the platform where to upload the files
        files (list[UploadFile], optional): List of files to upload

    Raises:
        HTTPException

    Returns:
        AddFirmwareResponse: Standard message response

    Args:
        platform_id (int):
        body (BodyAddFirmwareApiFirmwarePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddFirmwareResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        platform_id=platform_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyAddFirmwareApiFirmwarePost,
    platform_id: int,
) -> AddFirmwareResponse | HTTPValidationError | None:
    """Add Firmware

     Upload firmware files endpoint

    Args:
        request (Request): Fastapi Request object
        platform_slug (str): Slug of the platform where to upload the files
        files (list[UploadFile], optional): List of files to upload

    Raises:
        HTTPException

    Returns:
        AddFirmwareResponse: Standard message response

    Args:
        platform_id (int):
        body (BodyAddFirmwareApiFirmwarePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddFirmwareResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        platform_id=platform_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyAddFirmwareApiFirmwarePost,
    platform_id: int,
) -> Response[AddFirmwareResponse | HTTPValidationError]:
    """Add Firmware

     Upload firmware files endpoint

    Args:
        request (Request): Fastapi Request object
        platform_slug (str): Slug of the platform where to upload the files
        files (list[UploadFile], optional): List of files to upload

    Raises:
        HTTPException

    Returns:
        AddFirmwareResponse: Standard message response

    Args:
        platform_id (int):
        body (BodyAddFirmwareApiFirmwarePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddFirmwareResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        platform_id=platform_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyAddFirmwareApiFirmwarePost,
    platform_id: int,
) -> AddFirmwareResponse | HTTPValidationError | None:
    """Add Firmware

     Upload firmware files endpoint

    Args:
        request (Request): Fastapi Request object
        platform_slug (str): Slug of the platform where to upload the files
        files (list[UploadFile], optional): List of files to upload

    Raises:
        HTTPException

    Returns:
        AddFirmwareResponse: Standard message response

    Args:
        platform_id (int):
        body (BodyAddFirmwareApiFirmwarePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddFirmwareResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            platform_id=platform_id,
        )
    ).parsed
