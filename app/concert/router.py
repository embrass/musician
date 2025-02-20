from fastapi import APIRouter

from app.concert.dao import ConcertDAO

router = APIRouter(
    prefix="/concert",
    tags=["Концерты"]
)


@router.get("")
async def get_id():
    return await ConcertDAO.find_by_id(1)
