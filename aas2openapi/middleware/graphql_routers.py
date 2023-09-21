from aas2openapi.client.aas_client import get_aas_from_server, get_all_aas_from_server
from aas2openapi.convert.convert_pydantic import get_vars
from aas2openapi.models import base
from aas2openapi.util import convert_util
from aas2openapi.util.convert_util import get_all_submodel_elements_from_submodel, get_all_submodels_from_model

import typing

import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.experimental.pydantic.conversion_types import (
        PydanticModel,
        StrawberryTypeFromPydantic,
    )
from fastapi import APIRouter
from pydantic import BaseModel, create_model
from pydantic.fields import ModelField
from pydantic import BaseConfig, validator


from typing import List, Type

class Config(BaseConfig):
    arbitrary_types_allowed = True
    def prepare_field(self):
        pass

def convert_union_types_to_str(model_cls: Type[BaseModel]) -> Type[BaseModel]:
    """
    Converts all union types in the given pydantic model to str and adds a validator to the model to convert the values to str.

    Args:
        model_cls (Type[BaseModel]): Pydantic model for which the union types should be converted to str.

    Returns:
        Type[BaseModel]: Pydantic model with all union types converted to str.
    """
    new_model = create_model(__model_name=model_cls.__name__, __base__=model_cls)
    fields_requiring_post_validation = []
    new_type_dict = {}
    for field_name, field in new_model.__fields__.items():
        if isinstance(field, ModelField) and (field.type_ == typing._UnionGenericAlias or (hasattr(field.type_, "__origin__") and field.type_.__origin__ is typing.Union)):
            field.type_ = str
            field.default = ""
            fields_requiring_post_validation.append(field_name)
        new_type_dict[field_name] = (field.outer_type_, field.default if field.default else ...)
    def convert_to_str(cls, v):
        return str(v)
    validators = {
    'field_validator': validator(field_name, pre=True, always=True, allow_reuse=True)(convert_to_str) for field_name in fields_requiring_post_validation
    }
    newer_model = create_model(__model_name=model_cls.__name__, **new_type_dict, __config__=Config, __validators__=validators)
    return newer_model


def generate_strawberry_type_for_model(model: Type[BaseModel]) -> StrawberryTypeFromPydantic:
    """
    Generates a strawberry type for the given pydantic model.

    Args:
        model (Type[BaseModel]): Pydantic model for which the strawberry type should be generated.

    Returns:
        strawberry.type: Strawberry type for the given pydantic model.
    """
    # conversion of union types to str is necessary for strawberry to work!
    model = convert_union_types_to_str(model)
    class_name = model.__name__ + "Type"
    @strawberry.experimental.pydantic.type(model=model, all_fields=True, name=class_name)
    class StrawberryModel:
        pass
    StrawberryModel.__name__ = class_name
    StrawberryModel.__qualname__ = class_name
    return StrawberryModel

def update_type_with_field(type_: Type[BaseModel], field_name: str, field_type: StrawberryTypeFromPydantic | list | str | bool | float | int):
    """
    Updates the  type of a given field of a type.

    Args:
        type_ (Type[BaseModel]): type of which the field type should be updated.
        field_name (str): Name of the field which should be updated.
        field_type (StrawberryTypeFromPydantic | list | str | bool | float | int): New type of the field.
    """
    # TODO: fix problems with typing.List!
    field = ModelField(
            name=field_name,
            type_=field_type,
            class_validators=None,
            model_config=Config,
    )
    type_.__fields__.update({
        field_name: field
    })

def create_new_smc(smc: Type[base.SubmodelElementCollection]) -> Type[BaseModel]:
    new_submodel_type = create_model(__model_name=smc.__name__, **base.SubmodelElementCollection.__annotations__)
    return new_submodel_type


def add_submodel_elements_to_submodel_type(submodel_type: Type[BaseModel], attribute_name, submodel_element_type: Type[BaseModel]):
    """
    Adds the given submodel element type to the given submodel type.

    Args:
        submodel_type (Type[BaseModel]): Submodel type to which the submodel element type should be added.
        attribute_name (_type_): Name of the attribute of the submodel type to which the submodel element type should be added.
        submodel_element_type (Type[BaseModel]): Submodel element type which should be added to the submodel type.
    """
    # try:
    if submodel_element_type._name == "List" or issubclass(submodel_element_type, list):
        if issubclass(submodel_element_type.__args__[0], base.SubmodelElementCollection):
            strawberry_submodel_element_class = generate_strawberry_type_for_model(submodel_element_type)
            add_submodel_elements_to_submodel_type(submodel_type, attribute_name, List[strawberry_submodel_element_class])
        else:
            update_type_with_field(submodel_type, attribute_name, submodel_element_type)
        return
    elif issubclass(submodel_element_type, base.SubmodelElementCollection):
        new_smc = create_new_smc(submodel_element_type)
        strawberry_submodel_element_class = generate_strawberry_type_for_model(new_smc)
        update_type_with_field(submodel_type, attribute_name, strawberry_submodel_element_class)
        return
    # TODO: fox union types
    # except:
    #     print("Resolving Union type <", submodel_element_type, "> in <", submodel_type.__name__,"> for attribute <", attribute_name,"> to be considered as > str > type in GraphQL router.")
    update_type_with_field(submodel_type, attribute_name, submodel_element_type)

def generate_graphql_endpoint(models: List[Type[BaseModel]]) -> APIRouter:
    """
    Generates a GraphQL endpoint for the given pydantic models.
    Args:
        models (List[Type[BaseModel]]): List of pydantic models.
    Returns:
        APIRouter: FastAPI router with GraphQL endpoint for the given pydantic models.
    """
    for model in models:
        model_name = model.__name__
        model_type = create_model(__model_name=model_name, **base.AAS.__annotations__)
        
        submodels = get_all_submodels_from_model(model)
        for submodel in submodels:
            new_submodel_type = create_model(__model_name=submodel.__name__, **base.Submodel.__annotations__)
            sme_dict = get_all_submodel_elements_from_submodel(submodel)
            for sme_name, sme in sme_dict.items():
                add_submodel_elements_to_submodel_type(new_submodel_type, sme_name, sme)
            strawberry_submodel_class = generate_strawberry_type_for_model(new_submodel_type)
            attribute_name_of_submodel = convert_util.convert_camel_case_to_underscrore_str(new_submodel_type.__name__)
            update_type_with_field(model_type, attribute_name_of_submodel, strawberry_submodel_class)

        strawberry_aas_class = generate_strawberry_type_for_model(model_type)


        @strawberry.type
        class Query:
            @strawberry.field(name="get_" + model_name)
            async def get_model(self, id: str) -> strawberry_aas_class:
                aas = await get_aas_from_server(id)
                return strawberry_aas_class.from_pydantic(aas)
            
            @strawberry.field(name="get_all_" + model_name)
            async def get_all_models(self) -> List[strawberry_aas_class]:
                aas_list = await get_all_aas_from_server(model)
                return [strawberry_aas_class.from_pydantic(aas) for aas in aas_list]

    schema = strawberry.Schema(query=Query)
    return GraphQLRouter(schema, "/graphql")