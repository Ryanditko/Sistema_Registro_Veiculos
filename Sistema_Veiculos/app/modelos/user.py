from sqlalchemy import Column, Integer, String

from modelos.base import Base


class User(Base.Base, Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String(50), unique=True)
