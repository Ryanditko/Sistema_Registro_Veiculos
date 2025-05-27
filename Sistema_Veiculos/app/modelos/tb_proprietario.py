from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from modelos.base import Base


class Proprietario(Base.Base, Base):
    __tablename__ = 'proprietario'

    id_proprietario = Column(Integer, primary_key=True)

    bancos = relationship('Banco', back_populates='proprietario')
    empresas = relationship('Empresa', back_populates='proprietario')
    pessoas = relationship('Pessoa', back_populates='proprietario')
    donos = relationship('Dono', back_populates='proprietario')