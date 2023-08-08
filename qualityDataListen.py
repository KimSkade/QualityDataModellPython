from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional, List


class Result(SubmodelElementCollection):
    value: float
    measurementDate: str  # Typ anpassen #Time Stamp
    uppertol: float
    lowertol: float
    nominal: float
    resultCheck: bool


class SampleData(SubmodelElementCollection):
    sampleNumber: int
    sampleDate: str
    partCounter: int
    result: List[Result]


class SampleBatch(SubmodelElementCollection):
    sampleSize: int
    sampleData: List[SampleData]


class References(SubmodelElementCollection):
    point: Optional[str]
    line: Optional[str]
    surface: Optional[str]
    axis: Optional[str]


class QualityFeatureName(SubmodelElementCollection):
    featureType: str
    function: str
    unit: str
    targetValue: float
    upperTolerance: float
    lowerTolerance: float
    warningLimit: float
    controlLimit: float
    inspectionEquipement: str
    references: List[References]
    sampleBatch: List[SampleBatch]


class Features(SubmodelElementCollection):
    qualityFeatureName: List[QualityFeatureName]


class ProductionProcedures(SubmodelElementCollection):
    resource: str  # resources AAS verwenden?
    process: str  # process AAS verwenden?
    features: List[Features]


class QualityData(Submodel):
    productionProcedures: List[ProductionProcedures]


class QualityDataAAS(AAS):
    qualityData: QualityData


