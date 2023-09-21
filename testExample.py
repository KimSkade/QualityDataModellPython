import typing
from aas2openapi import models


class BillOfMaterial(models.Submodel):
    components: typing.List[str]
    result_check: bool


class ProcessModel(models.Submodel):
    processes: typing.List[str]
    result_check: bool


class Product(models.AAS):
    bill_of_material: BillOfMaterial
    process_model: typing.Optional[ProcessModel]


example_product = Product(
    id_="TEST",
    process_model=ProcessModel(
        id_="a8cd10ed",
        processes=["join", "screw"], result_check=False,
    ),
    bill_of_material=BillOfMaterial(
        id_="a7cba3bcd", components=["stator", "rotor", "coil", "bearing"], result_check=True,
    ),
)