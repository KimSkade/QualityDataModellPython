from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_data import ProcessData


T = TypeVar("T", bound="Procedure")


@attr.s(auto_attribs=True)
class Procedure:
    """Base class for all submodels.

    Args:
        id (str): Global id of the object.
        id_short (str): Local id of the object.
        description (str, optional): Description of the object. Defaults to None.
        semantic_id (str, optional): Semantic id of the object. Defaults to None.

        Attributes:
            id_short (str):
            id (str):
            process_data (ProcessData): Base class for all submodel element collections.

                Args:
                    id_short (str): Local id of the object.
                    description (str, optional): Description of the object. Defaults to None.
                    semantic_id (str, optional): Semantic id of the object. Defaults to None.
            description (Union[Unset, str]):
            semantic_id (Union[Unset, str]):
    """

    id_short: str
    id: str
    process_data: "ProcessData"
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        id = self.id
        process_data = self.process_data.to_dict()

        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "id": id,
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

        id = d.pop("id")

        process_data = ProcessData.from_dict(d.pop("process_data"))

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        procedure = cls(
            id_short=id_short,
            id=id,
            process_data=process_data,
            description=description,
            semantic_id=semantic_id,
        )

        procedure.additional_properties = d
        return procedure

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
