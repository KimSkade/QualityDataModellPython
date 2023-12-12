import multiprocessing
import pandas as pd
import h5py
import numpy as np
from scipy.signal import butter, filtfilt

def process_chunk(start_idx, end_idx, file_path, dataset_path, skip_steps):
    """
    Verarbeitet einen Datenblock der HDF5-Datei und nimmt eine systematische Stichprobenreduktion vor
    :param start_idx: Startindex des Datenblocks
    :param end_idx: Endindex des Datenblocks
    :param file_path: Pfad zur HDF5-Datei
    :param dataset_path: Pfad zum Datensatz innerhalb der HDF5-Datei
    :param skip_steps: Anzahl der zu überspringenden Schritte zwischen den Stichproben
    :return: Ein NumPy-Array mit den heruntergesampelten Daten
    """
    # Initialisierung einer Liste, um die heruntergesampelten Daten zu speichern
    data_sampled = []
    # Öffnen der HDF5-Datei im Lesemodus
    with h5py.File(file_path, 'r') as hdf5_file:
        # Zugriff auf das spezifizierte Dataset
        dataset = hdf5_file[dataset_path]
        # Iteration über den spezifizierten Bereich mit der festgelegten Schrittweite
        for i in range(start_idx, end_idx, skip_steps):
            # Überprüfung, ob der aktuelle Index innerhalb der Datenbereichsgrenze liegt
            if i < dataset.shape[0]:
                # Hinzufügen des Datenpunkts zur Liste
                data_sampled.append(dataset[i])
    # Umwandlung der Liste in ein NumPy-Array und Rückgabe
    return np.array(data_sampled)


def downsample(hdf5_path, dataset_path, n_samples):
    """
    Verwendet Multiprocessing, um die Anzahl der Stichproben in einem Datensatz innerhalb einer HDF5-Datei zu reduzieren
    :param hdf5_path: Pfad zur HDF5-Datei
    :param dataset_path: Pfad zum Datensatz innerhalb der HDF5-Datei
    :param n_samples: Gewünschte Anzahl an Stichproben nach der Reduktion
    :return: DataFrame mit den heruntergesampelten Daten
    """
    n_processes = multiprocessing.cpu_count()

    with h5py.File(hdf5_path, 'r') as hdf5_file:
        total_size = hdf5_file[dataset_path].shape[0]

    skip_steps = total_size // n_samples
    chunk_size = (total_size // n_processes) + 1

    args = [(i * chunk_size, min((i + 1) * chunk_size, total_size), hdf5_path, dataset_path, skip_steps)
            for i in range(n_processes)]

    with multiprocessing.Pool(n_processes) as pool:
        results = pool.starmap(process_chunk, args)

    data_sampled = np.concatenate(results)
    return pd.DataFrame(data_sampled, columns=['Value'])


def downsample_and_filter(hdf5_path, dataset_path, fs, cutoff_frequency, order, downsample_factor):
    """
    Reduziert die Anzahl der Stichproben in einem Datensatz innerhalb einer HDF5-Datei und benutzt einen Tiefpass Filter
    :param hdf5_path: Pfad zur HDF5-Datei
    :param dataset_path: Pfad zum Datensatz innerhalb der HDF5-Datei
    :param fs: Die ursprüngliche Abtastfrequenz der Daten
    :param cutoff_frequency: Die Grenzfrequenz für den Low-Pass-Filter
    :param order: Die Ordnung des Butterworth-Filters
    :param downsample_factor: Der Faktor, mit dem die Daten heruntergetastet werden sollen
    :return: Heruntergetastete und gefilterte Daten
    """
    # Öffnen der HDF5-Datei und Zugriff auf den Datensatz
    with h5py.File(hdf5_path, 'r') as hdf5_file:
        data = hdf5_file[dataset_path][:]  # Lese alle Daten aus dem Datensatz

    # Heruntertasten der Daten, indem jeder xte Punkt genommen wird
    downsampled_data = data[::downsample_factor]

    # Anpassung der Abtastfrequenz an die heruntergetasteten Daten
    new_fs = fs / downsample_factor

    # Berechnung der Nyquist-Frequenz
    nyquist = 0.5 * new_fs

    # Normalisierung der Grenzfrequenz durch die Nyquist-Frequenz
    normalized_cutoff = cutoff_frequency / nyquist

    # Berechnung der Filterkoeffizienten
    b, a = butter(N=order, Wn=normalized_cutoff, btype='low', analog=False)

    # Anwendung des Filters auf die heruntergetasteten Daten
    filtered_data = filtfilt(b, a, downsampled_data)

    return filtered_data


def bin_hdf5_dataset(hdf5_path, dataset_path, bin_size):
    """
    Liest einen Datensatz aus einer HDF5-Datei und wendet die Bin-Datenfunktion darauf an
    :param hdf5_path: Pfad zur HDF5-Datei
    :param dataset_path: Pfad zum Datensatz innerhalb der HDF5-Datei
    :param bin_size: Die Größe der Bins für das Binning
    :return: Die gebinnten Daten als NumPy-Array
    """
    # Öffne die HDF5-Datei im Lesemodus
    with h5py.File(hdf5_path, 'r') as hdf5_file:
        # Lese den Datensatz
        data = hdf5_file[dataset_path][:]

    # Berechne die Anzahl der vollständigen Bins
    num_full_bins = len(data) // bin_size

    # Nur vollständige Bins zu erhalten
    trimmed_data = data[:num_full_bins * bin_size]

    # Reshape das abgeschnittene Array in eine zweidimensionale Matrix, so dass jede Zeile einem Bin entspricht
    reshaped_data = trimmed_data.reshape((num_full_bins, bin_size))

    # Berechne den Mittelwert jeder Zeile (jedes Bins)
    binned_data = reshaped_data.mean(axis=1)

    return binned_data