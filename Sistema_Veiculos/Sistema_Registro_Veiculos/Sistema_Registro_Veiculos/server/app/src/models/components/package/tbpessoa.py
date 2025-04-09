from tbproprietario import Proprietario

from sqlalchemy import Column, Integer, String, ForeignKey

from modelos import Base

class Pessoa(Base.Base, Base):
    _tablename_ = "pessoa"
    cpf = Column(String, primary_key=True)
    num_carteira_motorista = Column(Integer, nullable=False)
    nome = Column(String, nullable=False)
    endereco = Column(String)
    id_proprietario = Column(Integer, ForeignKey('proprietario.id_proprietario'))
    
