from fastapi import APIRouter, File, UploadFile, Depends
from fastapi_pagination import Page, paginate, Params
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.repositories.twitchdata_repository import get_objects, get_objects_by_filters
from app.schemas.twitchdata import TwitchData, TwitchDataCreate, TwitchDataOptional
from app.services.batch_insert import insert


router = APIRouter(prefix="/api/v1")


@router.get('/')
def health():
    """
    Simple checks the server status
    """
    return {"health": "ok"}


@router.post("/csv")
def upload_csv(data: UploadFile = File(...)):
    return insert(data.file)


@router.get("/objects", response_model=Page[TwitchData])
def objects(db: Session = Depends(get_db), params: Params = Depends()):
    """
    Return all objects from database
    """
    return paginate(get_objects(db), params)


@router.get("/object", response_model=Page[TwitchData])
def filter_objects(
        entry: TwitchDataOptional = Depends(),
        db: Session = Depends(get_db),
        params: Params = Depends(),
):
    """
    Return objects filtered by the given parameters
    """
    return paginate(get_objects_by_filters(db, entry), params)


@router.put("/object")
def insert_object(entry: TwitchDataCreate, db: Session = Depends(get_db)):
    pass
