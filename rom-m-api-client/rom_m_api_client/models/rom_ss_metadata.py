from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RomSSMetadata")


@_attrs_define
class RomSSMetadata:
    """
    Attributes:
        bezel_url (None | str | Unset):
        box2d_url (None | str | Unset):
        box2d_side_url (None | str | Unset):
        box2d_back_url (None | str | Unset):
        box3d_url (None | str | Unset):
        fanart_url (None | str | Unset):
        fullbox_url (None | str | Unset):
        logo_url (None | str | Unset):
        manual_url (None | str | Unset):
        marquee_url (None | str | Unset):
        miximage_url (None | str | Unset):
        physical_url (None | str | Unset):
        screenshot_url (None | str | Unset):
        steamgrid_url (None | str | Unset):
        title_screen_url (None | str | Unset):
        video_url (None | str | Unset):
        video_normalized_url (None | str | Unset):
        bezel_path (None | str | Unset):
        box2d_back_path (None | str | Unset):
        box3d_path (None | str | Unset):
        fanart_path (None | str | Unset):
        miximage_path (None | str | Unset):
        physical_path (None | str | Unset):
        marquee_path (None | str | Unset):
        logo_path (None | str | Unset):
        video_path (None | str | Unset):
        ss_score (None | str | Unset):
        first_release_date (int | None | Unset):
        alternative_names (list[str] | Unset):
        companies (list[str] | Unset):
        franchises (list[str] | Unset):
        game_modes (list[str] | Unset):
        genres (list[str] | Unset):
        player_count (str | Unset):
    """

    bezel_url: None | str | Unset = UNSET
    box2d_url: None | str | Unset = UNSET
    box2d_side_url: None | str | Unset = UNSET
    box2d_back_url: None | str | Unset = UNSET
    box3d_url: None | str | Unset = UNSET
    fanart_url: None | str | Unset = UNSET
    fullbox_url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    manual_url: None | str | Unset = UNSET
    marquee_url: None | str | Unset = UNSET
    miximage_url: None | str | Unset = UNSET
    physical_url: None | str | Unset = UNSET
    screenshot_url: None | str | Unset = UNSET
    steamgrid_url: None | str | Unset = UNSET
    title_screen_url: None | str | Unset = UNSET
    video_url: None | str | Unset = UNSET
    video_normalized_url: None | str | Unset = UNSET
    bezel_path: None | str | Unset = UNSET
    box2d_back_path: None | str | Unset = UNSET
    box3d_path: None | str | Unset = UNSET
    fanart_path: None | str | Unset = UNSET
    miximage_path: None | str | Unset = UNSET
    physical_path: None | str | Unset = UNSET
    marquee_path: None | str | Unset = UNSET
    logo_path: None | str | Unset = UNSET
    video_path: None | str | Unset = UNSET
    ss_score: None | str | Unset = UNSET
    first_release_date: int | None | Unset = UNSET
    alternative_names: list[str] | Unset = UNSET
    companies: list[str] | Unset = UNSET
    franchises: list[str] | Unset = UNSET
    game_modes: list[str] | Unset = UNSET
    genres: list[str] | Unset = UNSET
    player_count: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bezel_url: None | str | Unset
        if isinstance(self.bezel_url, Unset):
            bezel_url = UNSET
        else:
            bezel_url = self.bezel_url

        box2d_url: None | str | Unset
        if isinstance(self.box2d_url, Unset):
            box2d_url = UNSET
        else:
            box2d_url = self.box2d_url

        box2d_side_url: None | str | Unset
        if isinstance(self.box2d_side_url, Unset):
            box2d_side_url = UNSET
        else:
            box2d_side_url = self.box2d_side_url

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

        fullbox_url: None | str | Unset
        if isinstance(self.fullbox_url, Unset):
            fullbox_url = UNSET
        else:
            fullbox_url = self.fullbox_url

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

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

        steamgrid_url: None | str | Unset
        if isinstance(self.steamgrid_url, Unset):
            steamgrid_url = UNSET
        else:
            steamgrid_url = self.steamgrid_url

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

        video_normalized_url: None | str | Unset
        if isinstance(self.video_normalized_url, Unset):
            video_normalized_url = UNSET
        else:
            video_normalized_url = self.video_normalized_url

        bezel_path: None | str | Unset
        if isinstance(self.bezel_path, Unset):
            bezel_path = UNSET
        else:
            bezel_path = self.bezel_path

        box2d_back_path: None | str | Unset
        if isinstance(self.box2d_back_path, Unset):
            box2d_back_path = UNSET
        else:
            box2d_back_path = self.box2d_back_path

        box3d_path: None | str | Unset
        if isinstance(self.box3d_path, Unset):
            box3d_path = UNSET
        else:
            box3d_path = self.box3d_path

        fanart_path: None | str | Unset
        if isinstance(self.fanart_path, Unset):
            fanart_path = UNSET
        else:
            fanart_path = self.fanart_path

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

        logo_path: None | str | Unset
        if isinstance(self.logo_path, Unset):
            logo_path = UNSET
        else:
            logo_path = self.logo_path

        video_path: None | str | Unset
        if isinstance(self.video_path, Unset):
            video_path = UNSET
        else:
            video_path = self.video_path

        ss_score: None | str | Unset
        if isinstance(self.ss_score, Unset):
            ss_score = UNSET
        else:
            ss_score = self.ss_score

        first_release_date: int | None | Unset
        if isinstance(self.first_release_date, Unset):
            first_release_date = UNSET
        else:
            first_release_date = self.first_release_date

        alternative_names: list[str] | Unset = UNSET
        if not isinstance(self.alternative_names, Unset):
            alternative_names = self.alternative_names

        companies: list[str] | Unset = UNSET
        if not isinstance(self.companies, Unset):
            companies = self.companies

        franchises: list[str] | Unset = UNSET
        if not isinstance(self.franchises, Unset):
            franchises = self.franchises

        game_modes: list[str] | Unset = UNSET
        if not isinstance(self.game_modes, Unset):
            game_modes = self.game_modes

        genres: list[str] | Unset = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        player_count = self.player_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bezel_url is not UNSET:
            field_dict["bezel_url"] = bezel_url
        if box2d_url is not UNSET:
            field_dict["box2d_url"] = box2d_url
        if box2d_side_url is not UNSET:
            field_dict["box2d_side_url"] = box2d_side_url
        if box2d_back_url is not UNSET:
            field_dict["box2d_back_url"] = box2d_back_url
        if box3d_url is not UNSET:
            field_dict["box3d_url"] = box3d_url
        if fanart_url is not UNSET:
            field_dict["fanart_url"] = fanart_url
        if fullbox_url is not UNSET:
            field_dict["fullbox_url"] = fullbox_url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
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
        if steamgrid_url is not UNSET:
            field_dict["steamgrid_url"] = steamgrid_url
        if title_screen_url is not UNSET:
            field_dict["title_screen_url"] = title_screen_url
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if video_normalized_url is not UNSET:
            field_dict["video_normalized_url"] = video_normalized_url
        if bezel_path is not UNSET:
            field_dict["bezel_path"] = bezel_path
        if box2d_back_path is not UNSET:
            field_dict["box2d_back_path"] = box2d_back_path
        if box3d_path is not UNSET:
            field_dict["box3d_path"] = box3d_path
        if fanart_path is not UNSET:
            field_dict["fanart_path"] = fanart_path
        if miximage_path is not UNSET:
            field_dict["miximage_path"] = miximage_path
        if physical_path is not UNSET:
            field_dict["physical_path"] = physical_path
        if marquee_path is not UNSET:
            field_dict["marquee_path"] = marquee_path
        if logo_path is not UNSET:
            field_dict["logo_path"] = logo_path
        if video_path is not UNSET:
            field_dict["video_path"] = video_path
        if ss_score is not UNSET:
            field_dict["ss_score"] = ss_score
        if first_release_date is not UNSET:
            field_dict["first_release_date"] = first_release_date
        if alternative_names is not UNSET:
            field_dict["alternative_names"] = alternative_names
        if companies is not UNSET:
            field_dict["companies"] = companies
        if franchises is not UNSET:
            field_dict["franchises"] = franchises
        if game_modes is not UNSET:
            field_dict["game_modes"] = game_modes
        if genres is not UNSET:
            field_dict["genres"] = genres
        if player_count is not UNSET:
            field_dict["player_count"] = player_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bezel_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bezel_url = _parse_bezel_url(d.pop("bezel_url", UNSET))

        def _parse_box2d_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        box2d_url = _parse_box2d_url(d.pop("box2d_url", UNSET))

        def _parse_box2d_side_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        box2d_side_url = _parse_box2d_side_url(d.pop("box2d_side_url", UNSET))

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

        def _parse_fullbox_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fullbox_url = _parse_fullbox_url(d.pop("fullbox_url", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

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

        def _parse_steamgrid_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        steamgrid_url = _parse_steamgrid_url(d.pop("steamgrid_url", UNSET))

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

        def _parse_video_normalized_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_normalized_url = _parse_video_normalized_url(d.pop("video_normalized_url", UNSET))

        def _parse_bezel_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bezel_path = _parse_bezel_path(d.pop("bezel_path", UNSET))

        def _parse_box2d_back_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        box2d_back_path = _parse_box2d_back_path(d.pop("box2d_back_path", UNSET))

        def _parse_box3d_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        box3d_path = _parse_box3d_path(d.pop("box3d_path", UNSET))

        def _parse_fanart_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fanart_path = _parse_fanart_path(d.pop("fanart_path", UNSET))

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

        def _parse_logo_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_path = _parse_logo_path(d.pop("logo_path", UNSET))

        def _parse_video_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_path = _parse_video_path(d.pop("video_path", UNSET))

        def _parse_ss_score(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ss_score = _parse_ss_score(d.pop("ss_score", UNSET))

        def _parse_first_release_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_release_date = _parse_first_release_date(d.pop("first_release_date", UNSET))

        alternative_names = cast(list[str], d.pop("alternative_names", UNSET))

        companies = cast(list[str], d.pop("companies", UNSET))

        franchises = cast(list[str], d.pop("franchises", UNSET))

        game_modes = cast(list[str], d.pop("game_modes", UNSET))

        genres = cast(list[str], d.pop("genres", UNSET))

        player_count = d.pop("player_count", UNSET)

        rom_ss_metadata = cls(
            bezel_url=bezel_url,
            box2d_url=box2d_url,
            box2d_side_url=box2d_side_url,
            box2d_back_url=box2d_back_url,
            box3d_url=box3d_url,
            fanart_url=fanart_url,
            fullbox_url=fullbox_url,
            logo_url=logo_url,
            manual_url=manual_url,
            marquee_url=marquee_url,
            miximage_url=miximage_url,
            physical_url=physical_url,
            screenshot_url=screenshot_url,
            steamgrid_url=steamgrid_url,
            title_screen_url=title_screen_url,
            video_url=video_url,
            video_normalized_url=video_normalized_url,
            bezel_path=bezel_path,
            box2d_back_path=box2d_back_path,
            box3d_path=box3d_path,
            fanart_path=fanart_path,
            miximage_path=miximage_path,
            physical_path=physical_path,
            marquee_path=marquee_path,
            logo_path=logo_path,
            video_path=video_path,
            ss_score=ss_score,
            first_release_date=first_release_date,
            alternative_names=alternative_names,
            companies=companies,
            franchises=franchises,
            game_modes=game_modes,
            genres=genres,
            player_count=player_count,
        )

        rom_ss_metadata.additional_properties = d
        return rom_ss_metadata

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
