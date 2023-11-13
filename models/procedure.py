from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class NewValuesProcessData(SubmodelElementCollection):
    timestamp: str
    value: List[float]


class ProcessData(SubmodelElementCollection):
    new_values: List[NewValuesProcessData]


class Procedure(Submodel):
    process_data_type: str
    process_data: ProcessData



