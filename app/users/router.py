from fastapi import APIRouter, HTTPException, status, Response, Request
from app.users.auth import get_password_hash
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth
from app.users.auth import auth_user
from app.users.auth import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await auth_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHRIZED)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("access_token", access_token)
    return {"access_token": access_token}

