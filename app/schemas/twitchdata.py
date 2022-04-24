from pydantic import BaseModel
from typing import Union


class TwitchDataCreate(BaseModel):
    channel: str
    watch_time: int
    stream_time: int
    peak_viewers: int
    average_viewers: int
    followers: int
    followers_gained: int
    views_gained: int
    partnered: bool
    mature: bool
    language: str


class TwitchData(TwitchDataCreate):
    id: int

    class Config:
        orm_mode = True


class TwitchDataOptional(BaseModel):
    id: Union[int, None]
    channel: Union[str, None]
    watch_time: Union[int, None]
    stream_time: Union[int, None]
    peak_viewers: Union[int, None]
    average_viewers: Union[int, None]
    followers: Union[int, None]
    followers_gained: Union[int, None]
    views_gained: Union[int, None]
    partnered: Union[bool, None]
    mature: Union[bool, None]
    language: Union[str, None]
