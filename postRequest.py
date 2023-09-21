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

data_dict = data.dict()
# Wandele die Python-Daten in ein JSON-Format um
json_data = json.dumps(data_dict)


# Definiere den Befehl als Liste von Zeichenfolgen und verwende das JSON-Datenobjekt
command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-d', json_data,  # Verwende das JSON-Datenobjekt hier
    'http://127.0.0.1:8000/Product/'
]


# Führe den Befehl aus
try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Fehler beim Ausführen des Befehls: {e}")