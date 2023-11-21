from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class NewValuesProcessData(SubmodelElementCollection):
    timestamp: str
    values: List[float]


class ProcessData(SubmodelElementCollection):
    process_data_resource: str
    features_list: List[str]
    new_values: List[NewValuesProcessData]


class Procedure(Submodel):
    process_data: ProcessData



