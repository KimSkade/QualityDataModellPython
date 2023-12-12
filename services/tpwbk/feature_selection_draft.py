import os
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
csv_file_path = os.path.join(data_dir, 'extracted_features.csv')
df_features = pd.read_csv(csv_file_path)

# Standardisierung
scaler = StandardScaler()
df_features_scaled = scaler.fit_transform(df_features)

# PCA
pca = PCA()
pca.fit(df_features_scaled)

# Erklärte Varianz
explained_variance = pca.explained_variance_ratio_

# Plot
plt.figure(figsize=(8, 4))
plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_)
plt.ylabel('Explained Variance')
plt.xlabel('Principal Components')
plt.title('Explained Variance Ratio by Principal Component')
plt.show()

# Optionally, choose the number of components that explain a certain threshold of variance (e.g., 95%)
cumulative_variance = explained_variance.cumsum()
num_components_for_threshold = (cumulative_variance < 0.95).sum() + 1
print(f"Number of components to explain 95% variance: {num_components_for_threshold}")

# Transform the scaled features using the selected number of principal components
pca = PCA(n_components=num_components_for_threshold)
df_features_reduced = pca.fit_transform(df_features_scaled)

# Convert the reduced features to a DataFrame
df_features_reduced_df = pd.DataFrame(df_features_reduced, columns=[f'PC{i+1}' for i in range(df_features_reduced.shape[1])])

# Save the reduced features DataFrame to a CSV file
output_csv_path = os.path.join(data_dir, 'reduced_features.csv')
df_features_reduced_df.to_csv(output_csv_path, index=False)

# pca_df = df_features_reduced_df[['PC1', 'PC2']]
#
# plt.figure(figsize=(8, 6))
# plt.scatter(pca_df['PC1'], pca_df['PC2'])
# plt.xlabel('Principal Component 1')
# plt.ylabel('Principal Component 2')
# plt.title('PCA of Extracted Features')
# plt.grid(True)
# plt.show()


#Variance Thresholding

#Extracted Features einlesen
csv_file_path = os.path.join(data_dir, 'extracted_features.csv')
df = pd.read_csv(csv_file_path)

# Feature-Selektion basierend auf Variabilität
max_features_to_keep = 5  # Setzen Sie die maximale Anzahl der Features, die Sie behalten möchten
selector = VarianceThreshold(threshold=1e-5)  # Hier können Sie den Schwellenwert nach Bedarf anpassen
selected_features = selector.fit_transform(df)

# Wenn die Anzahl der ausgewählten Features die maximale Anzahl übersteigt, wählen Sie nur die ersten
selected_features = selected_features[:, :max_features_to_keep]
selected_feature_names = df.columns[selector.get_support()][:max_features_to_keep]

# Speichern der ausgewählten Merkmale
selected_features_df = pd.DataFrame(selected_features, columns=selected_feature_names)
selected_features_path = os.path.join(data_dir, 'selected_features.csv')
selected_features_df.to_csv(selected_features_path, index=False)

# Visualisiere die Verteilung der ausgewählten Features
fig, axes = plt.subplots(nrows=1, ncols=len(selected_features_df.columns), figsize=(15, 6))
for i, feature in enumerate(selected_features_df.columns):
    axes[i].boxplot(selected_features_df[feature])
    axes[i].set_title(feature)
    axes[i].set_title(feature, y=1.05)  # Ändere den Wert von y nach Bedarf
    axes[i].set_ylabel('Feature-Werte')
    axes[i].set_ylabel('Feature-Werte', labelpad=15) # Passe den Abstand der Y-Achse-Beschriftung an

# Passe den Abstand zwischen den Subplots an
plt.subplots_adjust(wspace=0.75)

plt.show()



# Statistische Selektion
# Runtime Warning Division by Zero

csv_file_path = os.path.join(data_dir, 'extracted_features.csv')
df = pd.read_csv(csv_file_path)

# Dummy-Labels erstellen (alle 0, da keine echten Labels vorhanden sind)
dummy_labels = [0] * len(df)

# Anzahl der gewünschten ausgewählten Features
num_selected_features = 5

# Univariate statistische Feature-Selektion
selector = SelectKBest(score_func=f_classif, k=num_selected_features)
selected_features = selector.fit_transform(df, dummy_labels)

# Finde die Namen der ausgewählten Features
selected_feature_indices = selector.get_support(indices=True)
selected_feature_names = df.columns[selected_feature_indices]

