from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_machine_parameter import NewMachineParameter
    from ..models.process_datas import ProcessDatas


T = TypeVar("T", bound="ProcedureData")


@attr.s(auto_attribs=True)
class ProcedureData:
    """
    Attributes:
        id_short (str):
        process_data (ProcessDatas):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
        new_machine_parameter (Union[Unset, NewMachineParameter]):
    """

    id_short: str
    process_data: "ProcessDatas"
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    new_machine_parameter: Union[Unset, "NewMachineParameter"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        process_data = self.process_data.to_dict()

        description = self.description
        semantic_id = self.semantic_id
        new_machine_parameter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_machine_parameter, Unset):
            new_machine_parameter = self.new_machine_parameter.to_dict()

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
        if new_machine_parameter is not UNSET:
            field_dict["new_machine_parameter"] = new_machine_parameter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_machine_parameter import NewMachineParameter
        from ..models.process_datas import ProcessDatas

        d = src_dict.copy()
        id_short = d.pop("id_short")

        process_data = ProcessDatas.from_dict(d.pop("process_data"))

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        _new_machine_parameter = d.pop("new_machine_parameter", UNSET)
        new_machine_parameter: Union[Unset, NewMachineParameter]
        if isinstance(_new_machine_parameter, Unset):
            new_machine_parameter = UNSET
        else:
            new_machine_parameter = NewMachineParameter.from_dict(_new_machine_parameter)

        procedure_data = cls(
            id_short=id_short,
            process_data=process_data,
            description=description,
            semantic_id=semantic_id,
            new_machine_parameter=new_machine_parameter,
        )

        procedure_data.additional_properties = d
        return procedure_data

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
