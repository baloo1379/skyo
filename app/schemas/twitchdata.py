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
