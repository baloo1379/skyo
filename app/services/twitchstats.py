from sqlalchemy.orm import Session

from app.repositories.twitchdata_repository import get_objects
from app.schemas.twitchstats import Bar, Chart


def histogram(values: list[int]) -> list[Bar]:
    values.sort()
    mn = min(values)
    mx = max(values)
    step = int((mx - mn) / 10)
    result = list()
    for i in range(mn, mx, step):
        bar = Bar(name=f"({i},{i + step - 1})", value=0)
        for v in values:
            if i < v < i + step - 1:
                bar.value += 1
        result.append(bar)
    return result


def pie(values: list[bool]) -> list[Bar]:
    bar1 = Bar(name="true", value=values.count(True))
    bar2 = Bar(name="false", value=values.count(False))
    return list([bar1, bar2])


def chart_factory(title: str, values: list):
    if type(values[0]) is int:
        return Chart(title=title, bars=histogram(values))
    elif type(values[0]) is bool:
        return Chart(title=title, bars=pie(values))


def get_stats(db: Session) -> list[Chart]:
    objects = get_objects(db)
    return [
        chart_factory("Watch Time", [row.watch_time for row in objects]),
        chart_factory("Stream Time", [row.stream_time for row in objects]),
        chart_factory("Peak Viewers", [row.peak_viewers for row in objects]),
        chart_factory("Average Viewers", [row.average_viewers for row in objects]),
        chart_factory("Followers", [row.followers for row in objects]),
        chart_factory("Followers Gained", [row.followers_gained for row in objects]),
        chart_factory("Views Gained", [row.views_gained for row in objects]),
        chart_factory("Partnered", [row.partnered for row in objects]),
        chart_factory("Mature", [row.mature for row in objects])
    ]