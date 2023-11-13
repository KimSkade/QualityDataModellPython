from services.convert_timestamp_in_str import convert_timestamp_in_str
from services.testJSONeinlesen import load_features_from_json, timestamp_from_json

from aas2openapi_client.models import *


def put_new_process_data(json_file):
    loaded_features = load_features_from_json(json_file)
    features_data = loaded_features[0]
    feature_value_list = []
    for feature_name, feature_value in features_data.items():
        feature_value_list.append(feature_value)
    print(feature_value_list.__len__())
    new_value_process_data = NewValuesProcessData(
        id_short="new_data" + str(1),
        semantic_id="http://www.google.de/1",
        description="This are new process datas.",
        timestamp=convert_timestamp_in_str(timestamp_from_json(json_file)),
        value=feature_value_list,
    )
    process_data = ProcessData(
        id_short="process_data",
        semantic_id="http://www.google.de/1",
        description="Here new process data will be saved.",
        # process_data_type=feature_name,
        new_values=[new_value_process_data],
    )
    return process_data


json_file = "10785.json"

from aas2openapi_client import client
client = client.Client(base_url="http://127.0.0.1:8000")


process_data1 = put_new_process_data(json_file)
print(process_data1)

procedure_submodel = Procedure(
    id="bstring",
    id_short="ProcedureSubmodel",
    description="xyz",
    semantic_id="http://www.google.de/1",
    process_data_type='Koerperschall',
    process_data=process_data1,
)

from aas2openapi_client.api.quality_data_aas.put_item_quality_data_aas_item_id_procedure_put import sync
sync(client=client, item_id="12string", json_body=procedure_submodel)
