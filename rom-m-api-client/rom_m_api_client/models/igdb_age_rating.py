from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IGDBAgeRating")


@_attrs_define
class IGDBAgeRating:
    """
    Attributes:
        rating (str):
        category (str):
        rating_cover_url (str):
    """

    rating: str
    category: str
    rating_cover_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rating = self.rating

        category = self.category

        rating_cover_url = self.rating_cover_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rating": rating,
                "category": category,
                "rating_cover_url": rating_cover_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rating = d.pop("rating")

        category = d.pop("category")

        rating_cover_url = d.pop("rating_cover_url")

        igdb_age_rating = cls(
            rating=rating,
            category=category,
            rating_cover_url=rating_cover_url,
        )

        igdb_age_rating.additional_properties = d
        return igdb_age_rating

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
