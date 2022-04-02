from app.database.connection import engine
from app.models.twitchdata import TwitchData
import pandas as pd


def insert(file) -> dict:
    table_name = TwitchData.__tablename__

    df = pd.read_csv(
        file,
        header=0,
        names=["channel", "watch_time", "stream_time", "peak_viewers", "average_viewers", "followers", "followers_gained", "views_gained", "partnered", "mature", "language"]
    )
    df.to_sql(table_name, engine, index=False, if_exists='append')
    rows: int = engine.execute(f"SELECT COUNT(*) FROM {table_name}").scalar_one()
    return {"message": f"Data inserted. Rows affected: {rows}"}
