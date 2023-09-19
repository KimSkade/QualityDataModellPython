from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from typing import Optional


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
    result: Result


class SampleBatch(SubmodelElementCollection):
    sampleSize: int
    sampleData: SampleData


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
    references: References
    sampleBatch: SampleBatch


class Features(SubmodelElementCollection):
    qualityFeatureName: QualityFeatureName


class ProductionProcedures(SubmodelElementCollection):
    resource: str  # resources AAS verwenden?
    process: str  # process AAS verwenden?
    features: Features


class QualityData(Submodel):
    productionProcedures: ProductionProcedures


class QualityDataAAS(AAS):
    qualityData: QualityData
