
from app.backend.db import async_session_maker

from sqlalchemy import select, insert




class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as sc:
            query = select(cls.model).filter_by(id=model_id)
            result = await sc.execute(query)
            return result.scalar_one_or_none()




    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as sc:
            query = select(cls.model)
            concert = await sc.execute(query)
            return concert.scalars().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as sc:
            query = insert(cls.model).values(**data)
            await sc.execute(query)
            await sc.commit()