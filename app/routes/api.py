from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.repositories.twitchdata_repository import get_objects
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


@router.get("/objects")
def objects(db: Session = Depends(get_db)):
    """
    Return all objects from database
    """
    return get_objects(db)
