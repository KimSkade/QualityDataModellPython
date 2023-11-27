import os

from services.convert_timestamp_in_str import convert_timestamp_in_str
from services.set_warning_control_limit import *
from services.read_txt import getValuefromColumName
from services.id_generator import generate_unique_id

from aas2openapi_client.api.quality_data_aas import put_item_quality_data_aas_item_id_quality_data_put
from aas2openapi_client.api.quality_data_aas.get_item_quality_data_aas_item_id_quality_data_get import sync
from aas2openapi_client.models import *


def put_kmg_data(dateipfad, breakpoint):
    i = 1
    quality_features = []

    while breakpoint != getValuefromColumName(dateipfad, "planid", i):
        target_value = float(getValuefromColumName(dateipfad, "nominal", i))
        lower_tolerance = float(getValuefromColumName(dateipfad, "lowertol", i))
        upper_tolerance = float(getValuefromColumName(dateipfad, "uppertol", i))
        value = float(getValuefromColumName(dateipfad, "actual", i))
        upper_control_limit = set_upper_control_limit(upper_tolerance=upper_tolerance, percentage=0.8)
        lower_control_limit = set_lower_control_limit(lower_tolerance=lower_tolerance, percentage=0.8)
        upper_warning_limit = set_upper_warning_limit(upper_tolerance=upper_tolerance, percentage=0.6)
        lower_warning_limit = set_lower_warning_limit(lower_tolerance=lower_tolerance, percentage=0.6)

        #  new values results SubmodelElementCollections
        new_result = NewResults(
            id_short=generate_unique_id(),
            semantic_id="http://www.google.de/1",  # Platzhalter
            description="This are new measurement datas.",
            measurement_date=convert_timestamp_in_str(os.path.getctime(dateipfad)),
            value=float(getValuefromColumName(dateipfad, "actual", i)),
            result_check=result_check(
                upper_control_limit=upper_control_limit,
                lower_control_limit=lower_control_limit,
                target_value=target_value,
                value=value,
            ),
            sample_number="1223",  # wo kommt die her
            part_counter=getValuefromColumName(dateipfad, "partnb", i),
        )

        #  results SubmodelElementCollections
        result = Result(
            id_short=generate_unique_id(),
            semantic_id="http://www.google.de/1",
            description="New measurement datas will be saved here.",
            new_results=[new_result],
        )

        quality_feature = QualityFeature(
            id_short=generate_unique_id(),
            semantic_id="http://www.google.de/1",
            description="xyz",
            feature_type=getValuefromColumName(dateipfad, "featureid", i),
            function=getValuefromColumName(dateipfad, "type", i),
            inspection_equipment="PlatzhalterEquipment",  # wo kommt das her
            unit=getValuefromColumName(dateipfad, "unit", i),
            upper_warning_limit=upper_warning_limit,
            lower_warning_limit=lower_warning_limit,
            upper_control_limit=upper_control_limit,
            lower_control_limit=lower_control_limit,
            sample_size=1,  # wo kommt die her
            result=result,
            target_value=target_value,
            lower_tolerance=lower_tolerance,
            upper_tolerance=upper_tolerance,
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
                value = float(getValuefromColumName(dateipfad, "actual", i))
                new_result = NewResults(
                    id_short=generate_unique_id(),
                    semantic_id="http://www.google.de/1",
                    description="This are new measurement datas.",
                    measurement_date=convert_timestamp_in_str(os.path.getctime(dateipfad)),
                    value=value,
                    result_check=result_check(
                        upper_control_limit=quality_feature.upper_control_limit,
                        target_value=quality_feature.target_value,
                        lower_control_limit=quality_feature.lower_control_limit,
                        value=value,
                    ),
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


def load_kmp_data_in_aas(dateipfad, breakpoint, item_id, client):
    quality_data: QualityData = sync(item_id=item_id, client=client)
    if quality_data.quality_feature.__len__() == 1:
        quality_data.quality_feature = put_kmg_data(dateipfad=dateipfad, breakpoint=breakpoint)
        put_item_quality_data_aas_item_id_quality_data_put.sync(item_id=item_id, client=client, json_body=quality_data)
    elif quality_data.quality_feature.__len__() > 1:
        put_new_results(dateipfad=dateipfad, breakpoint=breakpoint, item_id=item_id, client=client)
    # sync detailed benutzen und je nach response handeln


