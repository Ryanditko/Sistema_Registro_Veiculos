import datetime 

class Dono:
    def __init__(self, id_proprietario:int, cod_veiculo:int, data_compra:str, alienado_ou_regular:str):
        self.id_proprietario = id_proprietario
        self.cod_veiculo = cod_veiculo
        self.data_compra = data_compra
        self.alienado_ou_regular = alienado_ou_regular
