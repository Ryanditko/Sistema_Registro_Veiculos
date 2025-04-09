from sqlalchemy import Column, Integer, String

from modelos import Base

class Veiculo_Registrado(Base.Base, Base):
    _tablename_ = "veiculo_registrado"
    cod_veiculo = Column(Integer, primary_key=True)
    placa = Column(String, nullable=False)
