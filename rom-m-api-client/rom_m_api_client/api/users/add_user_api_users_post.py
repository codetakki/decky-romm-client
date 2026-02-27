from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_add_user_api_users_post import BodyAddUserApiUsersPost
from ...models.http_validation_error import HTTPValidationError
from ...models.user_schema import UserSchema
from ...types import Response


def _get_kwargs(
    *,
    body: BodyAddUserApiUsersPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserSchema | None:
    if response.status_code == 201:
        response_201 = UserSchema.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | UserSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyAddUserApiUsersPost,
) -> Response[HTTPValidationError | UserSchema]:
    """Add User

     Create user endpoint

    Args:
        request (Request): Fastapi Requests object
        username (str): User username
        password (str): User password
        email (str): User email
        role (str): RomM Role object represented as string

    Returns:
        UserSchema: Newly created user

    Args:
        body (BodyAddUserApiUsersPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserSchema]
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
    client: AuthenticatedClient,
    body: BodyAddUserApiUsersPost,
) -> HTTPValidationError | UserSchema | None:
    """Add User

     Create user endpoint

    Args:
        request (Request): Fastapi Requests object
        username (str): User username
        password (str): User password
        email (str): User email
        role (str): RomM Role object represented as string

    Returns:
        UserSchema: Newly created user

    Args:
        body (BodyAddUserApiUsersPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyAddUserApiUsersPost,
) -> Response[HTTPValidationError | UserSchema]:
    """Add User

     Create user endpoint

    Args:
        request (Request): Fastapi Requests object
        username (str): User username
        password (str): User password
        email (str): User email
        role (str): RomM Role object represented as string

    Returns:
        UserSchema: Newly created user

    Args:
        body (BodyAddUserApiUsersPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyAddUserApiUsersPost,
) -> HTTPValidationError | UserSchema | None:
    """Add User

     Create user endpoint

    Args:
        request (Request): Fastapi Requests object
        username (str): User username
        password (str): User password
        email (str): User email
        role (str): RomM Role object represented as string

    Returns:
        UserSchema: Newly created user

    Args:
        body (BodyAddUserApiUsersPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
