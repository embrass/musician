# uvicorn app.main:feedback.app --reload port 8001
# uvicorn app.main:app --reload
#uvicorn app.main:app --reload
from app.musician.router import router as musicians
from app.concert.router import router as concert
from app.pages.router import router as concerts
from app.image.router import router as images
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(musicians)
app.include_router(musicians)
app.include_router(images)
app.include_router(concert)
app.include_router(concerts)


