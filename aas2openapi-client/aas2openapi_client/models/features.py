from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quality_feature_name import QualityFeatureName


T = TypeVar("T", bound="Features")


@attr.s(auto_attribs=True)
class Features:
    """
    Attributes:
        id_short (str):
        quality_feature_name (List['QualityFeatureName']):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    quality_feature_name: List["QualityFeatureName"]
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        quality_feature_name = []
        for quality_feature_name_item_data in self.quality_feature_name:
            quality_feature_name_item = quality_feature_name_item_data.to_dict()

            quality_feature_name.append(quality_feature_name_item)

        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "qualityFeatureName": quality_feature_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.quality_feature_name import QualityFeatureName

        d = src_dict.copy()
        id_short = d.pop("id_short")

        quality_feature_name = []
        _quality_feature_name = d.pop("qualityFeatureName")
        for quality_feature_name_item_data in _quality_feature_name:
            quality_feature_name_item = QualityFeatureName.from_dict(quality_feature_name_item_data)

            quality_feature_name.append(quality_feature_name_item)

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        features = cls(
            id_short=id_short,
            quality_feature_name=quality_feature_name,
            description=description,
            semantic_id=semantic_id,
        )

        features.additional_properties = d
        return features

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
