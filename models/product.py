from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class TargetValue (SubmodelElementCollection):
    value: float
    value_description: str


class Product (Submodel):
    target_value: List[TargetValue]


