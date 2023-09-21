from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillOfMaterial")


@attr.s(auto_attribs=True)
class BillOfMaterial:
    """
    Attributes:
        id (str):
        components (List[str]):
        result_check (bool):
        description (Union[Unset, str]):
        id_short (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id: str
    components: List[str]
    result_check: bool
    description: Union[Unset, str] = UNSET
    id_short: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        components = self.components

        result_check = self.result_check
        description = self.description
        id_short = self.id_short
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_": id,
                "components": components,
                "result_check": result_check,
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
        d = src_dict.copy()
        id = d.pop("id_")

        components = cast(List[str], d.pop("components"))

        result_check = d.pop("result_check")

        description = d.pop("description", UNSET)

        id_short = d.pop("id_short", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        bill_of_material = cls(
            id=id,
            components=components,
            result_check=result_check,
            description=description,
            id_short=id_short,
            semantic_id=semantic_id,
        )

        bill_of_material.additional_properties = d
        return bill_of_material

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
