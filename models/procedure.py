from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List
from datetime import datetime
from models import processAttributes, product, resource, qualityDataListen


# NewPlantParameters Submodel
class NewValuesPlantParameter(SubmodelElementCollection):
    timestamp: int       # passt datetime?
    value: List[float]


class NewPlantParameterData(SubmodelElementCollection):
    newValuesPlantParameter: List[NewValuesPlantParameter]


class NewPlantParameter(Submodel):
    newPlantParameter: NewPlantParameterData


# ProcessDatas Submodel
class NewValuesProcessData(SubmodelElementCollection):
    timestamp: int       # passt datetime?
    value: List[float]


class ProcessData(SubmodelElementCollection):
    processDataType: str
    newValues: List[NewValuesProcessData]


class ProcessDatas(Submodel):
    processData: List[ProcessData]


# Procedure AAS
class Procedure(AAS):
    product: product.Product
    resource: resource.Resource
    processAttributes: processAttributes.AttributePredicates
    newPlantParameters: NewPlantParameter
    processDatas: ProcessDatas
    # qualityData: qualityDataListen.QualityData

