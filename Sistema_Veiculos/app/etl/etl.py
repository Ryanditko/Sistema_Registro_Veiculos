import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from etl.abstract_etl import AbstractETL
from tests.exceptions import ETLExceptionHandler
from modelos.tb_proprietario import Proprietario
from modelos.tb_veiculo_registrado import VeiculoRegistrado
from modelos.tb_banco import Banco
from modelos.tb_empresa import Empresa
from modelos.tb_pessoa import Pessoa
from modelos.tb_caminhao import Caminhao
from modelos.tb_carro import Carro
from modelos.tb_dono import Dono


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
            for _, row in self.dataframes['Proprietário'].iterrows():
                obj = Proprietario(id_proprietario=int(row['id_proprietario']))
                session.add(obj)
            session.commit()

            for _, row in self.dataframes['Veículo_Registrado'].iterrows():
                obj = VeiculoRegistrado(cod_veiculo=int(row['cod_veiculo']), placa=row['placa'])
                session.add(obj)
            session.commit()

            for _, row in self.dataframes['Banco'].iterrows():
                obj = Banco(
                    bnome=row['bnome'],
                    bendereco=row['bendereco'],
                    id_proprietario=row['id_proprietario'] if pd.notna(row['id_proprietario']) else None
                )
                session.add(obj)
            session.commit()

            for _, row in self.dataframes['Empresa'].iterrows():
                obj = Empresa(
                    enome=row['enome'],
                    eendereco=row['eendereco'],
                    id_proprietario=row['id_proprietario'] if pd.notna(row['id_proprietario']) else None
                )
                session.add(obj)
            session.commit()

            for _, row in self.dataframes['Pessoa'].iterrows():
                obj = Pessoa(
                    cpf=row['cpf'],
                    num_carteira_motorista=row['num_carteira_motorista'],
                    nome=row['nome'],
                    endereco=row['endereco'],
                    id_proprietario=row['id_proprietario'] if pd.notna(row['id_proprietario']) else None
                )
                session.add(obj)
            session.commit()

            for _, row in self.dataframes['Caminhão'].iterrows():
                obj = Caminhao(
                    cod_veiculo=row['cod_veiculo'],
                    marca_caminhao=row['marca_caminhao'],
                    modelo_caminhao=row['modelo_caminhao'],
                    capacidade_peso=row['capacidade_peso'],
                    ano_caminhao=row['ano_caminhao']
                )
                session.add(obj)
            session.commit()

            for _, row in self.dataframes['Carro'].iterrows():
                obj = Carro(
                    cod_veiculo=row['cod_veiculo'],
                    estilo=row['estilo'],
                    marca_carro=row['marca_carro'],
                    modelo_carro=row['modelo_carro'],
                    ano_carro=row['ano_carro']
                )
                session.add(obj)
            session.commit()

            for _, row in self.dataframes['Dono'].iterrows():
                obj = Dono(
                    id_proprietario=row['id_proprietario'],
                    cod_veiculo=row['cod_veiculo'],
                    data_compra=row['data_compra'],
                    alienado_ou_regular=row['alienado_ou_regular']
                )
                session.add(obj)
            session.commit()

            print("Dados carregados com sucesso.")
        except SQLAlchemyError as e:
            session.rollback()
            raise
        finally:
            session.close()