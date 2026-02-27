from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tasks_api_tasks_get_response_list_tasks_api_tasks_get import (
    ListTasksApiTasksGetResponseListTasksApiTasksGet,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tasks",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListTasksApiTasksGetResponseListTasksApiTasksGet | None:
    if response.status_code == 200:
        response_200 = ListTasksApiTasksGetResponseListTasksApiTasksGet.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListTasksApiTasksGetResponseListTasksApiTasksGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListTasksApiTasksGetResponseListTasksApiTasksGet]:
    """List Tasks

     List all available tasks grouped by task type.

    Args:
        request (Request): FastAPI Request object
    Returns:
        GroupedTasksDict: Dictionary with tasks grouped by their type (scheduled, manual, watcher)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTasksApiTasksGetResponseListTasksApiTasksGet]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ListTasksApiTasksGetResponseListTasksApiTasksGet | None:
    """List Tasks

     List all available tasks grouped by task type.

    Args:
        request (Request): FastAPI Request object
    Returns:
        GroupedTasksDict: Dictionary with tasks grouped by their type (scheduled, manual, watcher)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTasksApiTasksGetResponseListTasksApiTasksGet
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListTasksApiTasksGetResponseListTasksApiTasksGet]:
    """List Tasks

     List all available tasks grouped by task type.

    Args:
        request (Request): FastAPI Request object
    Returns:
        GroupedTasksDict: Dictionary with tasks grouped by their type (scheduled, manual, watcher)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTasksApiTasksGetResponseListTasksApiTasksGet]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ListTasksApiTasksGetResponseListTasksApiTasksGet | None:
    """List Tasks

     List all available tasks grouped by task type.

    Args:
        request (Request): FastAPI Request object
    Returns:
        GroupedTasksDict: Dictionary with tasks grouped by their type (scheduled, manual, watcher)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTasksApiTasksGetResponseListTasksApiTasksGet
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
