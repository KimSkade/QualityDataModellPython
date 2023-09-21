from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill_of_material import BillOfMaterial
    from ..models.process_model import ProcessModel


T = TypeVar("T", bound="Product")


@attr.s(auto_attribs=True)
class Product:
    """
    Attributes:
        id (str):
        bill_of_material (BillOfMaterial):
        description (Union[Unset, str]):  Default: ''.
        id_short (Union[Unset, str]):  Default: 'TEST100'.
        process_model (Union[Unset, ProcessModel]):
    """

    id: str
    bill_of_material: "BillOfMaterial"
    description: Union[Unset, str] = ""
    id_short: Union[Unset, str] = "TEST100"
    process_model: Union[Unset, "ProcessModel"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        bill_of_material = self.bill_of_material.to_dict()

        description = self.description
        id_short = self.id_short
        process_model: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.process_model, Unset):
            process_model = self.process_model.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_": id,
                "bill_of_material": bill_of_material,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id_short is not UNSET:
            field_dict["id_short"] = id_short
        if process_model is not UNSET:
            field_dict["process_model"] = process_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bill_of_material import BillOfMaterial
        from ..models.process_model import ProcessModel

        d = src_dict.copy()
        id = d.pop("id_")

        bill_of_material = BillOfMaterial.from_dict(d.pop("bill_of_material"))

        description = d.pop("description", UNSET)

        id_short = d.pop("id_short", UNSET)

        _process_model = d.pop("process_model", UNSET)
        process_model: Union[Unset, ProcessModel]
        if isinstance(_process_model, Unset):
            process_model = UNSET
        else:
            process_model = ProcessModel.from_dict(_process_model)

        product = cls(
            id=id,
            bill_of_material=bill_of_material,
            description=description,
            id_short=id_short,
            process_model=process_model,
        )

        product.additional_properties = d
        return product

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
