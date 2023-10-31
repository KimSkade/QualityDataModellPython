import json


def load_features_from_json(json_file):
    features_list = []

    with open(json_file, "r") as file:
        data = json.load(file)

    if "d" in data and "features" in data["d"]:
        features_data = data["d"]["features"]
        features_list.append(features_data)

    return features_list


# json_file = "10785.json"
# loaded_features = load_features_from_json(json_file)
# print(loaded_features)


# maximale_Amplitude = loaded_features[0].get("Maximale_Amplitude_Rohsignal_0.0bis18.9s")
# print(maximale_Amplitude)


# if loaded_features:
    # features_data = loaded_features[0]
    # for feature_name, feature_value in features_data.items():
        # print(f"{feature_name}: {feature_value}")
        