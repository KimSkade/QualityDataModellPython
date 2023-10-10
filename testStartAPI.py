from startAPI import start_api_with_pydantic_model
from testQualityData import example2_qualityDataAAS

json_file = "simple_aas_and_submodels.json"
start_api_with_pydantic_model(example2_qualityDataAAS, json_file)

