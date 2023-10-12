from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.production_procedures import ProductionProcedures


T = TypeVar("T", bound="QualityData")


@attr.s(auto_attribs=True)
class QualityData:
    """
    Example:
        {"id_": "Submodel", "description": "xyz", "id_short": "QualityDataSubmodel", "semantic_id":
            "http://www.google.de/1", "production_procedures": [{"id_short": "ProductionProcedures", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "resource": "Platzhalter", "process": "Patzhalter", "features":
            [{"id_short": "Features", "description": "xyz", "semantic_id": "http://www.google.de/1", "quality_feature_name":
            [{"id_short": "qualityFeatureName1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "feature_type": "Zylinder Mitte", "function": "Durchmesser", "unit": "mm", "target_value": 9.0,
            "upper_tolerance": 0.1, "lower_tolerance": -0.1, "warning_limit": 100.0, "control_limit": 1.0,
            "inspection_equipement": "PlatzhalterEquipment", "references": [{"id_short": "reference1", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "point": "Platzhalter point", "line": "Platzhalter line", "surface":
            "Platzhalter surface", "axis": "Platzhalter axis"}], "sample_batch": [{"id_short": "sampleBatch1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "sample_size": 1, "sample_data": [{"id_short":
            "sampleData1", "description": "xyz", "semantic_id": "http://www.google.de/1", "sample_number": 1223,
            "sample_date": "Platzhalter Datum", "part_counter": 1212, "result": [{"id_short": "result1", "description":
            "xyz", "semantic_id": "http://www.google.de/1", "value": 8.9973025, "measurement_date": "Platzhalte Datum
            Uhrzeit", "uppertol": 0.1, "lowertol": -0.1, "nominal": 9.0, "result_check": true}]}]}]}]}]}]}

    Attributes:
        id (str):
        production_procedures (List['ProductionProcedures']):
        description (Union[Unset, str]):
        id_short (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id: str
    production_procedures: List["ProductionProcedures"]
    description: Union[Unset, str] = UNSET
    id_short: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        production_procedures = []
        for production_procedures_item_data in self.production_procedures:
            production_procedures_item = production_procedures_item_data.to_dict()

            production_procedures.append(production_procedures_item)

        description = self.description
        id_short = self.id_short
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_": id,
                "production_procedures": production_procedures,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id_short is not UNSET:
            field_dict["id_short"] = id_short
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.production_procedures import ProductionProcedures

        d = src_dict.copy()
        id = d.pop("id_")

        production_procedures = []
        _production_procedures = d.pop("production_procedures")
        for production_procedures_item_data in _production_procedures:
            production_procedures_item = ProductionProcedures.from_dict(production_procedures_item_data)

            production_procedures.append(production_procedures_item)

        description = d.pop("description", UNSET)

        id_short = d.pop("id_short", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        quality_data = cls(
            id=id,
            production_procedures=production_procedures,
            description=description,
            id_short=id_short,
            semantic_id=semantic_id,
        )

        quality_data.additional_properties = d
        return quality_data

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