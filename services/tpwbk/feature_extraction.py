import pandas as pd
import tsfel
import multiprocessing
from itertools import repeat
import os

# Funktion zum Extrahieren von Merkmalen aus einem Datenblock
def extract_features(chunk, cfg):
    """
    Extrahiert Merkmale aus einem Datenblock unter Verwendung der TSFEL-Bibliothek
    :param chunk: Teil des df, aus dem Merkmale extrahiert werden sollen
    :param cfg: Konfiguration für die Extraktion der Merkmale von TSFEL
    :return: df mit extrahierten Merkmalen
    """
    # Verwende TSFEL, um Merkmale aus dem Datenblock zu extrahieren
    return tsfel.time_series_features_extractor(cfg, chunk, verbose=0)

def generate_features(df, chunk_size=10000):
    """
    Generiert Merkmale aus einem DataFrame und gibt die Features in einem DataFrame wieder
    :param df: DataFrame mit einer Spalte
    :param chunk_size: Größe der Datenblöcke für die Merkmalsextraktion.
    """

    # TSFEL-Konfiguration definieren
    cfg = tsfel.get_features_by_domain()

    # Bestimme die Anzahl der Blöcke
    n_chunks = (len(df) + chunk_size - 1) // chunk_size

    # Aufteilung des df in Blöcke
    chunks = [df[i * chunk_size:(i + 1) * chunk_size] for i in range(n_chunks)]

    # Verwenden von Multiprocessing, um jeden Block zu verarbeiten
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        results = pool.starmap(extract_features, zip(chunks, repeat(cfg)))

    # Zusammenführen der Ergebnisse
    extracted_features = pd.concat(results, ignore_index=True)

    return extracted_features


# Beispiel für den Aufruf der Funktion
if __name__ == '__main__':
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    csv_file_input = os.path.join(data_dir, 'sampled_data.csv')
    csv_file_output = os.path.join(data_dir, 'extracted_features.csv')

    df = pd.read_csv(csv_file_input)
    df_features = generate_features(csv_file_input)
    df_features.to_csv(csv_file_output, index=False)