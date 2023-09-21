import startAPI
from typing import Optional, List
from aas2openapi.models.base import AAS, Submodel


class NewPlantParameter(Submodel):
    timestamp: str
    value: List[str]


class Procedure(AAS):
    new_plant_parameters: NewPlantParameter


example_proceure = Procedure(
    id_="test",
    new_plant_parameters=NewPlantParameter(
        id_="test123",
        timestamp="12",
        value=["0.23", "12.12"],
    ),
)


json_file = "simple_aas_and_submodels.json"
startAPI.start_api_with_pydantic_model(example_proceure, json_file)
