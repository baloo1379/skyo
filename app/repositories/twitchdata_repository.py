from sqlalchemy import column
from sqlalchemy.orm import Session

from app.models.twitchdata import TwitchData as TwitchDataEntity
from app.models.twitchstats import Chart
from app.schemas.twitchdata import TwitchDataCreate, TwitchDataOptional

def get_stats(db: Session) -> list[Chart]:
    objects = get_objects(db)
    return {
        Chart("watch_time", [row.watch_time for row in objects]),
        Chart("stream_time", [row.stream_time for row in objects]),
        Chart("peak_viewers", [row.peak_viewers for row in objects]),
        Chart("average_viewers", [row.average_viewers for row in objects]),
        Chart("followers", [row.followers for row in objects]),
        Chart("followers_gained", [row.followers_gained for row in objects]),
        Chart("views_gained", [row.views_gained for row in objects]),
        Chart("partnered", [row.partnered for row in objects]),
        Chart("mature", [row.mature for row in objects])
    }

def get_objects(db: Session) -> list[TwitchDataEntity]:
    return db.query(TwitchDataEntity).all()


def get_objects_by_filters(db: Session, entry: TwitchDataOptional) -> list[TwitchDataEntity]:
    parameters = entry.dict(exclude_none=True)
    if parameters:
        return db.query(TwitchDataEntity).filter_by(**parameters).all()
    else:
        return get_objects(db)

def save_object(db: Session, entry: TwitchDataCreate) -> TwitchDataEntity:
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
