# Buscando as classes dentro de seus arquivos
from pessoa import Pessoa
from banco import Banco
from empresa import Empresa 
# Chamando as superclasses 
class Proprietario(Pessoa, Banco, Empresa):
    def __init__(self,id_proprietario:int):
        self.id_proprietario = id_proprietario
        Pessoa.__init__(self)
        Banco.__init__(self)
        Empresa.__init__(self)