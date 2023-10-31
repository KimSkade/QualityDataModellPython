from aas2openapi_client import client
from convert_kmg_data import post_new_results

client = client.Client(base_url="http://127.0.0.1:8000")
test = post_new_results(
    dateipfad="C:/Users/kim0_/OneDrive/Dokumente/Masterarbeit/PruefplanValidierungsbauteil1_16.txt",
    client=client,
    item_id="12string",
)
print(test)
