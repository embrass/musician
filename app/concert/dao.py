from app.concert.concert import Concert
from app.dao.base import BaseDAO

class ConcertDAO(BaseDAO):
    model = Concert
