from models.qualityDataListen import QualityDataAAS, SampleData, QualityFeatureName, QualityData, SampleBatch, Features, Result, References, ProductionProcedures


result1 = Result(id_short='result1', description='xyz', semantic_id='http://www.google.de/1', value=8.9973025,
                  measurementDate='Platzhalte Datum Uhrzeit', uppertol=0.1, lowertol=-0.1, nominal=9.0, resultCheck=True)

sampleData1 = SampleData(id_short='sampleData1', description='xyz', semantic_id='http://www.google.de/1',
                        sampleNumber=1223, sampleDate='Platzhalter Datum', partCounter=1212, result=[result1])

sampleBatch1 = SampleBatch(id_short='sampleBatch1', description='xyz', semantic_id='http://www.google.de/1',
                          sampleSize=1, sampleData=[sampleData1])

references1 = References(id_short='reference1', description='xyz', semantic_id='http://www.google.de/1',
                        point='Platzhalter point', line='Platzhalter line', surface='Platzhalter surface', axis='Platzhalter axis')

qualityFeatureName1 = QualityFeatureName(id_short='qualityFeatureName1', description='xyz', semantic_id='http://www.google.de/1',
                                        featureType='Zylinder Mitte', function='Durchmesser', unit='mm', targetValue=9.0,
                                        upperTolerance=0.1, lowerTolerance=-0.1, warningLimit=100.0, controlLimit=1.0,
                                        inspectionEquipement='PlatzhalterEquipment', references=[references1],
                                        sampleBatch=[sampleBatch1])

features1 = Features(id_short='Features', description='xyz', semantic_id='http://www.google.de/1',
                    qualityFeatureName=[qualityFeatureName1])

productionProcedures1 = ProductionProcedures(id_short='ProductionProcedures', description='xyz',
                                            semantic_id='http://www.google.de/1', resource='Platzhalter',
                                            process='Patzhalter', features=[features1])

qualityDataSubmodel = QualityData(id_='Submodel', id_short='QualityDataSubmodel', description='xyz',
                                          semantic_id='http://www.google.de/1', productionProcedures=[productionProcedures1])

example2_qualityDataAAS = QualityDataAAS(id_='QualityDataAAS', description='xyz', id_short='QualityDataAAS',
                          qualityData=qualityDataSubmodel, semantic_id='http://www.google.de/1')