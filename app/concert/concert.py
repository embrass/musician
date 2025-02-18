from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Concert(Base):
    __tablename__ = "concert"

    id = Column(Integer, primary_key=True)
    concert_id = Column(ForeignKey("musician.id"))
    name = Column(String, nullable=False)
    locations = Column(String, nullable=False)
    date_to = Column(Date, nullable=False)
    cost = Column(Integer, nullable=False)

    concert = relationship("Musician", back_populates="concert")



