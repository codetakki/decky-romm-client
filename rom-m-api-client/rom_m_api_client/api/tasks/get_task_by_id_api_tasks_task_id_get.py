from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cleanup_task_status_response import CleanupTaskStatusResponse
from ...models.conversion_task_status_response import ConversionTaskStatusResponse
from ...models.generic_task_status_response import GenericTaskStatusResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.scan_task_status_response import ScanTaskStatusResponse
from ...models.update_task_status_response import UpdateTaskStatusResponse
from ...models.watcher_task_status_response import WatcherTaskStatusResponse
from ...types import Response


def _get_kwargs(
    task_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tasks/{task_id}".format(
            task_id=quote(str(task_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CleanupTaskStatusResponse
    | ConversionTaskStatusResponse
    | GenericTaskStatusResponse
    | ScanTaskStatusResponse
    | UpdateTaskStatusResponse
    | WatcherTaskStatusResponse
    | HTTPValidationError
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
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
                response_200_type_0 = ScanTaskStatusResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = ConversionTaskStatusResponse.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = UpdateTaskStatusResponse.from_dict(data)

                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = CleanupTaskStatusResponse.from_dict(data)

                return response_200_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = WatcherTaskStatusResponse.from_dict(data)

                return response_200_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_5 = GenericTaskStatusResponse.from_dict(data)

            return response_200_type_5

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    CleanupTaskStatusResponse
    | ConversionTaskStatusResponse
    | GenericTaskStatusResponse
    | ScanTaskStatusResponse
    | UpdateTaskStatusResponse
    | WatcherTaskStatusResponse
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    CleanupTaskStatusResponse
    | ConversionTaskStatusResponse
    | GenericTaskStatusResponse
    | ScanTaskStatusResponse
    | UpdateTaskStatusResponse
    | WatcherTaskStatusResponse
    | HTTPValidationError
]:
    """Get Task By Id

     Get the status of a task by its job ID.

    Args:
        request (Request): FastAPI Request object
        task_id (str): Job ID of the task to retrieve status for
    Returns:
        TaskStatusResponse: Task status information

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CleanupTaskStatusResponse | ConversionTaskStatusResponse | GenericTaskStatusResponse | ScanTaskStatusResponse | UpdateTaskStatusResponse | WatcherTaskStatusResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    CleanupTaskStatusResponse
    | ConversionTaskStatusResponse
    | GenericTaskStatusResponse
    | ScanTaskStatusResponse
    | UpdateTaskStatusResponse
    | WatcherTaskStatusResponse
    | HTTPValidationError
    | None
):
    """Get Task By Id

     Get the status of a task by its job ID.

    Args:
        request (Request): FastAPI Request object
        task_id (str): Job ID of the task to retrieve status for
    Returns:
        TaskStatusResponse: Task status information

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CleanupTaskStatusResponse | ConversionTaskStatusResponse | GenericTaskStatusResponse | ScanTaskStatusResponse | UpdateTaskStatusResponse | WatcherTaskStatusResponse | HTTPValidationError
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    CleanupTaskStatusResponse
    | ConversionTaskStatusResponse
    | GenericTaskStatusResponse
    | ScanTaskStatusResponse
    | UpdateTaskStatusResponse
    | WatcherTaskStatusResponse
    | HTTPValidationError
]:
    """Get Task By Id

     Get the status of a task by its job ID.

    Args:
        request (Request): FastAPI Request object
        task_id (str): Job ID of the task to retrieve status for
    Returns:
        TaskStatusResponse: Task status information

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CleanupTaskStatusResponse | ConversionTaskStatusResponse | GenericTaskStatusResponse | ScanTaskStatusResponse | UpdateTaskStatusResponse | WatcherTaskStatusResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    CleanupTaskStatusResponse
    | ConversionTaskStatusResponse
    | GenericTaskStatusResponse
    | ScanTaskStatusResponse
    | UpdateTaskStatusResponse
    | WatcherTaskStatusResponse
    | HTTPValidationError
    | None
):
    """Get Task By Id

     Get the status of a task by its job ID.

    Args:
        request (Request): FastAPI Request object
        task_id (str): Job ID of the task to retrieve status for
    Returns:
        TaskStatusResponse: Task status information

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CleanupTaskStatusResponse | ConversionTaskStatusResponse | GenericTaskStatusResponse | ScanTaskStatusResponse | UpdateTaskStatusResponse | WatcherTaskStatusResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
        )
    ).parsed
