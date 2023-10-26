from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from models.procedure import ProcedureData
from typing import Optional, List


class NewResults(SubmodelElementCollection):
    measurement_date: str
    value: float
    result_check: bool
    part_counter: str
    sample_number: Optional[str]


class Result(SubmodelElementCollection):
    new_results: List[NewResults]


class QualityFeatureName(SubmodelElementCollection):
    feature_type: str
    function: str
    inspection_equipment: str
    unit: str
    warning_limit: float
    control_limit: float
    sample_size: Optional[int]
    result: Result


class Features(SubmodelElementCollection):
    quality_feature_name: List[QualityFeatureName]


class ProductionProcedures(SubmodelElementCollection):
    # list_procedures: List[ProcedureData]
    features: Features


class QualityData(Submodel):
    production_procedures: List[ProductionProcedures]


class QualityDataAAS(AAS):
    quality_data: QualityData

