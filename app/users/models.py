from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    #booking = relationship("Bookings", back_populates="user")


