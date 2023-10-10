import KMGdata_to_QualityData_client
from aas2openapi_client.api.quality_data_aas.post_item_quality_data_aas_post import sync, sync_detailed
from aas2openapi_client import client
from aas2openapi_client.types import Response
from aas2openapi_client import models

example_QualityDataAAS = KMGdata_to_QualityData_client.createAASQualityDatafromOneRowKMG("PruefplanValidierungsbauteil1_16.txt")
test2 = models.QualityDataAAS.to_dict(example_QualityDataAAS)
print(example_QualityDataAAS)
print(test2)

client = client.Client(base_url="http://127.0.0.1:8000")
sync(client=client, json_body=example_QualityDataAAS)


from aas2openapi_client.api.quality_data_aas.get_items_quality_data_aas_get import sync, sync_detailed
my_data: models.QualityDataAAS = sync(client=client)
response: Response[models.QualityDataAAS] = sync_detailed(client=client)
