from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Concert(Base):
    __tablename__ = "concert"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    locations = Column(String, nullable=False)
    date_to = Column(Date, nullable=False)
    cost = Column(Integer, nullable=False)

    concert = relationship("Concert", back_populates="musician")

