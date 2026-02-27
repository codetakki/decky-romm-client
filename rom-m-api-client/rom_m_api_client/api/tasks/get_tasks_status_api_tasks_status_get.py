from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cleanup_task_status_response import CleanupTaskStatusResponse
from ...models.conversion_task_status_response import ConversionTaskStatusResponse
from ...models.generic_task_status_response import GenericTaskStatusResponse
from ...models.scan_task_status_response import ScanTaskStatusResponse
from ...models.update_task_status_response import UpdateTaskStatusResponse
from ...models.watcher_task_status_response import WatcherTaskStatusResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tasks/status",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    list[
        CleanupTaskStatusResponse
        | ConversionTaskStatusResponse
        | GenericTaskStatusResponse
        | ScanTaskStatusResponse
        | UpdateTaskStatusResponse
        | WatcherTaskStatusResponse
    ]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> (
                CleanupTaskStatusResponse
                | ConversionTaskStatusResponse
                | GenericTaskStatusResponse
                | ScanTaskStatusResponse
                | UpdateTaskStatusResponse
                | WatcherTaskStatusResponse
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = ScanTaskStatusResponse.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_1 = ConversionTaskStatusResponse.from_dict(data)

                    return response_200_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_2 = UpdateTaskStatusResponse.from_dict(data)

                    return response_200_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_3 = CleanupTaskStatusResponse.from_dict(data)

                    return response_200_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_4 = WatcherTaskStatusResponse.from_dict(data)

                    return response_200_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_5 = GenericTaskStatusResponse.from_dict(data)

                return response_200_item_type_5

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    list[
        CleanupTaskStatusResponse
        | ConversionTaskStatusResponse
        | GenericTaskStatusResponse
        | ScanTaskStatusResponse
        | UpdateTaskStatusResponse
        | WatcherTaskStatusResponse
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    list[
        CleanupTaskStatusResponse
        | ConversionTaskStatusResponse
        | GenericTaskStatusResponse
        | ScanTaskStatusResponse
        | UpdateTaskStatusResponse
        | WatcherTaskStatusResponse
    ]
]:
    """Get Tasks Status

     Get all active, queued, completed, and failed tasks.

    Args:
        request (Request): FastAPI Request object
    Returns:
        list[TaskStatusResponse]: List of all tasks with their current status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CleanupTaskStatusResponse | ConversionTaskStatusResponse | GenericTaskStatusResponse | ScanTaskStatusResponse | UpdateTaskStatusResponse | WatcherTaskStatusResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> (
    list[
        CleanupTaskStatusResponse
        | ConversionTaskStatusResponse
        | GenericTaskStatusResponse
        | ScanTaskStatusResponse
        | UpdateTaskStatusResponse
        | WatcherTaskStatusResponse
    ]
    | None
):
    """Get Tasks Status

     Get all active, queued, completed, and failed tasks.

    Args:
        request (Request): FastAPI Request object
    Returns:
        list[TaskStatusResponse]: List of all tasks with their current status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CleanupTaskStatusResponse | ConversionTaskStatusResponse | GenericTaskStatusResponse | ScanTaskStatusResponse | UpdateTaskStatusResponse | WatcherTaskStatusResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    list[
        CleanupTaskStatusResponse
        | ConversionTaskStatusResponse
        | GenericTaskStatusResponse
        | ScanTaskStatusResponse
        | UpdateTaskStatusResponse
        | WatcherTaskStatusResponse
    ]
]:
    """Get Tasks Status

     Get all active, queued, completed, and failed tasks.

    Args:
        request (Request): FastAPI Request object
    Returns:
        list[TaskStatusResponse]: List of all tasks with their current status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CleanupTaskStatusResponse | ConversionTaskStatusResponse | GenericTaskStatusResponse | ScanTaskStatusResponse | UpdateTaskStatusResponse | WatcherTaskStatusResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    list[
        CleanupTaskStatusResponse
        | ConversionTaskStatusResponse
        | GenericTaskStatusResponse
        | ScanTaskStatusResponse
        | UpdateTaskStatusResponse
        | WatcherTaskStatusResponse
    ]
    | None
):
    """Get Tasks Status

     Get all active, queued, completed, and failed tasks.

    Args:
        request (Request): FastAPI Request object
    Returns:
        list[TaskStatusResponse]: List of all tasks with their current status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CleanupTaskStatusResponse | ConversionTaskStatusResponse | GenericTaskStatusResponse | ScanTaskStatusResponse | UpdateTaskStatusResponse | WatcherTaskStatusResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
