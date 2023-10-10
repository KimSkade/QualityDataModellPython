from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_data import SampleData


T = TypeVar("T", bound="SampleBatch")


@attr.s(auto_attribs=True)
class SampleBatch:
    """
    Attributes:
        id_short (str):
        sample_size (int):
        sample_data (List['SampleData']):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    sample_size: int
    sample_data: List["SampleData"]
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        sample_size = self.sample_size
        sample_data = []
        for sample_data_item_data in self.sample_data:
            sample_data_item = sample_data_item_data.to_dict()

            sample_data.append(sample_data_item)

        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "sampleSize": sample_size,
                "sampleData": sample_data,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sample_data import SampleData

        d = src_dict.copy()
        id_short = d.pop("id_short")

        sample_size = d.pop("sampleSize")

        sample_data = []
        _sample_data = d.pop("sampleData")
        for sample_data_item_data in _sample_data:
            sample_data_item = SampleData.from_dict(sample_data_item_data)

            sample_data.append(sample_data_item)

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        sample_batch = cls(
            id_short=id_short,
            sample_size=sample_size,
            sample_data=sample_data,
            description=description,
            semantic_id=semantic_id,
        )

        sample_batch.additional_properties = d
        return sample_batch

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
