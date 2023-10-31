from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_data import ProcessData


T = TypeVar("T", bound="ProcessDatas")


@attr.s(auto_attribs=True)
class ProcessDatas:
    """
    Attributes:
        id_short (str):
        process_data (List['ProcessData']):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    process_data: List["ProcessData"]
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        process_data = []
        for process_data_item_data in self.process_data:
            process_data_item = process_data_item_data.to_dict()

            process_data.append(process_data_item)

        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "process_data": process_data,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.process_data import ProcessData

        d = src_dict.copy()
        id_short = d.pop("id_short")

        process_data = []
        _process_data = d.pop("process_data")
        for process_data_item_data in _process_data:
            process_data_item = ProcessData.from_dict(process_data_item_data)

            process_data.append(process_data_item)

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        process_datas = cls(
            id_short=id_short,
            process_data=process_data,
            description=description,
            semantic_id=semantic_id,
        )

        process_datas.additional_properties = d
        return process_datas

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
