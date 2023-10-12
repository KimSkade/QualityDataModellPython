from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.post_item_quality_data_aas_post_response_post_item_qualitydataaas_post import (
    PostItemQualityDataAASPostResponsePostItemQualitydataaasPost,
)
from ...models.quality_data_aas import QualityDataAAS
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: QualityDataAAS,
) -> Dict[str, Any]:
    url = "{}/QualityDataAAS/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostItemQualityDataAASPostResponsePostItemQualitydataaasPost.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: QualityDataAAS,
) -> Response[Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]]:
    """Post Item

    Args:
        json_body (QualityDataAAS):  Example: {"id_": "QualityDataAAS", "description": "xyz",
            "id_short": "QualityDataAAS", "quality_data": {"id_": "Submodel", "description": "xyz",
            "id_short": "QualityDataSubmodel", "semantic_id": "http://www.google.de/1",
            "production_procedures": [{"id_short": "ProductionProcedures", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "resource": "Platzhalter", "process":
            "Patzhalter", "features": [{"id_short": "Features", "description": "xyz", "semantic_id":
            "http://www.google.de/1", "quality_feature_name": [{"id_short": "qualityFeatureName1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "feature_type": "Zylinder
            Mitte", "function": "Durchmesser", "unit": "mm", "target_value": 9.0, "upper_tolerance":
            0.1, "lower_tolerance": -0.1, "warning_limit": 100.0, "control_limit": 1.0,
            "inspection_equipement": "PlatzhalterEquipment", "references": [{"id_short": "reference1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "point": "Platzhalter
            point", "line": "Platzhalter line", "surface": "Platzhalter surface", "axis": "Platzhalter
            axis"}], "sample_batch": [{"id_short": "sampleBatch1", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "sample_size": 1, "sample_data": [{"id_short":
            "sampleData1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "sample_number": 1223, "sample_date": "Platzhalter Datum", "part_counter": 1212, "result":
            [{"id_short": "result1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "value": 8.9973025, "measurement_date": "Platzhalte Datum Uhrzeit", "uppertol": 0.1,
            "lowertol": -0.1, "nominal": 9.0, "result_check": true}]}]}]}]}]}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: QualityDataAAS,
) -> Optional[Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]]:
    """Post Item

    Args:
        json_body (QualityDataAAS):  Example: {"id_": "QualityDataAAS", "description": "xyz",
            "id_short": "QualityDataAAS", "quality_data": {"id_": "Submodel", "description": "xyz",
            "id_short": "QualityDataSubmodel", "semantic_id": "http://www.google.de/1",
            "production_procedures": [{"id_short": "ProductionProcedures", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "resource": "Platzhalter", "process":
            "Patzhalter", "features": [{"id_short": "Features", "description": "xyz", "semantic_id":
            "http://www.google.de/1", "quality_feature_name": [{"id_short": "qualityFeatureName1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "feature_type": "Zylinder
            Mitte", "function": "Durchmesser", "unit": "mm", "target_value": 9.0, "upper_tolerance":
            0.1, "lower_tolerance": -0.1, "warning_limit": 100.0, "control_limit": 1.0,
            "inspection_equipement": "PlatzhalterEquipment", "references": [{"id_short": "reference1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "point": "Platzhalter
            point", "line": "Platzhalter line", "surface": "Platzhalter surface", "axis": "Platzhalter
            axis"}], "sample_batch": [{"id_short": "sampleBatch1", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "sample_size": 1, "sample_data": [{"id_short":
            "sampleData1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "sample_number": 1223, "sample_date": "Platzhalter Datum", "part_counter": 1212, "result":
            [{"id_short": "result1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "value": 8.9973025, "measurement_date": "Platzhalte Datum Uhrzeit", "uppertol": 0.1,
            "lowertol": -0.1, "nominal": 9.0, "result_check": true}]}]}]}]}]}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: QualityDataAAS,
) -> Response[Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]]:
    """Post Item

    Args:
        json_body (QualityDataAAS):  Example: {"id_": "QualityDataAAS", "description": "xyz",
            "id_short": "QualityDataAAS", "quality_data": {"id_": "Submodel", "description": "xyz",
            "id_short": "QualityDataSubmodel", "semantic_id": "http://www.google.de/1",
            "production_procedures": [{"id_short": "ProductionProcedures", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "resource": "Platzhalter", "process":
            "Patzhalter", "features": [{"id_short": "Features", "description": "xyz", "semantic_id":
            "http://www.google.de/1", "quality_feature_name": [{"id_short": "qualityFeatureName1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "feature_type": "Zylinder
            Mitte", "function": "Durchmesser", "unit": "mm", "target_value": 9.0, "upper_tolerance":
            0.1, "lower_tolerance": -0.1, "warning_limit": 100.0, "control_limit": 1.0,
            "inspection_equipement": "PlatzhalterEquipment", "references": [{"id_short": "reference1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "point": "Platzhalter
            point", "line": "Platzhalter line", "surface": "Platzhalter surface", "axis": "Platzhalter
            axis"}], "sample_batch": [{"id_short": "sampleBatch1", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "sample_size": 1, "sample_data": [{"id_short":
            "sampleData1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "sample_number": 1223, "sample_date": "Platzhalter Datum", "part_counter": 1212, "result":
            [{"id_short": "result1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "value": 8.9973025, "measurement_date": "Platzhalte Datum Uhrzeit", "uppertol": 0.1,
            "lowertol": -0.1, "nominal": 9.0, "result_check": true}]}]}]}]}]}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: QualityDataAAS,
) -> Optional[Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]]:
    """Post Item

    Args:
        json_body (QualityDataAAS):  Example: {"id_": "QualityDataAAS", "description": "xyz",
            "id_short": "QualityDataAAS", "quality_data": {"id_": "Submodel", "description": "xyz",
            "id_short": "QualityDataSubmodel", "semantic_id": "http://www.google.de/1",
            "production_procedures": [{"id_short": "ProductionProcedures", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "resource": "Platzhalter", "process":
            "Patzhalter", "features": [{"id_short": "Features", "description": "xyz", "semantic_id":
            "http://www.google.de/1", "quality_feature_name": [{"id_short": "qualityFeatureName1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "feature_type": "Zylinder
            Mitte", "function": "Durchmesser", "unit": "mm", "target_value": 9.0, "upper_tolerance":
            0.1, "lower_tolerance": -0.1, "warning_limit": 100.0, "control_limit": 1.0,
            "inspection_equipement": "PlatzhalterEquipment", "references": [{"id_short": "reference1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "point": "Platzhalter
            point", "line": "Platzhalter line", "surface": "Platzhalter surface", "axis": "Platzhalter
            axis"}], "sample_batch": [{"id_short": "sampleBatch1", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "sample_size": 1, "sample_data": [{"id_short":
            "sampleData1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "sample_number": 1223, "sample_date": "Platzhalter Datum", "part_counter": 1212, "result":
            [{"id_short": "result1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "value": 8.9973025, "measurement_date": "Platzhalte Datum Uhrzeit", "uppertol": 0.1,
            "lowertol": -0.1, "nominal": 9.0, "result_check": true}]}]}]}]}]}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PostItemQualityDataAASPostResponsePostItemQualitydataaasPost]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
