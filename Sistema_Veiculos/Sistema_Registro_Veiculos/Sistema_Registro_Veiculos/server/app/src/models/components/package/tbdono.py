from tbproprietario import Proprietario

from tbveiculo_registrado import Veiculo_Registrado

from sqlalchemy import Column, Integer, String, ForeignKey, Date, PrimaryKeyConstraint

from modelos import Base

class Dono(Base.Base, Base):
    _tablename_ = "dono"
    id_proprietario = Column(Integer, ForeignKey('proprietario.id_proprietario'), nullable=False)
    cod_veiculo = Column(Integer, ForeignKey('veiculo_registrado.cod_veiculo'), nullable=False)
    data_compra = Column(Date)
    alienado_ou_regular = Column(String)

    _table_args_ = (
        PrimaryKeyConstraint('id_proprietario', 'cod_veiculo')
    )