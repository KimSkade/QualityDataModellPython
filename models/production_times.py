from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class PartProductionTime(SubmodelElementCollection):
    timestamp: str
    part_counter: int


class ProductionTimes (Submodel):
    part_production_times: List[PartProductionTime]


