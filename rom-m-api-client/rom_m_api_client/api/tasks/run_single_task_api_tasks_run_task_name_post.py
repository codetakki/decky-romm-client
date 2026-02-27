from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.task_execution_response import TaskExecutionResponse
from ...types import Response


def _get_kwargs(
    task_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tasks/run/{task_name}".format(
            task_name=quote(str(task_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TaskExecutionResponse | None:
    if response.status_code == 200:
        response_200 = TaskExecutionResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TaskExecutionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | TaskExecutionResponse]:
    """Run Single Task

     Run a single task endpoint.

    Args:
        request (Request): FastAPI Request object
        task_name (str): Name of the task to run
    Returns:
        TaskExecutionResponse: Task execution response with details

    Args:
        task_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TaskExecutionResponse]
    """

    kwargs = _get_kwargs(
        task_name=task_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_name: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | TaskExecutionResponse | None:
    """Run Single Task

     Run a single task endpoint.

    Args:
        request (Request): FastAPI Request object
        task_name (str): Name of the task to run
    Returns:
        TaskExecutionResponse: Task execution response with details

    Args:
        task_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TaskExecutionResponse
    """

    return sync_detailed(
        task_name=task_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    task_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | TaskExecutionResponse]:
    """Run Single Task

     Run a single task endpoint.

    Args:
        request (Request): FastAPI Request object
        task_name (str): Name of the task to run
    Returns:
        TaskExecutionResponse: Task execution response with details

    Args:
        task_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TaskExecutionResponse]
    """

    kwargs = _get_kwargs(
        task_name=task_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_name: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | TaskExecutionResponse | None:
    """Run Single Task

     Run a single task endpoint.

    Args:
        request (Request): FastAPI Request object
        task_name (str): Name of the task to run
    Returns:
        TaskExecutionResponse: Task execution response with details

    Args:
        task_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TaskExecutionResponse
    """

    return (
        await asyncio_detailed(
            task_name=task_name,
            client=client,
        )
    ).parsed
