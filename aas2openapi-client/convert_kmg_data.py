from services.txtEinlesen import getValuefromColumName

from aas2openapi_client.api.quality_data_aas.get_item_quality_data_aas_item_id_quality_data_get import sync
from aas2openapi_client.api.quality_data_aas import put_item_quality_data_aas_item_id_quality_data_put
from aas2openapi_client.models import *
import os
from services.convert_timestamp_in_str import convert_timestamp_in_str

def put_kmg_data(dateipfad, breakpoint):
    i = 1
    quality_features = []

    while breakpoint != getValuefromColumName(dateipfad, "planid", i):
        #  new values results SubmodelElementCollections
        new_result = NewResults(
            id_short="result" + str(i),
            semantic_id="http://www.google.de/1",  # Platzhalter
            description="This are new measurement datas.",
            measurement_date=convert_timestamp_in_str(os.path.getctime(dateipfad)),
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

        quality_feature = QualityFeature(
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
            target_value=float(getValuefromColumName(dateipfad, "nominal", i)),
            lower_tolerance=float(getValuefromColumName(dateipfad, "lowertol", i)),
            upper_tolerance=float(getValuefromColumName(dateipfad, "uppertol", i)),
        )
        quality_features.append(quality_feature)
        i += 1

    return quality_features


def put_new_results(dateipfad, breakpoint, item_id, client):
    quality_data: QualityData = sync(item_id=item_id, client=client)
    # print(quality_data)
    for quality_feature in quality_data.quality_feature:
        i = 1
        while breakpoint != getValuefromColumName(dateipfad, "planid", i):
            if quality_feature.feature_type == getValuefromColumName(dateipfad, "featureid", i):
                new_result = NewResults(
                    id_short="result" + str(i)+ str(i),
                    semantic_id="http://www.google.de/1",
                    description="This are new measurement datas.",
                    measurement_date=convert_timestamp_in_str(os.path.getctime(dateipfad)),
                    value=float(getValuefromColumName(dateipfad, "actual", i)),
                    result_check=True,  # Formel für ResultCheck anpassen
                    sample_number="1223",
                    part_counter=getValuefromColumName(dateipfad, "partnb", i),
                )
                quality_feature.result.new_results.append(new_result)
                print(new_result)
                print(quality_data.quality_feature)
                break
            else:
                i += 1

    # put quality_data
    put_item_quality_data_aas_item_id_quality_data_put.sync(item_id=item_id, client=client, json_body=quality_data)
