from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class MachineParameter (SubmodelElementCollection):
    value_min: float
    value_max: float
    value_description: str


# NewMachineParameters SMC
class NewValuesMachineParameter(SubmodelElementCollection):
    timestamp: str
    value: List[float]


class NewMachineParameter(SubmodelElementCollection):
    new_values_machine_parameter: List[NewValuesMachineParameter]


class Resource (Submodel):
    machine_parameter: List[MachineParameter]
    new_machine_parameter: NewMachineParameter
