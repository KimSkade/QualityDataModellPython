from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quality_data import QualityData


T = TypeVar("T", bound="QualityDataAAS")


@attr.s(auto_attribs=True)
class QualityDataAAS:
    """
    Example:
        {"id_": "QualityDataAAS", "description": "xyz", "id_short": "QualityDataAAS", "qualityData": {"id_": "Submodel",
            "description": "xyz", "id_short": "QualityDataSubmodel", "semantic_id": "http://www.google.de/1",
            "productionProcedures": [{"id_short": "ProductionProcedures", "description": "xyz", "semantic_id":
            "http://www.google.de/1", "resource": "Platzhalter", "process": "Patzhalter", "features": [{"id_short":
            "Features", "description": "xyz", "semantic_id": "http://www.google.de/1", "qualityFeatureName": [{"id_short":
            "qualityFeatureName1", "description": "xyz", "semantic_id": "http://www.google.de/1", "featureType": "Zylinder
            Mitte", "function": "Durchmesser", "unit": "mm", "targetValue": 9.0, "upperTolerance": 0.1, "lowerTolerance":
            -0.1, "warningLimit": 100.0, "controlLimit": 1.0, "inspectionEquipement": "PlatzhalterEquipment", "references":
            [{"id_short": "reference1", "description": "xyz", "semantic_id": "http://www.google.de/1", "point": "Platzhalter
            point", "line": "Platzhalter line", "surface": "Platzhalter surface", "axis": "Platzhalter axis"}],
            "sampleBatch": [{"id_short": "sampleBatch1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "sampleSize": 1, "sampleData": [{"id_short": "sampleData1", "description": "xyz", "semantic_id":
            "http://www.google.de/1", "sampleNumber": 1223, "sampleDate": "Platzhalter Datum", "partCounter": 1212,
            "result": [{"id_short": "result1", "description": "xyz", "semantic_id": "http://www.google.de/1", "value":
            8.9973025, "measurementDate": "Platzhalte Datum Uhrzeit", "uppertol": 0.1, "lowertol": -0.1, "nominal": 9.0,
            "resultCheck": true}]}]}]}]}]}]}}

    Attributes:
        id (str):
        quality_data (QualityData):  Example: {"id_": "Submodel", "description": "xyz", "id_short":
            "QualityDataSubmodel", "semantic_id": "http://www.google.de/1", "productionProcedures": [{"id_short":
            "ProductionProcedures", "description": "xyz", "semantic_id": "http://www.google.de/1", "resource":
            "Platzhalter", "process": "Patzhalter", "features": [{"id_short": "Features", "description": "xyz",
            "semantic_id": "http://www.google.de/1", "qualityFeatureName": [{"id_short": "qualityFeatureName1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "featureType": "Zylinder Mitte", "function":
            "Durchmesser", "unit": "mm", "targetValue": 9.0, "upperTolerance": 0.1, "lowerTolerance": -0.1, "warningLimit":
            100.0, "controlLimit": 1.0, "inspectionEquipement": "PlatzhalterEquipment", "references": [{"id_short":
            "reference1", "description": "xyz", "semantic_id": "http://www.google.de/1", "point": "Platzhalter point",
            "line": "Platzhalter line", "surface": "Platzhalter surface", "axis": "Platzhalter axis"}], "sampleBatch":
            [{"id_short": "sampleBatch1", "description": "xyz", "semantic_id": "http://www.google.de/1", "sampleSize": 1,
            "sampleData": [{"id_short": "sampleData1", "description": "xyz", "semantic_id": "http://www.google.de/1",
            "sampleNumber": 1223, "sampleDate": "Platzhalter Datum", "partCounter": 1212, "result": [{"id_short": "result1",
            "description": "xyz", "semantic_id": "http://www.google.de/1", "value": 8.9973025, "measurementDate":
            "Platzhalte Datum Uhrzeit", "uppertol": 0.1, "lowertol": -0.1, "nominal": 9.0, "resultCheck": true}]}]}]}]}]}]}.
        description (Union[Unset, str]):
        id_short (Union[Unset, str]):
    """

    id: str
    quality_data: "QualityData"
    description: Union[Unset, str] = UNSET
    id_short: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        quality_data = self.quality_data.to_dict()

        description = self.description
        id_short = self.id_short

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_": id,
                "qualityData": quality_data,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id_short is not UNSET:
            field_dict["id_short"] = id_short

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.quality_data import QualityData

        d = src_dict.copy()
        id = d.pop("id_")

        quality_data = QualityData.from_dict(d.pop("qualityData"))

        description = d.pop("description", UNSET)

        id_short = d.pop("id_short", UNSET)

        quality_data_aas = cls(
            id=id,
            quality_data=quality_data,
            description=description,
            id_short=id_short,
        )

        quality_data_aas.additional_properties = d
        return quality_data_aas

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
