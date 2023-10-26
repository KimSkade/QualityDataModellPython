from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quality_data import QualityData


T = TypeVar("T", bound="QualityDataAAS")


@attr.s(auto_attribs=True)
class QualityDataAAS:
    """
    Attributes:
        id (str):
        quality_data (QualityData):
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
                "quality_data": quality_data,
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

        quality_data = QualityData.from_dict(d.pop("quality_data"))

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
