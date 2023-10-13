from aas2openapi_client import client, models
from aas2openapi_client.api.quality_data_aas.post_item_quality_data_aas_post import sync, sync_detailed
from aas2openapi_client.types import Response
from aas2openapi_client.models import QualityDataAAS, SampleData, QualityFeatureName, QualityData, SampleBatch, Features, Result, References, ProductionProcedures


result1 = Result(id_short='result1', description='xyz', semantic_id='http://www.google.de/1', value=8.9973025,
                 measurement_date='Platzhalte Datum Uhrzeit', uppertol=0.1, lowertol=-0.1, nominal=9.0,
                 result_check=True)

sample_data1 = SampleData(id_short='sampleData1', description='xyz', semantic_id='http://www.google.de/1',
                          sample_number=1223, sample_date='Platzhalter Datum', part_counter=1212, result=[result1])

sample_batch1 = SampleBatch(id_short='sampleBatch1', description='xyz', semantic_id='http://www.google.de/1',
                            sample_size=1, sample_data=[sample_data1])

references1 = References(id_short='reference1', description='xyz', semantic_id='http://www.google.de/1',
                         point='Platzhalter point', line='Platzhalter line', surface='Platzhalter surface',
                         axis='Platzhalter axis')

quality_feature_name1 = QualityFeatureName(id_short='qualityFeatureName1', description='xyz',
                                           semantic_id='http://www.google.de/1',
                                           feature_type='Zylinder Mitte', function='Durchmesser', unit='mm',
                                           target_value=9.0,
                                           upper_tolerance=0.1, lower_tolerance=-0.1, warning_limit=100.0,
                                           control_limit=1.0,
                                           inspection_equipement='PlatzhalterEquipment', references=[references1],
                                           sample_batch=[sample_batch1])

features1 = Features(id_short='Features', description='xyz', semantic_id='http://www.google.de/1',
                     quality_feature_name=[quality_feature_name1])

production_procedures1 = ProductionProcedures(id_short='ProductionProcedures', description='xyz',
                                              semantic_id='http://www.google.de/1', resource='Platzhalter',
                                              process='Patzhalter', features=[features1])

quality_data_submodel = QualityData(id='Submodel', id_short='QualityDataSubmodel', description='xyz',
                                    semantic_id='http://www.google.de/1',
                                    production_procedures=[production_procedures1])

example3_quality_data_aas = QualityDataAAS(id='TestPOSTQualityDataAAS', description='xyz', id_short='QualityDataAAS',
                                           quality_data=quality_data_submodel)
test2 = models.QualityDataAAS.to_dict(example3_quality_data_aas)
print(example3_quality_data_aas)
print(test2)

client = client.Client(base_url="http://127.0.0.1:8000")
sync(client=client, json_body=example3_quality_data_aas)


from aas2openapi_client.api.quality_data_aas.get_items_quality_data_aas_get import sync, sync_detailed

my_data: models.QualityDataAAS = sync(client=client)
response: Response[models.QualityDataAAS] = sync_detailed(client=client)
