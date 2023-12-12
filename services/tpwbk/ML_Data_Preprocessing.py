#Input: DF von Kim (timestamp, qass_Nr, selectedFeatures, productID, toolID, toolcondition, shift position, toolHolderClearance, correctionValueY, toolNumberCycles)
#Output: Überarbeiteter DF

import pandas as pd
import numpy as np
import json

# Pfade zu deiner JSON-Datei
json_dateipfad = '/Users/max/Desktop/Teamprojekt WBK/FormatVorlageKörperschall.json'

# JSON in DataFrame umwandeln
df = pd.read_json(json_dateipfad)

# Überprüfen auf fehlende Daten
fehlende_daten = df.isnull()

# Alternativ: Summe der fehlenden Daten pro Spalte
summe_fehlende_daten_pro_spalte = df.isnull().sum()

# Alternativ: Gesamtzahl der fehlenden Daten im gesamten DataFrame
gesamtzahl_fehlende_daten = df.isnull().sum().sum()

# Anzeigen der Ergebnisse
print("DataFrame:")
print(df)
print("\nFehlende Daten pro Spalte:")
print(summe_fehlende_daten_pro_spalte)
print("\nGesamtzahl der fehlenden Daten im DataFrame:", gesamtzahl_fehlende_daten)


#1. Option
#Löschen der Fehlenden Daten
df_cleaned = df.dropna().copy()

print("Data Frame cleaned:")
print(df_cleaned)


#2. Option
#Median Imputation
#Daten werden durch den Median aller Daten ersetzt
df_median_imputed = df.fillna(df.median()).copy()

print("Data Frame Median Imputation:")
print(df_median_imputed)


#3. Option
#K-Nearest_Neighbor Imputation
#Daten werden ersetz durch eine Schätzung anhand von ähnlichen Dataframes. Schätzung erfolgt anhand euklidischer Distanz.
from sklearn.impute import KNNImputer

# k-Nächste-Nachbarn-Imputation
knn_imputer = KNNImputer(n_neighbors=2)  # Du kannst die Anzahl der Nachbarn (n_neighbors) anpassen
df_knearestneighbor_imputed = pd.DataFrame(knn_imputer.fit_transform(df), columns=df.columns)

# Anzeigen des aktualisierten DataFrame
print("DataFrame k-nearest-neighbor-Imputation:")
print(df_knearestneighbor_imputed)


#4. Option
#Multiple Imputation
#Statistisches Verfahen: Fehlende Daten werden mehrfach geschätz um Unsicherheiten zu berücksichtigen.
#!!New Requirement: pip install fancyimpute!!
from fancyimpute import IterativeImputer

# Multiple Imputation
mice_imputer = IterativeImputer(max_iter=10, random_state=0)  # Du kannst die Anzahl der Iterationen (max_iter) anpassen
df_multiple_imputed = pd.DataFrame(mice_imputer.fit_transform(df), columns=df.columns)

# Anzeigen des aktualisierten DataFrame
print("DataFrame Multiple Imputation:")
print(df_multiple_imputed)


#5. Option
#Matrix Faktorisierung
#Schätzt fehlende Werte anhand von Matrix Faktorisierung. Gut für große Datenmengen :)
# Matrix Faktorisierung (NMF) für Imputation
from sklearn.decomposition import NMF

nmf_imputer = NMF(n_components=2, init='random', random_state=0)  # Du kannst die Anzahl der Komponenten (n_components) anpassen
df_matrix_imputed = pd.DataFrame(nmf_imputer.fit_transform(df), columns=df.columns)

# Anzeigen des aktualisierten DataFrame
print("DataFrame Matrix Faktorisierung:")
print(df_matrix_imputed)


#6. Option
#Random Forest Imputation
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

# Random-Forest-Imputation
rf_imputer = IterativeImputer(estimator='randomforest', random_state=0)
df_random_forest_imputed = pd.DataFrame(rf_imputer.fit_transform(df), columns=df.columns)

# Anzeigen des aktualisierten DataFrame
print("DataFrame Random-Forest-Imputation:")
print(df_random_forest_imputed)


#7. Option
#Datawig
#Python Bibliothek die automatisierte Imputation mit Deep Learning Techniken ermöglicht
#!!New Requirement: pip install datwig!!
from datwig.imputer import SingleImputer

# Datwig-Imputation
imputer = SingleImputer(strategy='RandomForest', threads=-1)
df_datawig_imputed = imputer.fit_transform(df)

# Anzeigen des aktualisierten DataFrame
print("DataFrame nach Datwig-Imputation:")
print(df_datawig_imputed)


#8. Option
#Iterative Imputation (MICE = Multivariate Imputation by chaines equations)
#!!New Requirement: pip install fancyimpute!!
from fancyimpute import IterativeImputer

# MICE-Imputation
mice_imputer = IterativeImputer(max_iter=10, random_state=0)  # Du kannst die Anzahl der Iterationen (max_iter) anpassen
df_mice_imputed = pd.DataFrame(mice_imputer.fit_transform(df), columns=df.columns)

# Anzeigen des aktualisierten DataFrame
print("DataFrame nach MICE-Imputation:")
print(df_mice_imputed)






