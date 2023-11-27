from aas2openapi_client import client
from aas2openapi_client.api.quality_data_aas.post_item_quality_data_aas_post import sync
from aas2openapi_client.models.quality_data import QualityData
from convert_kmg_data import put_kmg_data

quality_feature = put_kmg_data(
    "C:/Users/kim0_/OneDrive/Dokumente/Masterarbeit/PruefplanValidierungsbauteil1_16.txt", "END"
)


quality_data_submodel = QualityData(
    id="astring",
    id_short="QualityDataSubmodel",
    description="xyz",
    semantic_id="http://www.google.de/1",
    quality_feature=quality_feature,
)


client = client.Client(base_url="http://127.0.0.1:8000")


from aas2openapi_client.api.quality_data_aas.put_item_quality_data_aas_item_id_quality_data_put import sync

# sync(client=client, item_id="12string", json_body=quality_data_submodel)

from convert_kmg_data import load_kmp_data_in_aas

load_kmp_data_in_aas(dateipfad="C:/Users/kim0_/OneDrive/Dokumente/Masterarbeit/PruefplanValidierungsbauteil1_17.txt", client=client, item_id="12string", breakpoint="END")




# my_data: models.QualityDataAAS = sync(client=client)
# response: Response[models.QualityDataAAS] = sync_detailed(client=client)


# test = post_new_results(dateipfad='aas2openapi-client/PruefplanValidierungsbauteil1_17.txt', client=client, item_id='12string')
