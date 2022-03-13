from pydantic import BaseModel


class Bar(BaseModel):
    label: str
    value: int


class Chart(BaseModel):
    title: str
    bars: list[Bar]
