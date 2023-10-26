from aas2openapi_client import client
from aas2openapi_client.api.quality_data_aas.post_item_quality_data_aas_post import sync, sync_detailed
from aas2openapi_client.models import *
from aas2openapi_client.types import Response
from KMGdata_to_QualityData_client import put_kmg_data
from aas2openapi_client.models.quality_data import QualityData

quality_feature_name = put_kmg_data('C:/Users/kim0_/OneDrive/Dokumente/Masterarbeit/PruefplanValidierungsbauteil1_16.txt', 'END')

features = Features(
    id_short="Features",
    description="xyz",
    semantic_id="http://www.google.de/1",
    quality_feature_name=quality_feature_name,
)

production_procedures1 = ProductionProcedures(
    id_short="ProductionProcedures",
    description="xyz",
    semantic_id="http://www.google.de/1",
    features=features,
)




quality_data_submodel = QualityData(
    id="string",
    id_short="QualityDataSubmodel",
    description="xyz",
    semantic_id="http://www.google.de/1",
    production_procedures=[production_procedures1],
)


client = client.Client(base_url="http://127.0.0.1:8000")



from aas2openapi_client.api.quality_data_aas.put_item_quality_data_aas_item_id_quality_data_put import sync
sync(client=client, item_id='12string', json_body=quality_data_submodel)

#my_data: models.QualityDataAAS = sync(client=client)
#response: Response[models.QualityDataAAS] = sync_detailed(client=client)

test = quality_data_submodel.to_dict()
print(test)
