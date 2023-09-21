import aas2openapi_client
from aas2openapi_client.models import  product
from aas2openapi_client.api.product import post_item_product_post

client = aas2openapi_client.Client(base_url="http://localhost:8080")

# Anfrage senden

example_product = {Product(}
    id_="TEST100",
    process_model=ProcessModel(
        id_="a8cd10ed",
        processes=["join", "screw"], result_check=False,
    ),
    bill_of_material=BillOfMaterial(
        id_="a7cba3bcd", components=["stator", "rotor", "coil", "bearing"], result_check=True,
    ),
}

response = post_item_product_post.sync(Client=client, json_body=example_product)