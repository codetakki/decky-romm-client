from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_update_rom_user_api_roms_id_props_put import BodyUpdateRomUserApiRomsIdPropsPut
from ...models.http_validation_error import HTTPValidationError
from ...models.rom_user_schema import RomUserSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: BodyUpdateRomUserApiRomsIdPropsPut | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/roms/{id}/props".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | RomUserSchema | None:
    if response.status_code == 200:
        response_200 = RomUserSchema.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | RomUserSchema]:
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
    body: BodyUpdateRomUserApiRomsIdPropsPut | Unset = UNSET,
) -> Response[Any | HTTPValidationError | RomUserSchema]:
    """Update Rom User

     Update rom data associated to the current user.

    Args:
        id (int): Rom internal id.
        body (BodyUpdateRomUserApiRomsIdPropsPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | RomUserSchema]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateRomUserApiRomsIdPropsPut | Unset = UNSET,
) -> Any | HTTPValidationError | RomUserSchema | None:
    """Update Rom User

     Update rom data associated to the current user.

    Args:
        id (int): Rom internal id.
        body (BodyUpdateRomUserApiRomsIdPropsPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | RomUserSchema
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateRomUserApiRomsIdPropsPut | Unset = UNSET,
) -> Response[Any | HTTPValidationError | RomUserSchema]:
    """Update Rom User

     Update rom data associated to the current user.

    Args:
        id (int): Rom internal id.
        body (BodyUpdateRomUserApiRomsIdPropsPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | RomUserSchema]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateRomUserApiRomsIdPropsPut | Unset = UNSET,
) -> Any | HTTPValidationError | RomUserSchema | None:
    """Update Rom User

     Update rom data associated to the current user.

    Args:
        id (int): Rom internal id.
        body (BodyUpdateRomUserApiRomsIdPropsPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | RomUserSchema
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
