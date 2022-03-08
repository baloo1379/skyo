from sqlalchemy import Column, Integer, String, Boolean

from app.database.connection import Base


class TwitchData(Base):
    __tablename__ = "twt"

    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String)
    watch_time = Column(Integer)
    stream_time = Column(Integer)
    peak_viewers = Column(Integer)
    average_viewers = Column(Integer)
    followers = Column(Integer)
    followers_gained = Column(Integer)
    views_gained = Column(Integer)
    partnered = Column(Boolean)
    mature = Column(Boolean)
    language = Column(String)

    def as_dict(self):
        return {
            "id": self.id,
            "channel": self.channel,
            "watch_time": self.watch_time,
            "stream_time": self.stream_time,
            "peak_viewers": self.peak_viewers,
            "average_viewers": self.average_viewers,
            "followers": self.followers,
            "followers_gained": self.followers_gained,
            "views_gained": self.views_gained,
            "partnered": self.partnered,
            "mature": self.mature,
            "language": self.language,
        }
