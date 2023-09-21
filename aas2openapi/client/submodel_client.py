from __future__ import annotations

import os
import asyncio
from typing import List
from dotenv import load_dotenv

from fastapi import HTTPException
import aas2openapi
from aas2openapi.client import aas_client
from aas2openapi.convert import convert_pydantic
from aas2openapi.models import base

from aas2openapi.util import client_utils


from ba_syx_submodel_repository_client import Client as SMClient
from ba_syx_submodel_repository_client.api.submodel_repository_api import delete_submodel_by_id, get_all_submodels, get_submodel_by_id, post_submodel, put_submodel_by_id
from basyx.aas import model

load_dotenv('.env')

AAS_SERVER_ADRESS = "http://" + os.getenv("AAS_SERVER_HOST") + ":" + os.getenv("AAS_SERVER_PORT")
SUBMODEL_SERVER_ADRESS = "http://" + os.getenv("SUBMODEL_SERVER_HOST") + ":" + os.getenv("SUBMODEL_SERVER_PORT")


async def get_basyx_submodel_from_server(submodel_id: str) -> model.Submodel:
    """
    Function to get a submodel from the server
    Args:
        submodel_id (str): id of the submodel
    Returns:
        model.Submodel: submodel retrieved from the server
    """
    client = SMClient(SUBMODEL_SERVER_ADRESS)
    base_64_id = client_utils.get_base64_from_string(submodel_id)
    submodel_data = await get_submodel_by_id.asyncio(
        client=client, submodel_identifier=base_64_id
    )
    return client_utils.transform_client_to_basyx_model(submodel_data.to_dict())


async def get_all_basyx_submodels_from_server(aas: model.AssetAdministrationShell) -> List[model.Submodel]:
    """
    Function to get all submodels from an AAS in basyx format
    Args:
        aas (model.AssetAdministrationShell): AAS to get submodels from
    Returns:
        List[model.Submodel]: List of basyx submodels retrieved from the server
    """
    submodels = []
    for submodel_reference in aas.submodel:
        basyx_submodel = await get_basyx_submodel_from_server(submodel_reference.key[0].value)
        submodels.append(basyx_submodel)
    return submodels


async def submodel_is_on_server(submodel_id: str) -> bool:
    """
    Function to check if a submodel with the given id is on the server
    Args:
        submodel_id (str): id of the submodel
    Returns:
        bool: True if submodel is on server, False if not
    """
    try:
        await get_submodel_from_server(submodel_id)
        return True
    except Exception as e:
        return False


async def post_submodel_to_server(pydantic_submodel: base.Submodel):
    """
    Function to post a submodel to the server
    Args:
        pydantic_submodel (base.Submodel): submodel to post
    Raises:
        HTTPException: If submodel with the given id already exists
    """
    if await submodel_is_on_server(pydantic_submodel.id_):
        raise HTTPException(
            status_code=400,
            detail=f"Submodel with id {pydantic_submodel.id_} already exists",
        )
    basyx_submodel = aas2openapi.convert_pydantic_model_to_submodel(pydantic_submodel)
    submodel_for_client = convert_pydantic.ClientModel(basyx_object=basyx_submodel)
    client = SMClient(SUBMODEL_SERVER_ADRESS)
    response = await post_submodel.asyncio(client=client, json_body=submodel_for_client)


async def put_submodel_to_server(submodel: base.Submodel):
    """
    Function to put a submodel to the server
    Args:
        submodel (base.Submodel): submodel to put
    Raises:
        HTTPException: If submodel with the given id does not exist
    """
    if not await submodel_is_on_server(submodel.id_):
        raise HTTPException(
            status_code=400, detail=f"Submodel with id {submodel.id_} does not exist"
        )
    basyx_submodel = aas2openapi.convert_pydantic_model_to_submodel(submodel)
    submodel_for_client = convert_pydantic.ClientModel(basyx_object=basyx_submodel)
    client = SMClient(SUBMODEL_SERVER_ADRESS)
    base_64_id = client_utils.get_base64_from_string(submodel.id_)
    response = await put_submodel_by_id.asyncio(
        submodel_identifier=base_64_id, client=client, json_body=submodel
    )


async def get_submodel_from_server(submodel_id: str) -> base.Submodel:
    """
    Function to get a submodel from the server
    Args:
        submodel_id (str): id of the submodel
    Returns:
        base.Submodel: submodel retrieved from the server
    """
    basyx_submodel = await get_basyx_submodel_from_server(submodel_id)
    model_data = aas2openapi.convert_sm_to_pydantic_model(basyx_submodel)
    return model_data


async def get_all_submodels_from_server() -> List[base.Submodel]:
    """
    Function to get all submodels from the server
    Returns:
        List[base.Submodel]: List of submodels retrieved from the server
    """
    client = SMClient(SUBMODEL_SERVER_ADRESS)
    submodel_data = asyncio.run(get_all_submodels.asyncio(client=client))
    model_data = []
    for submodel in submodel_data:
        model_data.append(aas2openapi.convert_sm_to_pydantic_model(submodel))
    return model_data


async def get_submodel_from_aas_id_and_class_name(aas_id: str, class_name: str) -> base.Submodel:
    """
    Function to get a submodel from the server based on the AAS id and the class name of the submodel
    Args:
        aas_id (str): id of the AAS
        class_name (str): class name of the submodel
    Raises:
        HTTPException: If submodel with the given class name does not exist for the given AAS
    Returns:
        base.Submodel: submodel retrieved from the server
    """
    basyx_aas = await aas_client.get_basyx_aas_from_server(aas_id)
    for basyx_submodel in basyx_aas.submodel:
        submodel_id = basyx_submodel.key[0].value
        submodel = await get_submodel_from_server(submodel_id)
        if submodel.__class__.__name__ == class_name:
            return submodel
    raise HTTPException(
        status_code=400,
        detail=f"Submodel with name {class_name} does not exist for AAS with id {aas_id}",
    )


async def delete_submodel_from_server(submodel_id: str):
    """
    Function to delete a submodel from the server
    Args:
        submodel_id (str): id of the submodel
    """
    client = SMClient(SUBMODEL_SERVER_ADRESS)
    base_64_id = client_utils.get_base64_from_string(submodel_id)
    await asyncio.run(
        delete_submodel_by_id.asyncio(client=client, submodel_identifier=base_64_id)
    )