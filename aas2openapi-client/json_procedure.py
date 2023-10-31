from services.testJSONeinlesen import load_features_from_json

from aas2openapi_client.models import *


def put_new_process_data(json_file):
    loaded_features = load_features_from_json(json_file)
    features_data = loaded_features[0]
    process_data_list = []
    i = 1
    for feature_name, feature_value in features_data.items():
        new_value_process_data = NewValuesProcessData(
            id_short="new_data" + str(i),
            semantic_id="http://www.google.de/1",
            description="This are new process datas.",
            timestamp="Platzhalter",  # woher Wert
            value=feature_value,
        )
        process_data = ProcessData(
            id_short="process_data" + str(i),
            semantic_id="http://www.google.de/1",
            description="Here new proces data will be saved.",
            process_data_type=feature_value,
            new_values=[new_value_process_data],
        )
        process_data_list.append(process_data)
        i += 1
    return process_data_list


json_file = "10785.json"
process_datas = ProcessDatas(
    id_short="process_datas",
    semantic_id="http://www.google.de/1",
    description="Here new proces data will be saved.",
    process_data=put_new_process_data(json_file),
)
# print(process_datas.process_data)
