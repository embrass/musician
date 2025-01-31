from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(
    prefix="/images",
    tags=["Картинки"]
)

@router.post("/concert")
async def add_concert_pictures(name: int, file: UploadFile):
    with open("app/static/images/4.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

users_db = {
    1: {"Alice": "Frank", "12": "hehe"},
    2: {"Mike": "Trump", "19": "ahahaha"},

}


@router.get("/user/{id_user}")
def get_id(id_user: int):
    user = users_db.get(id_user)
    return user