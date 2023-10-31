from aas2openapi_client import client
from aas2openapi_client.api.quality_data_aas.post_item_quality_data_aas_post import sync
from aas2openapi_client.models import *
from aas2openapi_client.models.quality_data import QualityData
from convert_kmg_data import put_kmg_data
from json_procedure import put_new_process_data

quality_feature_name = put_kmg_data(
    "C:/Users/kim0_/OneDrive/Dokumente/Masterarbeit/PruefplanValidierungsbauteil1_16.txt", "END"
)

features = Features(
    id_short="Features",
    description="xyz",
    semantic_id="http://www.google.de/1",
    quality_feature_name=quality_feature_name,
)

json_file = "10785.json"
process_datas = ProcessDatas(
    id_short="process_datas",
    semantic_id="http://www.google.de/1",
    description="Here new proces data will be saved.",
    process_data=put_new_process_data(json_file),
)

procedure_data = ProcedureData(
    id_short="procedures_datas",
    semantic_id="http://www.google.de/1",
    description="Here new procedure data will be saved.",
    process_data=process_datas,
)

production_procedures1 = ProductionProcedures(
    id_short="ProductionProcedures",
    description="xyz",
    semantic_id="http://www.google.de/1",
    features=features,
    list_procedures=[procedure_data],
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

sync(client=client, item_id="12string", json_body=quality_data_submodel)

# my_data: models.QualityDataAAS = sync(client=client)
# response: Response[models.QualityDataAAS] = sync_detailed(client=client)


# test = post_new_results(dateipfad='aas2openapi-client/PruefplanValidierungsbauteil1_17.txt', client=client, item_id='12string')
