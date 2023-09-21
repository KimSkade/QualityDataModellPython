import subprocess
import json
from testExample import Product, ProcessModel, BillOfMaterial


# convert pydantic model to JSON
def convert_pydantic_model_to_json(data):
    data_dict = data.dict()     # convert pydantic model to dict
    json_data = json.dumps(data_dict)       # convert dict to JSON
    return json_data


# POST-Request
def post_json_data_to_url(json_data, url):
    # Erstelle den Curl-Command
    command = [
        'curl',
        '-X', 'POST',
        '-H', 'Content-Type: application/json',
        '-d', json_data,
        url
    ]

    try:
        # Führe den Curl-Command aus
        subprocess.run(command, check=True)
        print(f"POST-Request erfolgreich an {url} gesendet.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen des Befehls: {e}")

