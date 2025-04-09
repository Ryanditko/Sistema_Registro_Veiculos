from tbproprietario import Proprietario

from sqlalchemy import Column, Integer, String, ForeignKey

from modelos import Base

class Empresa(Base.Base, Base):
    _tablename_ = "empresa"
    enome = Column(String, primary_key=True)
    eendereco = Column(String)
    id_proprietario = Column(Integer, ForeignKey('proprietario.id_proprietario'))