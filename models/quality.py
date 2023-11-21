from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from models.procedure import Procedure
from models.resource import Resource
from models.production_times import ProductionTimes
from typing import Optional, List


class NewResults(SubmodelElementCollection):
    measurement_date: str
    value: float
    result_check: bool
    part_counter: str
    sample_number: Optional[str]


class Result(SubmodelElementCollection):
    new_results: List[NewResults]


class QualityFeature(SubmodelElementCollection):
    feature_type: str
    function: str
    inspection_equipment: str
    unit: str
    upper_warning_limit: float
    lower_warning_limit: float
    upper_control_limit: float
    lower_control_limit: float
    target_value: float
    upper_tolerance: float
    lower_tolerance: float
    sample_size: Optional[int]
    result: Result


class QualityData(Submodel):
    quality_feature: List[QualityFeature]


class QualityDataAAS(AAS):
    quality_data: QualityData
    procedure: Procedure
    resource: Resource
    production_times: ProductionTimes


