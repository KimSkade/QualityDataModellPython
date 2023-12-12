import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def create_feature_baseline(df, n_features=50):
    """
    Erstellt eine Baseline der wichtigsten Merkmale eines DataFrames mit PCA
    :param df: DataFrame mit den Merkmalen
    :param n_features: Anzahl der wichtigsten Merkmale, die identifiziert werden sollen
    :return: Liste der Namen der wichtigsten Merkmale
    """
    # Standardisierung der Daten
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Anwendung von PCA
    pca = PCA()
    pca.fit(scaled_data)

    # Bestimme die kumulative Wichtigkeit jedes Merkmals über alle Komponenten
    feature_importances = np.abs(pca.components_).sum(axis=0)

    # Sortiere die Features nach ihrer Wichtigkeit
    most_important_features_indices = feature_importances.argsort()[::-1][:n_features]

    # Extrahiere die Namen der wichtigsten Merkmale
    most_important_features = [df.columns[i] for i in most_important_features_indices]

    return most_important_features

def select_features(df, feature_baseline):
    """
    Wählt Merkmale aus einem DataFrame basierend auf einer gegebenen Merkmal-Baseline aus.

    :param df: DataFrame, aus dem die Merkmale ausgewählt werden sollen.
    :param feature_baseline: Liste der Merkmalnamen, die als Baseline dienen.
    :return: DataFrame mit den ausgewählten Merkmalen.
    """
    selected_features = df[feature_baseline]
    return selected_features

