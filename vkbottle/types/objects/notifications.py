from . import base, wall, photos, board, video
import typing
from enum import Enum
from ..base import BaseModel
from vkbottle.types import objects


class Feedback(BaseModel):
    attachments: typing.List = None
    from_id: int = None
    geo: "base.Geo" = None
    id: int = None
    likes: "base.LikesInfo" = None
    text: str = None
    to_id: int = None


class Notification(BaseModel):
    date: int = None
    feedback: "Feedback" = None
    parent: "NotificationParent" = None
    reply: "Reply" = None
    type: str = None


class NotificationsComment(BaseModel):
    date: int = None
    id: int = None
    owner_id: int = None
    photo: "photos.Photo" = None
    post: "wall.Wallpost" = None
    text: str = None
    topic: "board.Topic" = None
    video: "video.Video" = None


class NotificationParent(
    wall.WallpostToId, photos.Photo, board.Topic, video.Video, NotificationsComment
):
    pass


class Reply(BaseModel):
    date: int = None
    id: int = None
    text: int = None


class SendMessageError(BaseModel):
    code: int = None
    description: str = None


class SendMessageItem(BaseModel):
    user_id: int = None
    status: bool = None
    error: "SendMessageError" = None


