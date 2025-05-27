from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base

class Banco(Base.Base, Base):
    __tablename__ = 'banco'

    bnome = Column(String(100), primary_key=True)
    bendereco = Column(String)
    id_proprietario = Column(Integer, ForeignKey('proprietario.id_proprietario'))

    proprietario = relationship('Proprietario', back_populates='bancos')