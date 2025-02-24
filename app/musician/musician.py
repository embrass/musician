from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Musician(Base):
    __tablename__ = "musician"

    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String, nullable=False)
    concert_id = Column(ForeignKey("concert.id"))
    musician = relationship("Concert", back_populates="musician")





