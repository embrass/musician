from fastapi import APIRouter

router = APIRouter(
    prefix="/concert",
    tags=["Концерты"]
)


@router.get("/{name}/{city}/{stage}")
def get_id(name: str, city: str, stage: str):
    return [
        {"Выступает": name},
        {"В этом городе": city},
        {"На площадке": stage},
    ]


@router.get("/all")
async def get_all_concert(

):
    pass