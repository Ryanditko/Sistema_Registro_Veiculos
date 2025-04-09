from tbveiculo_registrado import Veiculo_Registrado

from sqlalchemy import Column, Integer, String, ForeignKey

from modelos import Base

class Caminhao(Base.Base, Base):
    _tablename_ = "caminhao"
    cod_veiculo = Column(Integer, ForeignKey('veiculo_registrado.cod_veiculo'), primary_key=True)
    marca_caminhao = Column(String)
    modelo_caminhao = Column(String)
    ano_caminhao = Column(Integer)