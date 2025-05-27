from abc import ABC, abstractmethod

class AbstractETL(ABC):
    def __init__(self, origem: str, destino: str):
        self.origem = origem
        self.destino = destino
        self._dados_extraidos = None
        self._dados_transformados = None

    @abstractmethod
    def extract(self):
        # TODO: lê os dados a serem inseridos a partir do caminho do arquivo (origem)
        pass

    @abstractmethod
    def transform(self):
        # TODO: transforma os dados extraídos em um formato mais adequado para inserção
        pass

    @abstractmethod
    def load(self):
        # TODO: cria uma engine a partir do destino (destino) e insere os dados transformados
        pass