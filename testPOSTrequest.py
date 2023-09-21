import postRequest
from testExample import example_product


example_product_JSON = postRequest.convert_pydantic_model_to_json(example_product)
url = 'http://127.0.0.1:8000/Product/'
postRequest.post_json_data_to_url(example_product_JSON, url)
