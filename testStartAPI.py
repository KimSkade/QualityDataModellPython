from startAPI import start_api_with_pydantic_model
from testQualityData import example_QualityDataAAS

json_file = "simple_aas_and_submodels.json"
start_api_with_pydantic_model(example_QualityDataAAS, json_file)

