from sqlalchemy import update
from sqlalchemy.orm import Session

from app.models.twitchdata import TwitchData as TwitchDataEntity
from app.schemas.twitchdata import TwitchDataCreate, TwitchDataOptional


def get_objects(db: Session) -> list[TwitchDataEntity]:
    return db.query(TwitchDataEntity).all()


def get_objects_by_filters(db: Session, entry: TwitchDataOptional) -> list[TwitchDataEntity]:
    parameters = entry.dict(exclude_none=True)
    if parameters:
        return db.query(TwitchDataEntity).filter_by(**parameters).all()
    else:
        return get_objects(db)


def get_object_by_id(db: Session, idx: int) -> TwitchDataEntity:
    return db.query(TwitchDataEntity).filter_by(id=idx).first()


def save_object(db: Session, entry: TwitchDataCreate) -> TwitchDataEntity:
    db_entry = TwitchDataEntity(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def find_and_update_object(db: Session, idx: int, entry: TwitchDataCreate) -> TwitchDataEntity:
    db.execute(update(TwitchDataEntity).where(TwitchDataEntity.id == idx).values(**entry.dict()))
    db.commit()
    return get_object_by_id(db, idx)
