from fastapi import APIRouter

router = APIRouter(
    prefix="/musician",
    tags=["Musician"]
)


@router.get("/{name},{city}")
def get_id(name: str, city: str):
    return [
        {"Музыкан": name},
        {"Выступает": city}
    ]


