from app.backend.db import async_session_maker

from sqlalchemy import select

from app.concert.concert import Concert
from app.dao.base import BaseDAO

class ConcertDAO(BaseDAO):
    model = Concert
