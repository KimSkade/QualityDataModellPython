def getValuefromColumName(dateipfad, spaltenname, zeilennummer):
    try:
        with open(dateipfad, 'r') as file:
            spaltenIndices = {}  # Dictionary zur Speicherung der Spaltenindices
            spaltennamen = None

            aktuelleZeilennummer = 0

            for zeile in file:
                spalten = zeile.strip().split('\t')

                if aktuelleZeilennummer == 0:
                    # Spaltennamen in Zeile 0 speichern
                    spaltennamen = spalten
                    for i in range(len(spaltennamen)):
                        spaltenIndices[spaltennamen[i]] = i
                elif aktuelleZeilennummer == zeilennummer:
                    # Gewünschte Zeile gefunden
                    spaltenindex = spaltenIndices.get(spaltenname)
                    if spaltenindex is not None and spaltenindex < len(spalten):
                        return spalten[spaltenindex]

                aktuelleZeilennummer += 1

            if spaltennamen is None:
                print("Spaltennamen nicht gefunden")
    except IOError as e:
        print("Ein Fehler ist beim Lesen der Datei aufgetreten:", e)

    return None





