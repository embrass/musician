#uvicorn app.main:app --reload
from app.musician.router import router as musicians
from app.concert.router import router as concert
from app.pages.router import router as concerts
from app.image.router import router as images
from app.users.router import router as users
from fastapi import FastAPI

app = FastAPI()


app.include_router(users)
app.include_router(musicians)
app.include_router(musicians)
app.include_router(images)
app.include_router(concert)
app.include_router(concerts)

