from services.convert_timestamp_in_str import convert_timestamp_in_str
from services.read_json import load_features_from_json, timestamp_from_json
from services.id_generator import generate_unique_id

from aas2openapi_client.models import *
from aas2openapi_client import client
from aas2openapi_client.api.quality_data_aas.get_item_quality_data_aas_item_id_procedure_get import sync as get_sync
from aas2openapi_client.api.quality_data_aas.put_item_quality_data_aas_item_id_procedure_put import sync as put_sync


def put_new_process_data(json_file):
    loaded_features = load_features_from_json(json_file)
    features_data = loaded_features[0]
    feature_value_list = []
    feature_type_list = []
    for feature_name, feature_value in features_data.items():
        feature_value_list.append(feature_value)
        feature_type_list.append(feature_name)
    print(feature_value_list.__len__())
    new_value_process_data = NewValuesProcessData(
        id_short=generate_unique_id(),
        semantic_id="http://www.google.de/1",
        description="This are new process datas.",
        timestamp=convert_timestamp_in_str(timestamp_from_json(json_file) / 1000),
        values=feature_value_list,
    )
    process_data = ProcessData(
        id_short=generate_unique_id(),
        semantic_id="http://www.google.de/1",
        description="Here new process data will be saved.",
        process_data_resource="",
        features_list=feature_type_list,
        new_values=[new_value_process_data],
    )
    return process_data


def put_new_values_process_data(json_file, item_id, client):
    procedure_submodel=get_sync(item_id=item_id, client=client)

    loaded_features = load_features_from_json(json_file)
    features_data = loaded_features[0]
    feature_value_list = []
    for feature_value in features_data.items():
        feature_value_list.append(feature_value)
    print(feature_value_list.__len__())

    new_value_process_data = NewValuesProcessData(
        id_short=generate_unique_id(),
        semantic_id="http://www.google.de/1",
        description="This are new process datas.",
        timestamp=convert_timestamp_in_str(timestamp_from_json(json_file) / 1000),
        values=feature_value_list,
    )
    procedure_submodel.process_data.new_values.append(new_value_process_data)
    put_sync(item_id=item_id, client=client, json_body=procedure_submodel)


def load_sensor_features_in_aas(json_file, item_id, client):
    procedure_submodel: Procedure = get_sync(item_id=item_id, client=client)
    if procedure_submodel.process_data.features_list.__len__() == 1:
        procedure_submodel.process_data = put_new_process_data(json_file=json_file)
        put_sync(item_id=item_id, client=client, json_body=procedure_submodel)
    # wenn features_type_liste schon Werte:
    elif procedure_submodel.process_data.new_values.__len__() > 1:
        put_new_process_data(procedure_submodel)
    # sync detailed benutzen und je nach response handeln


json_file = "10785.json"
client = client.Client(base_url="http://127.0.0.1:8000")


process_data1 = put_new_process_data(json_file)

procedure_submodel = Procedure(
    id="bstring",
    id_short="ProcedureSubmodel",
    description="xyz",
    semantic_id="http://www.google.de/1",
    process_data=process_data1,
)


put_sync(client=client, item_id="12string", json_body=procedure_submodel)
