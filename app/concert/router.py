from fastapi import APIRouter
from app.concert.schemas import SchemasConcert
from app.concert.dao import ConcertDAO

router = APIRouter(
    prefix="/concert",
    tags=["Concert"]
)


@router.get("")
async def get_id() -> list[SchemasConcert]:
    return await ConcertDAO.find_all()
