from models import qualityDataListen
from txtEinlesen import getValuefromColumName

from aas2openapi_client import models


def createAASQualityDatafromKMG(dateipfad, breakpoint):
    i = 1
    results = []
    sampleDatas = []
    sampleBatchs = []
    references = []
    qualityFeatureNames = []
    while breakpoint != getValuefromColumName(dateipfad, "planid", i):
        #  results SubmodelElementCollections
        result = qualityDataListen.Result(
            id_short="result" + str(i),
            semantic_id="http://www.google.de/1",
            description="xyz",
            value=float(getValuefromColumName(dateipfad, "actual", i)),
            measurementDate="Platzhalte Datum Uhrzeit",  # Quelle MeasureDate
            uppertol=float(getValuefromColumName(dateipfad, "uppertol", i)),
            lowertol=float(getValuefromColumName(dateipfad, "lowertol", i)),
            nominal=float(getValuefromColumName(dateipfad, "nominal", i)),
            resultCheck=True,  # Formel für ResultCheck anpassen
        )
        results.append(result)
        #  print(result)

        #  sampleDatas SubmodelElementCollections
        sampleData = qualityDataListen.SampleData(
            id_short="sampleData" + str(i),
            semantic_id="http://www.google.de/1",
            description="xyz",
            sampleNumber=1223,
            sampleDate="Platzhalter Datum",
            partCounter=1212,
            result=results
            #  result=results[i-1]
        )
        sampleDatas.append(sampleData)

        #  sampleDatas SubmodelElementCollections
        sampleBatch = qualityDataListen.SampleBatch(
            id_short="sampleBatch" + str(i),
            semantic_id="http://www.google.de/1",
            description="xyz",
            sampleSize=1,
            sampleData=sampleDatas,
        )
        sampleBatchs.append(sampleBatch)

        #  references SubmodelElementCollections
        reference = qualityDataListen.References(
            id_short="reference" + str(i),
            semantic_id="http://www.google.de/1",
            description="xyz",
            point="Platzhalter point",
            line="Platzhalter line",
            surface="Platzhalter surface",
            axis="Platzhalter axis",
        )
        references.append(reference)

        #  qualityFeatureNames SubmodelElementCollections
        qualityFeatureName = qualityDataListen.QualityFeatureName(
            id_short="qualityFeatureName" + str(i),
            semantic_id="http://www.google.de/1",
            description="xyz",
            featureType=getValuefromColumName(dateipfad, "featureid", i),
            function=getValuefromColumName(dateipfad, "type", i),
            unit=getValuefromColumName(dateipfad, "unit", i),
            targetValue=float(getValuefromColumName(dateipfad, "nominal", i)),
            upperTolerance=float(getValuefromColumName(dateipfad, "uppertol", i)),
            lowerTolerance=float(getValuefromColumName(dateipfad, "lowertol", i)),
            warningLimit=float(getValuefromColumName(dateipfad, "warningLimitCF", i)),
            controlLimit=1,
            inspectionEquipement="PlatzhalterEquipment",
            references=references,
            sampleBatch=sampleBatchs,
        )
        qualityFeatureNames.append(qualityFeatureName)
        i += 1
    #  print(qualityFeatureNames[2])

    #  Features SubmodelElementCollection
    feature = qualityDataListen.Features(
        id_short="Features",
        semantic_id="http://www.google.de/1",
        description="xyz",
        qualityFeatureName=qualityFeatureNames,
    )
    features = []
    features.append(feature)

    #  ProductionProcedures SubmodelElementCollection
    productionProcedure = qualityDataListen.ProductionProcedures(
        id_short="ProductionProcedures",
        semantic_id="http://www.google.de/1",
        description="xyz",
        resource="Platzhalter",
        process="Patzhalter",
        features=features,
    )
    productionProcedures = []
    productionProcedures.append(productionProcedure)

    #  QualityData Submodel
    qualityDataSubmodel = qualityDataListen.QualityData(
        id_="QualityDataSubmodel",
        id_short="QualityData",
        semantic_id="http://www.google.de/1",
        description="xyz",
        productionProcedures=productionProcedures,
    )

    #  QualityDataAAS
    qualityDataAAS = qualityDataListen.QualityDataAAS(
        description="xyz", id_short="QualityDataAAS", id_="QualityDataAAS", qualityData=qualityDataSubmodel
    )

    return qualityDataAAS


