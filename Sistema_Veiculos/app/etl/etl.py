import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.etl.abstract_etl import AbstractETL
from app.tests.etl_exceptions import ETLExceptionHandler
from app.modelos.tb_proprietario import Proprietario
from app.modelos.tb_veiculo_registrado import VeiculoRegistrado
from app.modelos.tb_banco import Banco
from app.modelos.tb_empresa import Empresa
from app.modelos.tb_pessoa import Pessoa
from app.modelos.tb_caminhao import Caminhao
from app.modelos.tb_carro import Carro
from app.modelos.tb_dono import Dono


class ETL(AbstractETL):
    def __init__(self, origem, destino):
        super().__init__(origem, destino)
        self.engine = create_engine(destino)
        self.Session = sessionmaker(bind=self.engine)
        self.dataframes = {}

    @ETLExceptionHandler.handle_extraction_error
    def extract(self):
        self.dataframes = pd.read_excel(self.origem, sheet_name=None)

    @ETLExceptionHandler.handle_transformation_error
    def transform(self):
        df = self.dataframes['Banco']
        df['id_proprietario'] = pd.to_numeric(df['id_proprietario'], errors='coerce').astype('Int64')
        self.dataframes['Banco'] = df

        df = self.dataframes['Caminhão']
        df['cod_veiculo'] = pd.to_numeric(df['cod_veiculo'], errors='coerce').astype('Int64')
        self.dataframes['Caminhão'] = df

        df = self.dataframes['Carro']
        df['cod_carro'] = pd.to_numeric(df['cod_veiculo'], errors='coerce').astype('Int64')
        self.dataframes['Carro'] = df

        df = self.dataframes['Dono']
        df['id_proprietario'] = pd.to_numeric(df['id_proprietario'], errors='coerce').astype('Int64')
        df['cod_veiculo'] = pd.to_numeric(df['cod_veiculo'], errors='coerce').astype('Int64')
        df['data_compra'] = pd.to_datetime(df['data_compra']).dt.date
        self.dataframes['Dono'] = df

        df = self.dataframes['Empresa']
        df['id_proprietario'] = pd.to_numeric(df['id_proprietario'], errors='coerce').astype('Int64')
        self.dataframes['Empresa'] = df

        df = self.dataframes['Pessoa']
        df['id_proprietario'] = pd.to_numeric(df['id_proprietario'], errors='coerce').astype('Int64')
        self.dataframes['Pessoa'] = df

        df = self.dataframes['Proprietário']
        df['id_proprietario'] = pd.to_numeric(df['id_proprietario'], errors='coerce').astype('Int64')
        self.dataframes['Proprietário'] = df

        df = self.dataframes['Veículo_Registrado']
        df['cod_veiculo'] = pd.to_numeric(df['cod_veiculo'], errors='coerce').astype('Int64')
        self.dataframes['Veículo_Registrado'] = df

    @ETLExceptionHandler.handle_loading_error
    def load(self):
        session = self.Session()
        try:
            # Proprietário
            lista_proprietario = []
            lista_proprietario.extend(Proprietario.from_dataframe(self.dataframes['Proprietário']))
            session.add_all(lista_proprietario)
            session.commit()

            # Veiculo registrado
            lista_veiculo_registrado = []
            lista_veiculo_registrado.extend(VeiculoRegistrado.from_dataframe(self.dataframes['Veículo_Registrado']))
            session.add_all(lista_veiculo_registrado)
            session.commit()

            # Banco
            lista_banco = []
            lista_banco.extend(Banco.from_dataframe(self.dataframes['Banco']))
            session.add_all(lista_banco)
            session.commit()

            # Empresa
            lista_empresa = []
            lista_empresa.extend(Empresa.from_dataframe(self.dataframes['Empresa']))
            session.add_all(lista_empresa)
            session.commit()

            # Pessoa
            lista_pessoa = []
            lista_pessoa.extend(Pessoa.from_dataframe(self.dataframes['Pessoa']))
            session.add_all(lista_pessoa)
            session.commit()

            # Caminhão      
            lista_caminhao = []
            lista_caminhao.extend(Caminhao.from_dataframe(self.dataframes['Caminhão']))
            session.add_all(lista_caminhao)
            session.commit()

            # Carro
            lista_carro = []
            lista_carro.extend(Carro.from_dataframe(self.dataframes['Carro']))
            session.add_all(lista_carro)
            session.commit()

            # Dono
            lista_dono = []
            lista_dono.extend(Dono.from_dataframe(self.dataframes['Dono']))
            session.add_all(lista_dono)
            session.commit()

            print("Dados carregados com sucesso.")
        except SQLAlchemyError as e:
            session.rollback()
            raise
        finally:
            session.close()