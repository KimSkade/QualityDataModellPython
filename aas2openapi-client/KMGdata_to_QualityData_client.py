from services.txtEinlesen import getValuefromColumName

from aas2openapi_client.models import *


def put_kmg_data(dateipfad, breakpoint):
    i = 1
    quality_feature_names = []

    while breakpoint != getValuefromColumName(dateipfad, "planid", i):
        #  new values results SubmodelElementCollections
        new_result = NewResults(
            id_short="result" + str(i),
            semantic_id="http://www.google.de/1",
            description="This are new measurement datas.",
            measurement_date="Platzhalte Datum Uhrzeit",  # Quelle MeasureDate
            value=float(getValuefromColumName(dateipfad, "actual", i)),
            result_check=True,  # Formel für ResultCheck anpassen
            sample_number="1223",
            part_counter=getValuefromColumName(dateipfad, "partnb", i),
        )

        #  results SubmodelElementCollections
        result = Result(
            id_short="Result",
            semantic_id="http://www.google.de/1",
            description="New measurement datas will be saved here.",
            new_results=[new_result],
        )

        quality_feature_name = QualityFeatureName(
            id_short="qualityFeatureName" + str(i),
            semantic_id="http://www.google.de/1",
            description="xyz",
            feature_type=getValuefromColumName(dateipfad, "featureid", i),
            function=getValuefromColumName(dateipfad, "type", i),
            inspection_equipment="PlatzhalterEquipment",
            unit=getValuefromColumName(dateipfad, "unit", i),
            warning_limit=float(getValuefromColumName(dateipfad, "warningLimitCF", i)),
            control_limit=1,
            sample_size=1,
            result=result,
        )
        quality_feature_names.append(quality_feature_name)
        i += 1

    return quality_feature_names


data = put_kmg_data("C:/Users/kim0_/OneDrive/Dokumente/Masterarbeit/PruefplanValidierungsbauteil1_16.txt", "END")
print(data)
