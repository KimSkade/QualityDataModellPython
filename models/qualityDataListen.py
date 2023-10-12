from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class Result(SubmodelElementCollection):
    value: float
    measurement_date: str  # Typ anpassen #Time Stamp
    uppertol: float
    lowertol: float
    nominal: float
    result_check: bool


class SampleData(SubmodelElementCollection):
    sample_number: int
    sample_date: str
    part_counter: int
    result: List[Result]


class SampleBatch(SubmodelElementCollection):
    sample_size: int
    sample_data: List[SampleData]


class References(SubmodelElementCollection):
    point: Optional[str]
    line: Optional[str]
    surface: Optional[str]
    axis: Optional[str]


class QualityFeatureName(SubmodelElementCollection):
    feature_type: str
    function: str
    unit: str
    target_value: float
    upper_tolerance: float
    lower_tolerance: float
    warning_limit: float
    control_limit: float
    inspection_equipement: str
    references: List[References]
    sample_batch: List[SampleBatch]


class Features(SubmodelElementCollection):
    quality_feature_name: List[QualityFeatureName]


class ProductionProcedures(SubmodelElementCollection):
    resource: str  # resources AAS verwenden?
    process: str  # process AAS verwenden?
    features: List[Features]


class QualityData(Submodel):
    production_procedures: List[ProductionProcedures]


class QualityDataAAS(AAS):
    quality_data: QualityData
