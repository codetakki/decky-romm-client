from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_token_api_token_post import BodyTokenApiTokenPost
from ...models.http_validation_error import HTTPValidationError
from ...models.token_response import TokenResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyTokenApiTokenPost | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/token",
    }

    if not isinstance(body, Unset):
        _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TokenResponse | None:
    if response.status_code == 200:
        response_200 = TokenResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyTokenApiTokenPost | Unset = UNSET,
) -> Response[HTTPValidationError | TokenResponse]:
    """Token

     OAuth2 token endpoint

    Args:
        form_data (Annotated[OAuth2RequestForm, Depends): Form Data with OAuth2 info

    Raises:
        HTTPException: Missing refresh token
        HTTPException: Invalid refresh token
        HTTPException: Missing username or password
        HTTPException: Invalid username or password
        HTTPException: Client credentials are not yet supported
        HTTPException: Invalid or unsupported grant type
        HTTPException: Insufficient scope

    Returns:
        TokenResponse: TypedDict with the new generated token info

    Args:
        body (BodyTokenApiTokenPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BodyTokenApiTokenPost | Unset = UNSET,
) -> HTTPValidationError | TokenResponse | None:
    """Token

     OAuth2 token endpoint

    Args:
        form_data (Annotated[OAuth2RequestForm, Depends): Form Data with OAuth2 info

    Raises:
        HTTPException: Missing refresh token
        HTTPException: Invalid refresh token
        HTTPException: Missing username or password
        HTTPException: Invalid username or password
        HTTPException: Client credentials are not yet supported
        HTTPException: Invalid or unsupported grant type
        HTTPException: Insufficient scope

    Returns:
        TokenResponse: TypedDict with the new generated token info

    Args:
        body (BodyTokenApiTokenPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TokenResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyTokenApiTokenPost | Unset = UNSET,
) -> Response[HTTPValidationError | TokenResponse]:
    """Token

     OAuth2 token endpoint

    Args:
        form_data (Annotated[OAuth2RequestForm, Depends): Form Data with OAuth2 info

    Raises:
        HTTPException: Missing refresh token
        HTTPException: Invalid refresh token
        HTTPException: Missing username or password
        HTTPException: Invalid username or password
        HTTPException: Client credentials are not yet supported
        HTTPException: Invalid or unsupported grant type
        HTTPException: Insufficient scope

    Returns:
        TokenResponse: TypedDict with the new generated token info

    Args:
        body (BodyTokenApiTokenPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BodyTokenApiTokenPost | Unset = UNSET,
) -> HTTPValidationError | TokenResponse | None:
    """Token

     OAuth2 token endpoint

    Args:
        form_data (Annotated[OAuth2RequestForm, Depends): Form Data with OAuth2 info

    Raises:
        HTTPException: Missing refresh token
        HTTPException: Invalid refresh token
        HTTPException: Missing username or password
        HTTPException: Invalid username or password
        HTTPException: Client credentials are not yet supported
        HTTPException: Invalid or unsupported grant type
        HTTPException: Insufficient scope

    Returns:
        TokenResponse: TypedDict with the new generated token info

    Args:
        body (BodyTokenApiTokenPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
