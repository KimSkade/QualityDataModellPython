import aas2openapi
import basyx.aas.adapter.json.json_serialization
import uvicorn
from aas2openapi.middleware import Middleware
from aas2openapi.models import AAS


def start_api_with_pydantic_model(aas_model: AAS, dateipfad_json: str):
    obj_store = aas2openapi.convert_pydantic_model_to_aas(aas_model)
    with open(dateipfad_json, "w", encoding="utf-8") as json_file:
        basyx.aas.adapter.json.write_aas_json_file(json_file, obj_store)

    middleware = Middleware()
    middleware.load_pydantic_model_instances([aas_model])
    middleware.generate_rest_api()

    app = middleware.app
    uvicorn.run(app, host='0.0.0.0', port=8000)



