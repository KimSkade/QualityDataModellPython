from services.txtEinlesen import getValuefromColumName

from aas2openapi_client.api.quality_data_aas.get_item_quality_data_aas_item_id_quality_data_get import sync
from aas2openapi_client.models import *


def put_kmg_data(dateipfad, breakpoint):
    i = 1
    quality_feature_names = []

    while breakpoint != getValuefromColumName(dateipfad, "planid", i):
        #  new values results SubmodelElementCollections
        new_result = NewResults(
            id_short="result" + str(i),
            semantic_id="http://www.google.de/1",  # Platzhalter
            description="This are new measurement datas.",
            measurement_date="Platzhalte Datum Uhrzeit",  # Quelle MeasureDate
            value=float(getValuefromColumName(dateipfad, "actual", i)),
            result_check=True,  # Formel für ResultCheck anpassen
            sample_number="1223",  # wo kommt die her
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
            inspection_equipment="PlatzhalterEquipment",  # wo kommt das her
            unit=getValuefromColumName(dateipfad, "unit", i),
            warning_limit=float(getValuefromColumName(dateipfad, "warningLimitCF", i)),
            control_limit=1,
            sample_size=1,  # wo kommt die her
            result=result,
        )
        quality_feature_names.append(quality_feature_name)
        i += 1

    return quality_feature_names


def post_new_results(dateipfad, item_id, client):
    quality_data: QualityData = sync(item_id=item_id, client=client)
    # print(quality_data)
    for quality_feature_name in quality_data.production_procedures[
        0
    ].features.quality_feature_name:  # production_procedures setzen
        i = 1
        while breakpoint != getValuefromColumName(dateipfad, "planid", i):
            if quality_feature_name.feature_type == getValuefromColumName(dateipfad, "featureid", i):
                post_id = quality_feature_name.id_short
                print(post_id)
                new_result = NewResults(
                    id_short="result" + str(i),
                    semantic_id="http://www.google.de/1",
                    description="This are new measurement datas.",
                    measurement_date="Platzhalter Datum Uhrzeit",  # Quelle MeasureDate
                    value=float(getValuefromColumName(dateipfad, "actual", i)),
                    result_check=True,  # Formel für ResultCheck anpassen
                    sample_number="1223",
                    part_counter=getValuefromColumName(dateipfad, "partnb", i),
                )
                # post new_result
                print(new_result)
                break
            else:
                i += 1