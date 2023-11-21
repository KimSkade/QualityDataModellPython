from aas2openapi_client import client

client = client.Client(base_url="http://127.0.0.1:8000")


# sync(client=client, item_id="12string", json_body=quality_data_submodel)

# my_data: models.QualityDataAAS = sync(client=client)
# response: Response[models.QualityDataAAS] = sync_detailed(client=client)

from convert_kmg_data import put_new_results

test = put_new_results(
    dateipfad="C:/Users/kim0_/OneDrive/Dokumente/Masterarbeit/PruefplanValidierungsbauteil1_17.txt",
    client=client,
    item_id="12string",
    breakpoint="END",
)
