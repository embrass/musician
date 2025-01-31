from fastapi import APIRouter, Request, Depends

from fastapi.templating import Jinja2Templates



router = APIRouter(
    tags=["Frontend"],
    prefix="/pages"
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/concert")
async def get_concert(
        request: Request,
        concert=Depends()
):
    return templates.TemplateResponse(name="concert.html", context={"request": request})


#get_hotels_by_location_and_time