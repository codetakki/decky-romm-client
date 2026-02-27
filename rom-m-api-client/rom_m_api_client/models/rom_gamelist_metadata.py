from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RomGamelistMetadata")


@_attrs_define
class RomGamelistMetadata:
    """
    Attributes:
        box2d_url (None | str | Unset):
        box2d_back_url (None | str | Unset):
        box3d_url (None | str | Unset):
        fanart_url (None | str | Unset):
        image_url (None | str | Unset):
        manual_url (None | str | Unset):
        marquee_url (None | str | Unset):
        miximage_url (None | str | Unset):
        physical_url (None | str | Unset):
        screenshot_url (None | str | Unset):
        thumbnail_url (None | str | Unset):
        title_screen_url (None | str | Unset):
        video_url (None | str | Unset):
        rating (float | None | Unset):
        first_release_date (None | str | Unset):
        companies (list[str] | None | Unset):
        franchises (list[str] | None | Unset):
        genres (list[str] | None | Unset):
        player_count (None | str | Unset):
        md5_hash (None | str | Unset):
        box3d_path (None | str | Unset):
        miximage_path (None | str | Unset):
        physical_path (None | str | Unset):
        marquee_path (None | str | Unset):
        video_path (None | str | Unset):
    """

    box2d_url: None | str | Unset = UNSET
    box2d_back_url: None | str | Unset = UNSET
    box3d_url: None | str | Unset = UNSET
    fanart_url: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    manual_url: None | str | Unset = UNSET
    marquee_url: None | str | Unset = UNSET
    miximage_url: None | str | Unset = UNSET
    physical_url: None | str | Unset = UNSET
    screenshot_url: None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    title_screen_url: None | str | Unset = UNSET
    video_url: None | str | Unset = UNSET
    rating: float | None | Unset = UNSET
    first_release_date: None | str | Unset = UNSET
    companies: list[str] | None | Unset = UNSET
    franchises: list[str] | None | Unset = UNSET
    genres: list[str] | None | Unset = UNSET
    player_count: None | str | Unset = UNSET
    md5_hash: None | str | Unset = UNSET
    box3d_path: None | str | Unset = UNSET
    miximage_path: None | str | Unset = UNSET
    physical_path: None | str | Unset = UNSET
    marquee_path: None | str | Unset = UNSET
    video_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        box2d_url: None | str | Unset
        if isinstance(self.box2d_url, Unset):
            box2d_url = UNSET
        else:
            box2d_url = self.box2d_url

        box2d_back_url: None | str | Unset
        if isinstance(self.box2d_back_url, Unset):
            box2d_back_url = UNSET
        else:
            box2d_back_url = self.box2d_back_url

        box3d_url: None | str | Unset
        if isinstance(self.box3d_url, Unset):
            box3d_url = UNSET
        else:
            box3d_url = self.box3d_url

        fanart_url: None | str | Unset
        if isinstance(self.fanart_url, Unset):
            fanart_url = UNSET
        else:
            fanart_url = self.fanart_url

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        manual_url: None | str | Unset
        if isinstance(self.manual_url, Unset):
            manual_url = UNSET
        else:
            manual_url = self.manual_url

        marquee_url: None | str | Unset
        if isinstance(self.marquee_url, Unset):
            marquee_url = UNSET
        else:
            marquee_url = self.marquee_url

        miximage_url: None | str | Unset
        if isinstance(self.miximage_url, Unset):
            miximage_url = UNSET
        else:
            miximage_url = self.miximage_url

        physical_url: None | str | Unset
        if isinstance(self.physical_url, Unset):
            physical_url = UNSET
        else:
            physical_url = self.physical_url

        screenshot_url: None | str | Unset
        if isinstance(self.screenshot_url, Unset):
            screenshot_url = UNSET
        else:
            screenshot_url = self.screenshot_url

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        title_screen_url: None | str | Unset
        if isinstance(self.title_screen_url, Unset):
            title_screen_url = UNSET
        else:
            title_screen_url = self.title_screen_url

        video_url: None | str | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        else:
            video_url = self.video_url

        rating: float | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        first_release_date: None | str | Unset
        if isinstance(self.first_release_date, Unset):
            first_release_date = UNSET
        else:
            first_release_date = self.first_release_date

        companies: list[str] | None | Unset
        if isinstance(self.companies, Unset):
            companies = UNSET
        elif isinstance(self.companies, list):
            companies = self.companies

        else:
            companies = self.companies

        franchises: list[str] | None | Unset
        if isinstance(self.franchises, Unset):
            franchises = UNSET
        elif isinstance(self.franchises, list):
            franchises = self.franchises

        else:
            franchises = self.franchises

        genres: list[str] | None | Unset
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        player_count: None | str | Unset
        if isinstance(self.player_count, Unset):
            player_count = UNSET
        else:
            player_count = self.player_count

        md5_hash: None | str | Unset
        if isinstance(self.md5_hash, Unset):
            md5_hash = UNSET
        else:
            md5_hash = self.md5_hash

        box3d_path: None | str | Unset
        if isinstance(self.box3d_path, Unset):
            box3d_path = UNSET
        else:
            box3d_path = self.box3d_path

        miximage_path: None | str | Unset
        if isinstance(self.miximage_path, Unset):
            miximage_path = UNSET
        else:
            miximage_path = self.miximage_path

        physical_path: None | str | Unset
        if isinstance(self.physical_path, Unset):
            physical_path = UNSET
        else:
            physical_path = self.physical_path

        marquee_path: None | str | Unset
        if isinstance(self.marquee_path, Unset):
            marquee_path = UNSET
        else:
            marquee_path = self.marquee_path

        video_path: None | str | Unset
        if isinstance(self.video_path, Unset):
            video_path = UNSET
        else:
            video_path = self.video_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if box2d_url is not UNSET:
            field_dict["box2d_url"] = box2d_url
        if box2d_back_url is not UNSET:
            field_dict["box2d_back_url"] = box2d_back_url
        if box3d_url is not UNSET:
            field_dict["box3d_url"] = box3d_url
        if fanart_url is not UNSET:
            field_dict["fanart_url"] = fanart_url
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if manual_url is not UNSET:
            field_dict["manual_url"] = manual_url
        if marquee_url is not UNSET:
            field_dict["marquee_url"] = marquee_url
        if miximage_url is not UNSET:
            field_dict["miximage_url"] = miximage_url
        if physical_url is not UNSET:
            field_dict["physical_url"] = physical_url
        if screenshot_url is not UNSET:
            field_dict["screenshot_url"] = screenshot_url
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if title_screen_url is not UNSET:
            field_dict["title_screen_url"] = title_screen_url
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if rating is not UNSET:
            field_dict["rating"] = rating
        if first_release_date is not UNSET:
            field_dict["first_release_date"] = first_release_date
        if companies is not UNSET:
            field_dict["companies"] = companies
        if franchises is not UNSET:
            field_dict["franchises"] = franchises
        if genres is not UNSET:
            field_dict["genres"] = genres
        if player_count is not UNSET:
            field_dict["player_count"] = player_count
        if md5_hash is not UNSET:
            field_dict["md5_hash"] = md5_hash
        if box3d_path is not UNSET:
            field_dict["box3d_path"] = box3d_path
        if miximage_path is not UNSET:
            field_dict["miximage_path"] = miximage_path
        if physical_path is not UNSET:
            field_dict["physical_path"] = physical_path
        if marquee_path is not UNSET:
            field_dict["marquee_path"] = marquee_path
        if video_path is not UNSET:
            field_dict["video_path"] = video_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_box2d_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        box2d_url = _parse_box2d_url(d.pop("box2d_url", UNSET))

        def _parse_box2d_back_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        box2d_back_url = _parse_box2d_back_url(d.pop("box2d_back_url", UNSET))

        def _parse_box3d_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        box3d_url = _parse_box3d_url(d.pop("box3d_url", UNSET))

        def _parse_fanart_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fanart_url = _parse_fanart_url(d.pop("fanart_url", UNSET))

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("image_url", UNSET))

        def _parse_manual_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manual_url = _parse_manual_url(d.pop("manual_url", UNSET))

        def _parse_marquee_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marquee_url = _parse_marquee_url(d.pop("marquee_url", UNSET))

        def _parse_miximage_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        miximage_url = _parse_miximage_url(d.pop("miximage_url", UNSET))

        def _parse_physical_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        physical_url = _parse_physical_url(d.pop("physical_url", UNSET))

        def _parse_screenshot_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        screenshot_url = _parse_screenshot_url(d.pop("screenshot_url", UNSET))

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnail_url", UNSET))

        def _parse_title_screen_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_screen_url = _parse_title_screen_url(d.pop("title_screen_url", UNSET))

        def _parse_video_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_url = _parse_video_url(d.pop("video_url", UNSET))

        def _parse_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))

        def _parse_first_release_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_release_date = _parse_first_release_date(d.pop("first_release_date", UNSET))

        def _parse_companies(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                companies_type_0 = cast(list[str], data)

                return companies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        companies = _parse_companies(d.pop("companies", UNSET))

        def _parse_franchises(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                franchises_type_0 = cast(list[str], data)

                return franchises_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        franchises = _parse_franchises(d.pop("franchises", UNSET))

        def _parse_genres(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = cast(list[str], data)

                return genres_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        genres = _parse_genres(d.pop("genres", UNSET))

        def _parse_player_count(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        player_count = _parse_player_count(d.pop("player_count", UNSET))

        def _parse_md5_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        md5_hash = _parse_md5_hash(d.pop("md5_hash", UNSET))

        def _parse_box3d_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        box3d_path = _parse_box3d_path(d.pop("box3d_path", UNSET))

        def _parse_miximage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        miximage_path = _parse_miximage_path(d.pop("miximage_path", UNSET))

        def _parse_physical_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        physical_path = _parse_physical_path(d.pop("physical_path", UNSET))

        def _parse_marquee_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marquee_path = _parse_marquee_path(d.pop("marquee_path", UNSET))

        def _parse_video_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_path = _parse_video_path(d.pop("video_path", UNSET))

        rom_gamelist_metadata = cls(
            box2d_url=box2d_url,
            box2d_back_url=box2d_back_url,
            box3d_url=box3d_url,
            fanart_url=fanart_url,
            image_url=image_url,
            manual_url=manual_url,
            marquee_url=marquee_url,
            miximage_url=miximage_url,
            physical_url=physical_url,
            screenshot_url=screenshot_url,
            thumbnail_url=thumbnail_url,
            title_screen_url=title_screen_url,
            video_url=video_url,
            rating=rating,
            first_release_date=first_release_date,
            companies=companies,
            franchises=franchises,
            genres=genres,
            player_count=player_count,
            md5_hash=md5_hash,
            box3d_path=box3d_path,
            miximage_path=miximage_path,
            physical_path=physical_path,
            marquee_path=marquee_path,
            video_path=video_path,
        )

        rom_gamelist_metadata.additional_properties = d
        return rom_gamelist_metadata

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
