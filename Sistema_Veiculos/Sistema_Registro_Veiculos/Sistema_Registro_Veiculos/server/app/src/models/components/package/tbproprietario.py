from sqlalchemy import Column, Integer, String

from modelos import Base

class Proprietario(Base.Base, Base):
    _tablename_ = "proprietario.id_proprietario" 
    id_proprietario = Column(Integer, primary_key=True)
    