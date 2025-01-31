from fastapi import APIRouter
from app.users.schemas import *



router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_user(user_data: SUser):
    pass