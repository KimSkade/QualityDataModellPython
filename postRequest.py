import subprocess
import json
from testExample import Product, ProcessModel, BillOfMaterial

# pydantic model
data = Product(
    id_="bc2119e48d0",
    process_model=ProcessModel(
        id_="a8cd10ed",
        processes=["join", "screw"], result_check=False,
    ),
    bill_of_material=BillOfMaterial(
        id_="a7cba3bcd", components=["stator", "rotor", "coil", "bearing"], result_check=True,
    ),
)


# convert pydantic model to dict
data_dict = data.dict()
# convert dict to JSON
json_data = json.dumps(data_dict)


# POST-Request
command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-d', json_data,  # Verwende das JSON-Datenobjekt hier
    'http://127.0.0.1:8000/Product/'
]

try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Fehler beim Ausführen des Befehls: {e}")
