from pydantic import BaseModel
from datetime import date


class SchemasConcert(BaseModel):
    id: int
    concert_id: int
    name: str
    locations: str
    date_to: date
    cost: int

    class Config:
        from_attributes = True