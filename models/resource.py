from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class PlantParameter (SubmodelElementCollection):
    valueMin: float
    valueMax: float
    valueDescription: str


class Resource (Submodel):
    plantParameter: List[PlantParameter]
