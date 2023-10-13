from models import qualityDataListen
from txtEinlesen import getValuefromColumName


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
            sampleData=sampleDatas
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
            axis="Platzhalter axis"
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
            sampleBatch=sampleBatchs
        )
        qualityFeatureNames.append(qualityFeatureName)
        i += 1
    #  print(qualityFeatureNames[2])

    #  Features SubmodelElementCollection
    feature = qualityDataListen.Features(
        id_short="Features",
        semantic_id="http://www.google.de/1",
        description="xyz",
        qualityFeatureName=qualityFeatureNames
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
        features=features
    )
    productionProcedures = []
    productionProcedures.append(productionProcedure)

    #  QualityData Submodel
    qualityDataSubmodel = qualityDataListen.QualityData(
        id_="QualityDataSubmodel",
        id_short="QualityData",
        semantic_id="http://www.google.de/1",
        description="xyz",
        productionProcedures=productionProcedures
    )

    #  QualityDataAAS
    qualityDataAAS = qualityDataListen.QualityDataAAS(
        description="xyz",
        id_short="QualityDataAAS",
        id_="QualityDataAAS",
        qualityData=qualityDataSubmodel
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
        sampleData=sampleDatas
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
        axis="Platzhalter axis"
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
        sampleBatch=sampleBatchs
    )
    qualityFeatureNames.append(qualityFeatureName)

    #  print(qualityFeatureNames[2])

    #  Features SubmodelElementCollection
    feature = qualityDataListen.Features(
        id_short="Features",
        semantic_id="http://www.google.de/1",
        description="xyz",
        qualityFeatureName=qualityFeatureNames
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
        features=features
    )
    productionProcedures = []
    productionProcedures.append(productionProcedure)

    #  QualityData Submodel
    qualityDataSubmodel = qualityDataListen.QualityData(
        id_="QualityDataSubmodel",
        id_short="QualityData",
        semantic_id="http://www.google.de/1",
        description="xyz",
        productionProcedures=productionProcedures
    )

    #  QualityDataAAS
    qualityDataAAS = qualityDataListen.QualityDataAAS(
        description="xyz",
        id_short="QualityDataAAStest",
        id_="QualityDataAAS",
        qualityData=qualityDataSubmodel
    )

    return qualityDataAAS
