from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base


class Pessoa(Base.Base, Base):
    __tablename__ = 'pessoa'

    cpf = Column(String(14), primary_key=True)
    num_carteira_motorista = Column(String)
    nome = Column(String)
    endereco = Column(String)
    id_proprietario = Column(Integer, ForeignKey('proprietario.id_proprietario'))

    proprietario = relationship('Proprietario', back_populates='pessoas')