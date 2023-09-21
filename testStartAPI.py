import startAPI
from testExample import example_product

json_file = "simple_aas_and_submodels.json"
startAPI.start_api_with_pydantic_model(example_product, json_file)
