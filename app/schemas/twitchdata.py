from pydantic import BaseModel


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
    id: int | None
    channel: str | None
    watch_time: int | None
    stream_time: int | None
    peak_viewers: int | None
    average_viewers: int | None
    followers: int | None
    followers_gained: int | None
    views_gained: int | None
    partnered: bool | None
    mature: bool | None
    language: str | None
