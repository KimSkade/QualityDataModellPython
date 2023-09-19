import aas2openapi
from aas2openapi.middleware import Middleware
import basyx.aas.adapter.json.json_serialization
import uvicorn
import typing
from aas2openapi import models


class BillOfMaterial(models.Submodel):
    components: typing.List[str]
    result_check: bool


class ProcessModel(models.Submodel):
    processes: typing.List[str]
    result_check: bool


class Product(models.AAS):
    bill_of_material: BillOfMaterial
    process_model: typing.Optional[ProcessModel]


example_product = Product(
    id_="bc2119e48d0",
    process_model=ProcessModel(
        id_="a8cd10ed",
        processes=["join", "screw"], result_check=False,
    ),
    bill_of_material=BillOfMaterial(
        id_="a7cba3bcd", components=["stator", "rotor", "coil", "bearing"], result_check=True,
    ),
)

obj_store = aas2openapi.convert_pydantic_model_to_aas(example_product)
with open("simple_aas_and_submodels.json", "w", encoding="utf-8") as json_file:
    basyx.aas.adapter.json.write_aas_json_file(json_file, obj_store)


middleware = Middleware()
middleware.load_pydantic_model_instances([example_product])
middleware.generate_rest_api()

app = middleware.app
uvicorn.run(app)

