from startAPI import start_api_with_pydantic_model
from testExample import example_product

json_file = "simple_aas_and_submodels.json"
start_api_with_pydantic_model(example_product, json_file)

