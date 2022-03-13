from pydantic import BaseModel


class Bar(BaseModel):
    name: str
    value: int


class Chart(BaseModel):
    title: str
    bars: list[Bar]
