from sqlalchemy import Column, String, Integer, Float, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from modelos.base import Base

class Caminhao(Base.Base, Base):
    __tablename__ = 'caminhao'

    cod_veiculo = Column(BigInteger, ForeignKey('veiculo_registrado.cod_veiculo'), primary_key=True)
    marca_caminhao = Column(String)
    modelo_caminhao = Column(String)
    capacidade_peso = Column(Float)
    ano_caminhao = Column(Integer)

    veiculo = relationship('VeiculoRegistrado', back_populates='caminhao')