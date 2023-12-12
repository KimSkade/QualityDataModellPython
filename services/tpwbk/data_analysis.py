import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import os

# Pfad zum Ordner 'data'
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
extracted_features_path = os.path.join(data_dir, 'extracted_features.csv')

# Laden der extrahierten Merkmale
df_features = pd.read_csv(extracted_features_path)

num_features = df_features.shape[1]  # Die Anzahl der Spalten im DataFrame entspricht der Anzahl der Merkmale.
print(f"Anzahl der extrahierten Merkmale: {num_features}")

# Visualisierung der ersten Merkmale über die Zeit
for feature in df_features.columns[:5]:
    plt.figure(figsize=(10, 4))
    plt.plot(df_features[feature])
    plt.title(f'Zeitreihe des Merkmals: {feature}')
    plt.xlabel('Zeitschritt')
    plt.ylabel('Wert')
    plt.show()

# Histogramme für die ersten Merkmale
df_features[df_features.columns[:5]].hist(bins=15, figsize=(10, 8))
plt.suptitle('Verteilungen der Merkmale')
plt.show()

# Korrelations-Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df_features.corr(), annot=False, cmap='coolwarm')
plt.title('Korrelations-Heatmap der Merkmale')
plt.show()

# PCA zur Dimensionsreduktion
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_features)

plt.figure(figsize=(8, 6))
plt.scatter(pca_result[:, 0], pca_result[:, 1])
plt.title('PCA - Erste zwei Hauptkomponenten')
plt.xlabel('Hauptkomponente 1')
plt.ylabel('Hauptkomponente 2')
plt.show()