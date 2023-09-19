from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class TargetValue (SubmodelElementCollection):
    value: float
    valueDescription: str


class Product (Submodel):
    targetValue: List[TargetValue]