# Speichern der ausgewählten Merkmale
selected_features_statistical_df = pd.DataFrame(selected_features, columns=selected_feature_names)
selected_features_statistical_path = os.path.join(data_dir, 'selected_features_statistical.csv')
selected_features_statistical_df.to_csv(selected_features_statistical_path, index=False)

# Annahme: 'label' ist die Spalte in Ihrem DataFrame, die die Klassen enthält
df['label'] = dummy_labels

# Plot der ausgewählten Merkmale
fig, axes = plt.subplots(nrows=1, ncols=num_selected_features, figsize=(15, 6))

for i, feature in enumerate(selected_feature_names):
    sns.boxplot(x='label', y=feature, data=df, ax=axes[i])
    axes[i].set_title(feature)
    axes[i].set_title(feature, y=1.05)  # Ändere den Wert von y nach Bedarf
    axes[i].set_ylabel('Feature-Werte')
    axes[i].set_xlabel('Klasse')
    axes[i].set_ylabel('Feature-Werte', labelpad=15) # Passe den Abstand der Y-Achse-Beschriftung an

plt.tight_layout()
plt.show()



#Korrelationsbasierte Selektion

csv_file_path = os.path.join(data_dir, 'extracted_features.csv')
df = pd.read_csv(csv_file_path)

# Annahme: df ist Ihr DataFrame ohne 'label'
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
csv_file_path = os.path.join(data_dir, 'extracted_features.csv')
df = pd.read_csv(csv_file_path)

# Berechnen Sie die Korrelationsmatrix
correlation_matrix = df.corr()

# Setzen Sie die Diagonale auf Null, um Selbstkorrelationen zu vermeiden
correlation_matrix.values[[range(correlation_matrix.shape[0])] * 2] = 0

# Summieren Sie die Korrelationen für jedes Feature
correlation_sums = correlation_matrix.abs().sum()

# Wählen Sie die Top-5-Features aus
top_5_features = correlation_sums.nlargest(5).index

# Extrahieren Sie die ausgewählten Merkmale
selected_features = df.loc[:, top_5_features]

# Speichern Sie die ausgewählten Merkmale
selected_features_path = os.path.join(data_dir, 'selected_features_correlation_top5.csv')
selected_features.to_csv(selected_features_path, index=False)

import matplotlib.pyplot as plt

# Annahme: selected_features ist Ihr DataFrame mit den ausgewählten Features und deren Korrelationssummen
selected_features_path = os.path.join(data_dir, 'selected_features_correlation_top5.csv')
selected_features = pd.read_csv(selected_features_path)

# Berechnen Sie die Korrelationssummen für die ausgewählten Features
correlation_sums = selected_features.corr().abs().sum()

# Plot der ausgewählten Features und ihrer Korrelationssummen
fig, ax = plt.subplots(figsize=(13, 6))
ax.bar(selected_features.columns, correlation_sums, width=0.75)  # Passen Sie die Breite nach Bedarf an
ax.set_xlabel('Feature')
ax.set_ylabel('Korrelationssumme')
ax.set_title('Top 5 Features basierend auf Korrelationssumme')

plt.show()


#RFE Classifier

# Laden Sie Ihren extrahierten Datensatz
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
csv_file_path = os.path.join(data_dir, 'extracted_features.csv')
df = pd.read_csv(csv_file_path)

# Annahme: df ist Ihr DataFrame ohne 'label'
X = df.drop(columns=['label'], errors='ignore')
y = [0] * len(df)  # Dummy-Labels (alle 0)

# Verwenden Sie RandomForestClassifier als Schätzer
estimator = RandomForestClassifier(n_estimators=100, random_state=42)

# RFE mit 5 gewünschten Features
num_selected_features = 5
selector = RFE(estimator, n_features_to_select=num_selected_features)
selector = selector.fit(X, y)

# Extrahieren Sie die ausgewählten Features
selected_features = X.columns[selector.support_]

# Speichern Sie die ausgewählten Features
selected_features_path = os.path.join(data_dir, 'selected_features_rfe_top5.csv')
X[selected_features].to_csv(selected_features_path, index=False)

# Laden Sie die ausgewählten Features
selected_features_path = os.path.join(data_dir, 'selected_features_rfe_top5.csv')
selected_features = pd.read_csv(selected_features_path)

# Plot der ausgewählten Features
fig, ax = plt.subplots(figsize=(10, 6))
for feature in selected_features.columns:
    ax.plot(selected_features[feature], label=feature)

ax.set_xlabel('Beispielindex')
ax.set_ylabel('Feature-Wert')
ax.set_title('Ausgewählte Features nach RFE')
ax.legend()

plt.show()