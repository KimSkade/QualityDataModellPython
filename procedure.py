import aas2openapi
from aas2openapi.middleware import Middleware
import basyx.aas.adapter.json.json_serialization
import uvicorn
import typing
from aas2openapi import models
from typing import Optional, List


class NewValuesAnlagenparameter(models.SubmodelElementCollection):
        timestamp: str        #  str tauschen
        value: List[float]


class NeueAnlagenparameter(models.SubmodelElementCollection):
    newValuesAnlagenparameter: List[NewValuesAnlagenparameter]


#  Ressource Submodel
class Anlagenparameter(models.SubmodelElementCollection):
    parameter: List[str]


class Ressource(models.Submodel):
    anlagenparameter: Anlagenparameter


#  Product Submodel
class SollDaten(models.SubmodelElementCollection):
    value: List[str]


class Product(models.Submodel):
    sollDaten: List[SollDaten]


#  Processdata Submodel
class NewValuesDruck(models.SubmodelElementCollection):
    timestamp: str      #  str tauschen
    value: List[float]


class Druck(models.SubmodelElementCollection):
    newValuesDruck: List[NewValuesDruck]


class Processdata(models.Submodel):
    druck: Druck


#  Procedure AAS
class Procedure(models.AAS):
    product: Product
    ressource: Ressource
    neueAnlagenparameter: List[NeueAnlagenparameter]
    processData: Processdata

