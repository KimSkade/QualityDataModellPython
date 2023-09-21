import subprocess
import json
from testExample import Product, ProcessModel, BillOfMaterial

# Definiere die Daten
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

data_dict= data.dict()
# Wandele die Python-Daten in ein JSON-Format um
json_data = json.dumps(data_dict)

print(json_data)