# für eine Spalte:
def createAASQualityDatafromOneRowKMG(dateipfad):
    i = 1
    results = []
    sampleDatas = []
    sampleBatchs = []
    references = []
    qualityFeatureNames = []

    #  results SubmodelElementCollections
    result = models.result.Result(
        id_short="result" + str(i),
        semantic_id="http://www.google.de/1",
        description="xyz",
        value=float(getValuefromColumName(dateipfad, "actual", i)),
        measurement_date="Platzhalte Datum Uhrzeit",  # Quelle MeasureDate
        uppertol=float(getValuefromColumName(dateipfad, "uppertol", i)),
        lowertol=float(getValuefromColumName(dateipfad, "lowertol", i)),
        nominal=float(getValuefromColumName(dateipfad, "nominal", i)),
        result_check=True,  # Formel für ResultCheck anpassen
    )
    results.append(result)
    #  print(result)

    #  sampleDatas SubmodelElementCollections
    sampleData = models.sample_data.SampleData(
        id_short="sampleData" + str(i),
        semantic_id="http://www.google.de/1",
        description="xyz",
        sample_number=1223,
        sample_date="Platzhalter Datum",
        part_counter=1212,
        result=results
        #  result=results[i-1]
    )
    sampleDatas.append(sampleData)

    #  sampleDatas SubmodelElementCollections
    sampleBatch = models.sample_batch.SampleBatch(
        id_short="sampleBatch" + str(i),
        semantic_id="http://www.google.de/1",
        description="xyz",
        sample_size=1,
        sample_data=sampleDatas,
    )
    sampleBatchs.append(sampleBatch)

    #  references SubmodelElementCollections
    reference = models.references.References(
        id_short="reference" + str(i),
        semantic_id="http://www.google.de/1",
        description="xyz",
        point="Platzhalter point",
        line="Platzhalter line",
        surface="Platzhalter surface",
        axis="Platzhalter axis",
    )
    references.append(reference)

    #  qualityFeatureNames SubmodelElementCollections
    qualityFeatureName = models.quality_feature_name.QualityFeatureName(
        id_short="qualityFeatureName" + str(i),
        semantic_id="http://www.google.de/1",
        description="xyz",
        feature_type=getValuefromColumName(dateipfad, "featureid", i),
        function=getValuefromColumName(dateipfad, "type", i),
        unit=getValuefromColumName(dateipfad, "unit", i),
        target_value=float(getValuefromColumName(dateipfad, "nominal", i)),
        upper_tolerance=float(getValuefromColumName(dateipfad, "uppertol", i)),
        lower_tolerance=float(getValuefromColumName(dateipfad, "lowertol", i)),
        warning_limit=float(getValuefromColumName(dateipfad, "warningLimitCF", i)),
        control_limit=1,
        inspection_equipement="PlatzhalterEquipment",
        references=references,
        sample_batch=sampleBatchs,
    )
    qualityFeatureNames.append(qualityFeatureName)

    #  print(qualityFeatureNames[2])

    #  Features SubmodelElementCollection
    feature = models.features.Features(
        id_short="Features",
        semantic_id="http://www.google.de/1",
        description="xyz",
        quality_feature_name=qualityFeatureNames,
    )
    features = []
    features.append(feature)

    #  ProductionProcedures SubmodelElementCollection
    productionProcedure = models.ProductionProcedures(
        id_short="ProductionProcedures",
        semantic_id="http://www.google.de/1",
        description="xyz",
        resource="Platzhalter",
        process="Patzhalter",
        features=features,
    )
    productionProcedures = []
    productionProcedures.append(productionProcedure)

    #  QualityData Submodel
    qualityDataSubmodel = models.QualityData(
        id="QualityDataSubmodel",
        id_short="QualityData",
        semantic_id="http://www.google.de/1",
        description="xyz",
        production_procedures=productionProcedures,
    )

    #  QualityDataAAS
    qualityDataAAS = models.QualityDataAAS(
        description="xyz", id_short="QualityDataAAS", id="QualityDataAAS", quality_data=qualityDataSubmodel
    )

    return qualityDataAAS
