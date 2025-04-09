from tbproprietario import Proprietario

from sqlalchemy import Column, Integer, String, ForeignKey

from modelos import Base

class Banco(Base.Base, Base):
    _tablename_ = "banco"
    bnome = Column(String, primary_key=True)
    bendereco = Column(String)
    id_proprietario = Column(Integer, ForeignKey('proprietario.id_proprietario'))