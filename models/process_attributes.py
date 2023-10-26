from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List
from enum import Enum
from basyx.aas.model.base import Identifier
from basyx.aas.model.base import Reference



class PredicateTypeEnum (Enum):
    matching = "matching"
    max = "maximum"
    min = "minimum"


class AttributeValue (SubmodelElementCollection):
    minimum: Optional[float]
    maximum: Optional[float]


class AttributePredicate (SubmodelElementCollection):
    attribute_carrier: str  # reference element
    general_attribute: str  # reference element
    predicate_type: str  # kann gelöscht werden, eindeutig durch attribute_value
    attribute_value: AttributeValue

class AttributePredicates (Submodel):
    attribute_predicate: List[AttributePredicate]