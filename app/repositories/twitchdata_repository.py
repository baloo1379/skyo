from sqlalchemy.orm import Session

from app.models.twitchdata import TwitchData as TwitchDataEntity
from app.schemas.twitchdata import TwitchDataCreate


def get_objects(db: Session) -> list[TwitchDataEntity]:
    return db.query(TwitchDataEntity).all()


def save_entry(db: Session, entry: TwitchDataCreate) -> TwitchDataEntity:
    db_entry = TwitchDataEntity(
        channel=entry.channel,
        watch_time=entry.watch_time,
        stream_time=entry.stream_time,
        peak_viewers=entry.peak_viewers,
        average_viewers=entry.average_viewers,
        followers=entry.followers,
        followers_gained=entry.followers_gained,
        views_gained=entry.views_gained,
        partnered=entry.partnered,
        mature=entry.mature,
        language=entry.language
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
