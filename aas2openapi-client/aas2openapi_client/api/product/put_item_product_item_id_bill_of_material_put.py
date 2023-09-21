from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.bill_of_material import BillOfMaterial
from ...models.http_validation_error import HTTPValidationError
from ...models.put_item_product_item_id_bill_of_material_put_response_put_item_product_item_id_billofmaterial_put import (
    PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut,
)
from ...types import Response


def _get_kwargs(
    item_id: str,
    *,
    client: Client,
    json_body: BillOfMaterial,
) -> Dict[str, Any]:
    url = "{}/Product/{item_id}/BillOfMaterial/".format(client.base_url, item_id=item_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut.from_dict(
            response.json()
        )

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: Client,
    json_body: BillOfMaterial,
) -> Response[
    Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]
]:
    """Put Item

    Args:
        item_id (str):
        json_body (BillOfMaterial):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: Client,
    json_body: BillOfMaterial,
) -> Optional[
    Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]
]:
    """Put Item

    Args:
        item_id (str):
        json_body (BillOfMaterial):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: Client,
    json_body: BillOfMaterial,
) -> Response[
    Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]
]:
    """Put Item

    Args:
        item_id (str):
        json_body (BillOfMaterial):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: Client,
    json_body: BillOfMaterial,
) -> Optional[
    Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]
]:
    """Put Item

    Args:
        item_id (str):
        json_body (BillOfMaterial):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PutItemProductItemIdBillOfMaterialPutResponsePutItemProductItemIdBillofmaterialPut]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
