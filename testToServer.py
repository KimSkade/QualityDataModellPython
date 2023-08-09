import aas2openapi
from testQualityData import createAASQualityDatafromKMG
from aas2openapi.middleware import Middleware
import basyx.aas.adapter.json.json_serialization
import uvicorn


dateipfad = "C:\\Users\\kim0_\\Desktop\\Masterarbeit\\PruefplanValidierungsbauteil1_16.txt"
breakpoint = "END"
example_QualityDataAAS = createAASQualityDatafromKMG(dateipfad, breakpoint)


obj_store = aas2openapi.convert_pydantic_model_to_aas(example_QualityDataAAS)
with open("simple_aas_and_submodels.json", "w", encoding="utf-8") as json_file:
    basyx.aas.adapter.json.write_aas_json_file(json_file, obj_store)


middleware = Middleware()
middleware.load_pydantic_model_instances([example_QualityDataAAS])
middleware.generate_rest_api()
middleware.generate_graphql_api()

app = middleware.app
uvicorn.run(app)
