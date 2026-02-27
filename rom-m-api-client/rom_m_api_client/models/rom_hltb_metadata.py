from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RomHLTBMetadata")


@_attrs_define
class RomHLTBMetadata:
    """
    Attributes:
        main_story (int | Unset):
        main_story_count (int | Unset):
        main_plus_extra (int | Unset):
        main_plus_extra_count (int | Unset):
        completionist (int | Unset):
        completionist_count (int | Unset):
        all_styles (int | Unset):
        all_styles_count (int | Unset):
        release_year (int | Unset):
        review_score (int | Unset):
        review_count (int | Unset):
        popularity (int | Unset):
        completions (int | Unset):
    """

    main_story: int | Unset = UNSET
    main_story_count: int | Unset = UNSET
    main_plus_extra: int | Unset = UNSET
    main_plus_extra_count: int | Unset = UNSET
    completionist: int | Unset = UNSET
    completionist_count: int | Unset = UNSET
    all_styles: int | Unset = UNSET
    all_styles_count: int | Unset = UNSET
    release_year: int | Unset = UNSET
    review_score: int | Unset = UNSET
    review_count: int | Unset = UNSET
    popularity: int | Unset = UNSET
    completions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_story = self.main_story

        main_story_count = self.main_story_count

        main_plus_extra = self.main_plus_extra

        main_plus_extra_count = self.main_plus_extra_count

        completionist = self.completionist

        completionist_count = self.completionist_count

        all_styles = self.all_styles

        all_styles_count = self.all_styles_count

        release_year = self.release_year

        review_score = self.review_score

        review_count = self.review_count

        popularity = self.popularity

        completions = self.completions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main_story is not UNSET:
            field_dict["main_story"] = main_story
        if main_story_count is not UNSET:
            field_dict["main_story_count"] = main_story_count
        if main_plus_extra is not UNSET:
            field_dict["main_plus_extra"] = main_plus_extra
        if main_plus_extra_count is not UNSET:
            field_dict["main_plus_extra_count"] = main_plus_extra_count
        if completionist is not UNSET:
            field_dict["completionist"] = completionist
        if completionist_count is not UNSET:
            field_dict["completionist_count"] = completionist_count
        if all_styles is not UNSET:
            field_dict["all_styles"] = all_styles
        if all_styles_count is not UNSET:
            field_dict["all_styles_count"] = all_styles_count
        if release_year is not UNSET:
            field_dict["release_year"] = release_year
        if review_score is not UNSET:
            field_dict["review_score"] = review_score
        if review_count is not UNSET:
            field_dict["review_count"] = review_count
        if popularity is not UNSET:
            field_dict["popularity"] = popularity
        if completions is not UNSET:
            field_dict["completions"] = completions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        main_story = d.pop("main_story", UNSET)

        main_story_count = d.pop("main_story_count", UNSET)

        main_plus_extra = d.pop("main_plus_extra", UNSET)

        main_plus_extra_count = d.pop("main_plus_extra_count", UNSET)

        completionist = d.pop("completionist", UNSET)

        completionist_count = d.pop("completionist_count", UNSET)

        all_styles = d.pop("all_styles", UNSET)

        all_styles_count = d.pop("all_styles_count", UNSET)

        release_year = d.pop("release_year", UNSET)

        review_score = d.pop("review_score", UNSET)

        review_count = d.pop("review_count", UNSET)

        popularity = d.pop("popularity", UNSET)

        completions = d.pop("completions", UNSET)

        rom_hltb_metadata = cls(
            main_story=main_story,
            main_story_count=main_story_count,
            main_plus_extra=main_plus_extra,
            main_plus_extra_count=main_plus_extra_count,
            completionist=completionist,
            completionist_count=completionist_count,
            all_styles=all_styles,
            all_styles_count=all_styles_count,
            release_year=release_year,
            review_score=review_score,
            review_count=review_count,
            popularity=popularity,
            completions=completions,
        )

        rom_hltb_metadata.additional_properties = d
        return rom_hltb_metadata

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
