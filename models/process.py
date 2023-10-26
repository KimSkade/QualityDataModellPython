from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List
from models import process_attributes, process_model


class Process (Submodel):
    process_attributes: List[process_attributes.AttributePredicate]
