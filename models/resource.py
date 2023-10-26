from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class MachineParameter (SubmodelElementCollection):
    value_min: float
    value_max: float
    value_description: str


class Resource (Submodel):
    machine_parameter: List[MachineParameter]
