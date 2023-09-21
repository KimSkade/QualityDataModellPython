import aas2openapi
from aas2openapi.middleware import Middleware
import basyx.aas.adapter.json.json_serialization
import uvicorn
from testExample import example_product


obj_store = aas2openapi.convert_pydantic_model_to_aas(example_product)
with open("simple_aas_and_submodels.json", "w", encoding="utf-8") as json_file:
    basyx.aas.adapter.json.write_aas_json_file(json_file, obj_store)


middleware = Middleware()
middleware.load_pydantic_model_instances([example_product])
middleware.generate_rest_api()

app = middleware.app
uvicorn.run(app)

