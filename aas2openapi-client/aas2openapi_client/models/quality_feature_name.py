from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.references import References
    from ..models.sample_batch import SampleBatch


T = TypeVar("T", bound="QualityFeatureName")


@attr.s(auto_attribs=True)
class QualityFeatureName:
    """
    Attributes:
        id_short (str):
        feature_type (str):
        function (str):
        unit (str):
        target_value (float):
        upper_tolerance (float):
        lower_tolerance (float):
        warning_limit (float):
        control_limit (float):
        inspection_equipement (str):
        references (List['References']):
        sample_batch (List['SampleBatch']):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    feature_type: str
    function: str
    unit: str
    target_value: float
    upper_tolerance: float
    lower_tolerance: float
    warning_limit: float
    control_limit: float
    inspection_equipement: str
    references: List["References"]
    sample_batch: List["SampleBatch"]
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        feature_type = self.feature_type
        function = self.function
        unit = self.unit
        target_value = self.target_value
        upper_tolerance = self.upper_tolerance
        lower_tolerance = self.lower_tolerance
        warning_limit = self.warning_limit
        control_limit = self.control_limit
        inspection_equipement = self.inspection_equipement
        references = []
        for references_item_data in self.references:
            references_item = references_item_data.to_dict()

            references.append(references_item)

        sample_batch = []
        for sample_batch_item_data in self.sample_batch:
            sample_batch_item = sample_batch_item_data.to_dict()

            sample_batch.append(sample_batch_item)

        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "featureType": feature_type,
                "function": function,
                "unit": unit,
                "targetValue": target_value,
                "upperTolerance": upper_tolerance,
                "lowerTolerance": lower_tolerance,
                "warningLimit": warning_limit,
                "controlLimit": control_limit,
                "inspectionEquipement": inspection_equipement,
                "references": references,
                "sampleBatch": sample_batch,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.references import References
        from ..models.sample_batch import SampleBatch

        d = src_dict.copy()
        id_short = d.pop("id_short")

        feature_type = d.pop("featureType")

        function = d.pop("function")

        unit = d.pop("unit")

        target_value = d.pop("targetValue")

        upper_tolerance = d.pop("upperTolerance")

        lower_tolerance = d.pop("lowerTolerance")

        warning_limit = d.pop("warningLimit")

        control_limit = d.pop("controlLimit")

        inspection_equipement = d.pop("inspectionEquipement")

        references = []
        _references = d.pop("references")
        for references_item_data in _references:
            references_item = References.from_dict(references_item_data)

            references.append(references_item)

        sample_batch = []
        _sample_batch = d.pop("sampleBatch")
        for sample_batch_item_data in _sample_batch:
            sample_batch_item = SampleBatch.from_dict(sample_batch_item_data)

            sample_batch.append(sample_batch_item)

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        quality_feature_name = cls(
            id_short=id_short,
            feature_type=feature_type,
            function=function,
            unit=unit,
            target_value=target_value,
            upper_tolerance=upper_tolerance,
            lower_tolerance=lower_tolerance,
            warning_limit=warning_limit,
            control_limit=control_limit,
            inspection_equipement=inspection_equipement,
            references=references,
            sample_batch=sample_batch,
            description=description,
            semantic_id=semantic_id,
        )

        quality_feature_name.additional_properties = d
        return quality_feature_name

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
