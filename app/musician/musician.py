from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Musician(Base):
    __tablename__ = "musician"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)


    musician = relationship("concert", back_populates="musician")





