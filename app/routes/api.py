from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
from database.connection import engine
from sqlalchemy import insert, MetaData, Column, Table, String, Integer, Boolean, inspect
import pandas as pd


router = APIRouter(prefix="/api/v1")


@router.get('/')
def health():
    """
    Simple checks the server status
    """
    return {"health": "ok"}


@router.post("/{table_name}/csv")
async def upload_csv(table_name, data: UploadFile = File(...)):
    meta = MetaData()
    meta.create_all(engine)
    pd.read_csv(data.file, header=1).to_sql(table_name, engine, if_exists='replace')
    return {"message": "Data inserted"}
