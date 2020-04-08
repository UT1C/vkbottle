from . import photos, base
import typing
from enum import Enum
from ..base import BaseModel
from vkbottle.types import objects


class Currency(BaseModel):
    id: int = None
    name: str = None


class MarketAlbum(BaseModel):
    count: int = None
    id: int = None
    owner_id: int = None
    photo: "photos.Photo" = None
    title: str = None
    updated_time: int = None


class MarketCategory(BaseModel):
    id: int = None
    name: str = None
    section: "Section" = None


class MarketItem(BaseModel):
    access_key: str = None
    availability: "MarketItemAvailability" = None
    button_title: str = None
    category: "MarketCategory" = None
    date: int = None
    description: str = None
    external_id: str = None
    id: int = None
    is_favorite: bool = None
    owner_id: int = None
    price: "Price" = None
    thumb_photo: str = None
    title: str = None
    url: str = None


class MarketItemAvailability(Enum):
    _0 = "0"
    _1 = "1"
    _2 = "2"


class MarketItemFull(MarketItem):
    albums_ids: typing.List = None
    photos: typing.List = None
    can_comment: "base.BoolInt" = None
    can_repost: "base.BoolInt" = None
    likes: "base.Likes" = None
    reposts: "base.RepostsInfo" = None
    views_count: int = None


class Price(BaseModel):
    amount: str = None
    currency: "Currency" = None
    discount_rate: int = None
    old_amount: str = None
    text: str = None


class Section(BaseModel):
    id: int = None
    name: str = None


