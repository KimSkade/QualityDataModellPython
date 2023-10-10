from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="References")


@attr.s(auto_attribs=True)
class References:
    """
    Attributes:
        id_short (str):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
        point (Union[Unset, str]):
        line (Union[Unset, str]):
        surface (Union[Unset, str]):
        axis (Union[Unset, str]):
    """

    id_short: str
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    point: Union[Unset, str] = UNSET
    line: Union[Unset, str] = UNSET
    surface: Union[Unset, str] = UNSET
    axis: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        description = self.description
        semantic_id = self.semantic_id
        point = self.point
        line = self.line
        surface = self.surface
        axis = self.axis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id
        if point is not UNSET:
            field_dict["point"] = point
        if line is not UNSET:
            field_dict["line"] = line
        if surface is not UNSET:
            field_dict["surface"] = surface
        if axis is not UNSET:
            field_dict["axis"] = axis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_short = d.pop("id_short")

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        point = d.pop("point", UNSET)

        line = d.pop("line", UNSET)

        surface = d.pop("surface", UNSET)

        axis = d.pop("axis", UNSET)

        references = cls(
            id_short=id_short,
            description=description,
            semantic_id=semantic_id,
            point=point,
            line=line,
            surface=surface,
            axis=axis,
        )

        references.additional_properties = d
        return references

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
