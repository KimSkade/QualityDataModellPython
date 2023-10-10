from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Result")


@attr.s(auto_attribs=True)
class Result:
    """
    Attributes:
        id_short (str):
        value (float):
        measurement_date (str):
        uppertol (float):
        lowertol (float):
        nominal (float):
        result_check (bool):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    value: float
    measurement_date: str
    uppertol: float
    lowertol: float
    nominal: float
    result_check: bool
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        value = self.value
        measurement_date = self.measurement_date
        uppertol = self.uppertol
        lowertol = self.lowertol
        nominal = self.nominal
        result_check = self.result_check
        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "value": value,
                "measurementDate": measurement_date,
                "uppertol": uppertol,
                "lowertol": lowertol,
                "nominal": nominal,
                "resultCheck": result_check,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_short = d.pop("id_short")

        value = d.pop("value")

        measurement_date = d.pop("measurementDate")

        uppertol = d.pop("uppertol")

        lowertol = d.pop("lowertol")

        nominal = d.pop("nominal")

        result_check = d.pop("resultCheck")

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        result = cls(
            id_short=id_short,
            value=value,
            measurement_date=measurement_date,
            uppertol=uppertol,
            lowertol=lowertol,
            nominal=nominal,
            result_check=result_check,
            description=description,
            semantic_id=semantic_id,
        )

        result.additional_properties = d
        return result

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
