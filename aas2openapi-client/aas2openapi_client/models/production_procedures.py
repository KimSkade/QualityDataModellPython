from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.features import Features
    from ..models.procedure_data import ProcedureData


T = TypeVar("T", bound="ProductionProcedures")


@attr.s(auto_attribs=True)
class ProductionProcedures:
    """
    Attributes:
        id_short (str):
        features (Features):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
        list_procedures (Union[Unset, List['ProcedureData']]):
    """

    id_short: str
    features: "Features"
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    list_procedures: Union[Unset, List["ProcedureData"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        features = self.features.to_dict()

        description = self.description
        semantic_id = self.semantic_id
        list_procedures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.list_procedures, Unset):
            list_procedures = []
            for list_procedures_item_data in self.list_procedures:
                list_procedures_item = list_procedures_item_data.to_dict()

                list_procedures.append(list_procedures_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "features": features,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id
        if list_procedures is not UNSET:
            field_dict["list_procedures"] = list_procedures

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.features import Features
        from ..models.procedure_data import ProcedureData

        d = src_dict.copy()
        id_short = d.pop("id_short")

        features = Features.from_dict(d.pop("features"))

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        list_procedures = []
        _list_procedures = d.pop("list_procedures", UNSET)
        for list_procedures_item_data in _list_procedures or []:
            list_procedures_item = ProcedureData.from_dict(list_procedures_item_data)

            list_procedures.append(list_procedures_item)

        production_procedures = cls(
            id_short=id_short,
            features=features,
            description=description,
            semantic_id=semantic_id,
            list_procedures=list_procedures,
        )

        production_procedures.additional_properties = d
        return production_procedures

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
