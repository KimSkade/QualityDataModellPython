from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List
from datetime import datetime
from models import process_attributes, product, resource


# NewMachineParameters Submodel
class NewValuesMachineParameter(SubmodelElementCollection):
    timestamp: str
    value: List[float]


class NewMachineParameter(SubmodelElementCollection):
    new_values_machine_parameter: List[NewValuesMachineParameter]


# ProcessDatas Submodel
class NewValuesProcessData(SubmodelElementCollection):
    timestamp: str
    value: List[float]


class ProcessData(SubmodelElementCollection):
    process_data_type: str
    new_values: List[NewValuesProcessData]


class ProcessDatas(SubmodelElementCollection):
    process_data: List[ProcessData]


class ProcedureData(SubmodelElementCollection):
    new_machine_parameter: Optional[NewMachineParameter]
    process_data: ProcessDatas


# Procedure AAS
class Procedure(AAS):
    product: product.Product
    resource: resource.Resource
    process_attributes: process_attributes.AttributePredicates
    procedure_data: ProcedureData

