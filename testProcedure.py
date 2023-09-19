from models import procedure, processAttributes, resource, product
import aas2openapi
from aas2openapi.middleware import Middleware
import basyx.aas.adapter.json.json_serialization
import uvicorn
import typing
from aas2openapi import models


example_product=product.Product(
    id_="Produkt1",
    targetValue=[product.TargetValue(id_short="TEST",
        value=0.123,
        valueDescription="DurchmesserSeiteA"
    )]
)


example_resource=resource.Resource(
    id_="Ressource1",
    plantParameter=[resource.PlantParameter(id_short="TEST",
        valueMin=100.00,
        valueMax=1000.00,
        valueDescription="Rotationsgeschwindigkeit"
    )]
)


example_process_attributes=processAttributes.AttributePredicates(
    id_="AttributPredicate1",
    attributePredicate=[processAttributes.AttributePredicate(id_short="TEST",
        attribute_carrier="test",
        general_attribute="test",
        predicate_type="maximum",
        attribute_value=processAttributes.AttributeValue(id_short="TEST"
        )
    )]
)


example_NewPlantParameter=procedure.NewPlantParameter(
    id_="NeueAnlagenparameter1",
    newPlantParameter=procedure.NewPlantParameterData(id_short="TEST",
        newValuesPlantParameter=[procedure.NewValuesPlantParameter(id_short="TEST",
            timestamp=23435454534,
            value=[12323, 1213.545]
        )]
    )
)


example_ProcessData=procedure.ProcessDatas(
    id_="ProcessDaten1",
    processData=[procedure.ProcessData(id_short="TEST",
        processDataType="Temperatur",
        newValues=[procedure.NewValuesPlantParameter(id_short="TEST",
            timestamp=23435454534,
            value=[12323, 1213.545]
        )]
    )]
)


example_procedure = procedure.Procedure(
    id_="Prozedu1",
    product=example_product,
    resource=example_resource,
    processAttributes=example_process_attributes,
    newPlantParameters=example_NewPlantParameter,
    processDatas=example_ProcessData
)


obj_store = aas2openapi.convert_pydantic_model_to_aas(example_procedure)
with open("simple_aas_and_submodels.json", "w", encoding="utf-8") as json_file:
    basyx.aas.adapter.json.write_aas_json_file(json_file, obj_store)


middleware = Middleware()
middleware.load_pydantic_model_instances([example_procedure])
middleware.generate_rest_api()
#  middleware.generate_graphql_api()

app = middleware.app
uvicorn.run(app)

