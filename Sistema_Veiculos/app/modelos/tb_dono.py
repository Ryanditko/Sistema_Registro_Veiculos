from sqlalchemy import Column, String, Integer,BigInteger, Date, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from modelos.base import Base


class Dono(Base.Base, Base):
    __tablename__ = 'dono'

    id_proprietario = Column(Integer, ForeignKey('proprietario.id_proprietario'))
    cod_veiculo = Column(BigInteger, ForeignKey('veiculo_registrado.cod_veiculo'))
    data_compra = Column(Date)
    alienado_ou_regular = Column(String)

    __table_args__ = (
        PrimaryKeyConstraint('id_proprietario', 'cod_veiculo'),
    )

    proprietario = relationship('Proprietario', back_populates='donos')
    veiculo = relationship('VeiculoRegistrado', back_populates='donos')