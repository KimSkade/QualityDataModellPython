def detect_anomalies_statistical(df, window_size, sigma_count_threshold, action='remove'):
    """
    Erkenne Anomalien in einem DataFrame mit Sigma Werten
    :param df: Pandas DataFrame mit einer einzelnen Spalte numerischer Werte
    :param window_size: Größe des gleitenden Fensters zur Berechnung von Mittelwert und Standardabweichung
    :param sigma_count_threshold: Sigma-Schwellenwert zur Identifikation einer Anomalie
    :param action: 'remove', um Anomalien zu löschen, 'smooth', um sie durch den gleitenden Mittelwert zu ersetzen
    :return: DataFrame mit behandelten Anomalien und die Anzahl der erkannten Anomalien
    """

    # Berechne den gleitenden Mittelwert und die Standardabweichung
    rolling_mean = df.rolling(window=window_size, center=True).mean()
    rolling_std = df.rolling(window=window_size, center=True).std()

    # Kopiere den ursprünglichen DataFrame
    df_anomaly = df.copy()
    # Berechne den Sigma Wert
    df_anomaly['sigma_score'] = (df - rolling_mean) / rolling_std
    # Erstelle eine neue Spalte 'anomaly', die anzeigt, ob der Sigma Wert den Schwellenwert überschreitet
    df_anomaly['anomaly'] = df_anomaly['sigma_score'].abs() > sigma_count_threshold

    # Zähle Anomalien
    anomalies_count = df_anomaly['anomaly'].sum()

    # Behandle Anomalien entsprechend der gewählten Aktion
    if action == 'remove':
        df_anomaly = df_anomaly[~df_anomaly['anomaly']]
    elif action == 'smooth':
        df_anomaly.loc[df_anomaly['anomaly'], df.columns[0]] = rolling_mean

    # Entferne zusätzliche Spalten
    df_anomaly.drop(['sigma_score', 'anomaly'], axis=1, inplace=True)

    # Gib den bereinigten df und die Anzahl der Anomalien zurück
    return df_anomaly, anomalies_count
