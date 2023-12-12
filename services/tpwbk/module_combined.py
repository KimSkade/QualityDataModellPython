import os
import json
from feature_selection import create_feature_baseline, select_features
from downsampling import downsample, process_chunk
from anomaly_detection import detect_anomalies_statistical
from feature_extraction import generate_features


def process_h5_file(hdf5_path, dataset_path, output_json_path, n_samples=1000000):
    """
    Verarbeitet eine HDF5-Datei mit Downsampling, Anomalieerkennung und Merkmalsextraktion
    und speichert das Ergebnis als JSON.
    :param hdf5_path: Pfad zur HDF5-Datei
    :param dataset_path: Pfad zum Datensatz innerhalb der HDF5-Datei
    :param output_json_path: Pfad, wo das JSON-Ergebnis gespeichert werden soll
    :param n_samples: Anzahl der Stichproben nach dem Downsampling
    """

    # Abrufen der Argumente für das Downsampling
    df_sampled = downsample(hdf5_path, dataset_path, n_samples)

    # Anomalieerkennung
    df_anomaly_detected, _ = detect_anomalies_statistical(df_sampled, window_size=50, sigma_count_threshold=2)

    # Merkmalsextraktion
    df_features_all = generate_features(df_anomaly_detected)

    # Feature Baseline Lesen
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, 'selected_features')
    with open(data_dir, 'r') as file:
        feature_baseline = json.load(file)

    df_features_selected = select_features(df_features_all, feature_baseline)

    json_data = {
        "t": 1697192247000,  # Beispiel-Timestamp (ersetzen Sie diesen durch echte Daten)
        "d": {
            "qass_nr": 10785,  # Beispiel-QASS-Nummer (ersetzen Sie diese durch echte Daten)
            "features": df_features_selected.to_dict(orient='records')[0],
            "productId": "21039093_6391374_01_129624_000",  # Beispiel-Produkt-ID (ersetzen Sie diese durch echte Daten)
            "toolId": "F409650-15 Dia",  # Beispiel-Werkzeug-ID (ersetzen Sie diese durch echte Daten)
            "toolCondition": "A0",  # Beispiel-Werkzeugzustand (ersetzen Sie diesen durch echte Daten)
            "shiftPosition": 1,  # Beispiel-Schichtposition (ersetzen Sie diese durch echte Daten)
            "toolHolderClearance": 0.002,  # Beispiel-Werkzeughalterabstand (ersetzen Sie diesen durch echte Daten)
            "correctionValueY": 0.01,  # Beispiel-Korrekturwert Y (ersetzen Sie diesen durch echte Daten)
            "toolNumberOfCycles": 2349  # Beispiel-Werkzeugzyklenanzahl (ersetzen Sie diese durch echte Daten)
        }
    }

    # Speichern als JSON-Datei
    with open(output_json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

def process_directory(directory_path, dataset_path):
    """
    Scannt ein Verzeichnis nach HDF5-Dateien und verarbeitet jede Datei
    :param directory_path: Pfad zum Verzeichnis, das gescannt werden soll
    :param dataset_path: Pfad zum Datensatz innerhalb der HDF5-Dateien
    """
    for filename in os.listdir(directory_path):
        if filename.endswith('.h5'):
            hdf5_path = os.path.join(directory_path, filename)
            output_json_path = os.path.splitext(hdf5_path)[0] + '_selected_features.json'
            process_h5_file(hdf5_path, dataset_path, output_json_path)


# Hauptmethode zum Testen
if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(parent_dir, 'data')
    dataset_path = 'data/values'
    process_directory(data_dir, dataset_path)
