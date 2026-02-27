from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.launchbox_image import LaunchboxImage


T = TypeVar("T", bound="RomLaunchboxMetadata")


@_attrs_define
class RomLaunchboxMetadata:
    """
    Attributes:
        first_release_date (int | None | Unset):
        max_players (int | Unset):
        release_type (str | Unset):
        cooperative (bool | Unset):
        youtube_video_id (str | Unset):
        community_rating (float | Unset):
        community_rating_count (int | Unset):
        wikipedia_url (str | Unset):
        esrb (str | Unset):
        genres (list[str] | Unset):
        companies (list[str] | Unset):
        images (list[LaunchboxImage] | Unset):
    """

    first_release_date: int | None | Unset = UNSET
    max_players: int | Unset = UNSET
    release_type: str | Unset = UNSET
    cooperative: bool | Unset = UNSET
    youtube_video_id: str | Unset = UNSET
    community_rating: float | Unset = UNSET
    community_rating_count: int | Unset = UNSET
    wikipedia_url: str | Unset = UNSET
    esrb: str | Unset = UNSET
    genres: list[str] | Unset = UNSET
    companies: list[str] | Unset = UNSET
    images: list[LaunchboxImage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_release_date: int | None | Unset
        if isinstance(self.first_release_date, Unset):
            first_release_date = UNSET
        else:
            first_release_date = self.first_release_date

        max_players = self.max_players

        release_type = self.release_type

        cooperative = self.cooperative

        youtube_video_id = self.youtube_video_id

        community_rating = self.community_rating

        community_rating_count = self.community_rating_count

        wikipedia_url = self.wikipedia_url

        esrb = self.esrb

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        companies: list[str] | Unset = UNSET
        if not isinstance(self.companies, Unset):
            companies = self.companies

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_release_date is not UNSET:
            field_dict["first_release_date"] = first_release_date
        if max_players is not UNSET:
            field_dict["max_players"] = max_players
        if release_type is not UNSET:
            field_dict["release_type"] = release_type
        if cooperative is not UNSET:
            field_dict["cooperative"] = cooperative
        if youtube_video_id is not UNSET:
            field_dict["youtube_video_id"] = youtube_video_id
        if community_rating is not UNSET:
            field_dict["community_rating"] = community_rating
        if community_rating_count is not UNSET:
            field_dict["community_rating_count"] = community_rating_count
        if wikipedia_url is not UNSET:
            field_dict["wikipedia_url"] = wikipedia_url
        if esrb is not UNSET:
            field_dict["esrb"] = esrb
        if genres is not UNSET:
            field_dict["genres"] = genres
        if companies is not UNSET:
            field_dict["companies"] = companies
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.launchbox_image import LaunchboxImage

        d = dict(src_dict)

        def _parse_first_release_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_release_date = _parse_first_release_date(d.pop("first_release_date", UNSET))

        max_players = d.pop("max_players", UNSET)

        release_type = d.pop("release_type", UNSET)

        cooperative = d.pop("cooperative", UNSET)

        youtube_video_id = d.pop("youtube_video_id", UNSET)

        community_rating = d.pop("community_rating", UNSET)

        community_rating_count = d.pop("community_rating_count", UNSET)

        wikipedia_url = d.pop("wikipedia_url", UNSET)

        esrb = d.pop("esrb", UNSET)

        genres = cast(list[str], d.pop("genres", UNSET))

        companies = cast(list[str], d.pop("companies", UNSET))

        _images = d.pop("images", UNSET)
        images: list[LaunchboxImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = LaunchboxImage.from_dict(images_item_data)

                images.append(images_item)

        rom_launchbox_metadata = cls(
            first_release_date=first_release_date,
            max_players=max_players,
            release_type=release_type,
            cooperative=cooperative,
            youtube_video_id=youtube_video_id,
            community_rating=community_rating,
            community_rating_count=community_rating_count,
            wikipedia_url=wikipedia_url,
            esrb=esrb,
            genres=genres,
            companies=companies,
            images=images,
        )

        rom_launchbox_metadata.additional_properties = d
        return rom_launchbox_metadata

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
