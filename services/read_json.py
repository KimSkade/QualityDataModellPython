import json


def load_features_from_json(json_file):
    features_list = []

    with open(json_file, "r") as file:
        data = json.load(file)

    if "d" in data and "features" in data["d"]:
        features_data = data["d"]["features"]
        features_list.append(features_data)

    return features_list


def timestamp_from_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    if "t" in data:
        timestamp = data["t"]
    return timestamp


