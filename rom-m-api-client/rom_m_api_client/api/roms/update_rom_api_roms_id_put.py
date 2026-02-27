from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_update_rom_api_roms_id_put import BodyUpdateRomApiRomsIdPut
from ...models.detailed_rom_schema import DetailedRomSchema
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: BodyUpdateRomApiRomsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    unmatch_metadata: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["remove_cover"] = remove_cover

    params["unmatch_metadata"] = unmatch_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/roms/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DetailedRomSchema.from_dict(response.json())

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
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
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
    body: BodyUpdateRomApiRomsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    unmatch_metadata: bool | Unset = False,
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
    """Update Rom

     Update a rom.

    Args:
        id (int): Rom internal id.
        remove_cover (bool | Unset): Whether to remove the cover image for this rom. Default:
            False.
        unmatch_metadata (bool | Unset): Whether to remove the metadata matches for this game.
            Default: False.
        body (BodyUpdateRomApiRomsIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DetailedRomSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        remove_cover=remove_cover,
        unmatch_metadata=unmatch_metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateRomApiRomsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    unmatch_metadata: bool | Unset = False,
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    """Update Rom

     Update a rom.

    Args:
        id (int): Rom internal id.
        remove_cover (bool | Unset): Whether to remove the cover image for this rom. Default:
            False.
        unmatch_metadata (bool | Unset): Whether to remove the metadata matches for this game.
            Default: False.
        body (BodyUpdateRomApiRomsIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DetailedRomSchema | HTTPValidationError
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        remove_cover=remove_cover,
        unmatch_metadata=unmatch_metadata,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateRomApiRomsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    unmatch_metadata: bool | Unset = False,
) -> Response[Any | DetailedRomSchema | HTTPValidationError]:
    """Update Rom

     Update a rom.

    Args:
        id (int): Rom internal id.
        remove_cover (bool | Unset): Whether to remove the cover image for this rom. Default:
            False.
        unmatch_metadata (bool | Unset): Whether to remove the metadata matches for this game.
            Default: False.
        body (BodyUpdateRomApiRomsIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DetailedRomSchema | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        remove_cover=remove_cover,
        unmatch_metadata=unmatch_metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUpdateRomApiRomsIdPut | Unset = UNSET,
    remove_cover: bool | Unset = False,
    unmatch_metadata: bool | Unset = False,
) -> Any | DetailedRomSchema | HTTPValidationError | None:
    """Update Rom

     Update a rom.

    Args:
        id (int): Rom internal id.
        remove_cover (bool | Unset): Whether to remove the cover image for this rom. Default:
            False.
        unmatch_metadata (bool | Unset): Whether to remove the metadata matches for this game.
            Default: False.
        body (BodyUpdateRomApiRomsIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DetailedRomSchema | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            remove_cover=remove_cover,
            unmatch_metadata=unmatch_metadata,
        )
    ).parsed
