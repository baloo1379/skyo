from fastapi import FastAPI

from app.database.connection import engine
from app.models.twitchdata import Base
from app.routes.api import router as api_router

app = FastAPI(
    title='Top Streamers on Twitch',
    description='This contains data of Top 1000 Streamers from 2019.',
    version='1.0.0'
)


def prepare_routes():
    app.include_router(api_router)


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    prepare_routes()
