from tbveiculo_registrado import Veiculo_Registrado

from sqlalchemy import Column, Integer, String, ForeignKey

from modelos import Base

class Carro(Base.Base, Base):
    _tablename_ = "carro"
    cod_veiculo = Column(Integer, ForeignKey('veiculo_registrado.cod_veiculo'), primary_key=True)
    estilo = Column(String)
    marca_carro = Column(String)
    modelo_carro = Column(String)
    ano_carro = Column(Integer)