from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ejs_controls_0 import EjsControls0
    from ..models.ejs_controls_1 import EjsControls1
    from ..models.ejs_controls_2 import EjsControls2
    from ..models.ejs_controls_3 import EjsControls3


T = TypeVar("T", bound="EjsControls")


@_attrs_define
class EjsControls:
    """
    Attributes:
        field_0 (EjsControls0):
        field_1 (EjsControls1):
        field_2 (EjsControls2):
        field_3 (EjsControls3):
    """

    field_0: EjsControls0
    field_1: EjsControls1
    field_2: EjsControls2
    field_3: EjsControls3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_0 = self.field_0.to_dict()

        field_1 = self.field_1.to_dict()

        field_2 = self.field_2.to_dict()

        field_3 = self.field_3.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_0": field_0,
                "_1": field_1,
                "_2": field_2,
                "_3": field_3,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ejs_controls_0 import EjsControls0
        from ..models.ejs_controls_1 import EjsControls1
        from ..models.ejs_controls_2 import EjsControls2
        from ..models.ejs_controls_3 import EjsControls3

        d = dict(src_dict)
        field_0 = EjsControls0.from_dict(d.pop("_0"))

        field_1 = EjsControls1.from_dict(d.pop("_1"))

        field_2 = EjsControls2.from_dict(d.pop("_2"))

        field_3 = EjsControls3.from_dict(d.pop("_3"))

        ejs_controls = cls(
            field_0=field_0,
            field_1=field_1,
            field_2=field_2,
            field_3=field_3,
        )

        ejs_controls.additional_properties = d
        return ejs_controls

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
