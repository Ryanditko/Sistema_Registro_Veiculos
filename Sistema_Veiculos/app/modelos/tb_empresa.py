from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base


class Empresa(Base.Base, Base):
    __tablename__ = 'empresa'

    enome = Column(String(100), primary_key=True)
    eendereco = Column(String)
    id_proprietario = Column(Integer, ForeignKey('proprietario.id_proprietario'))

    proprietario = relationship('Proprietario', back_populates='empresas')