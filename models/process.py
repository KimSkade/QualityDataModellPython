from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List
from models import processAttributes, processModel


class Process (Submodel):
    processAttributes: List[processAttributes.AttributePredicate]
