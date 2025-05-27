# %%
# imports
import os
import logging
from dotenv import load_dotenv
from tests.exceptions import ETLExceptionHandler
from etl.etl import ETL

load_dotenv()

# %%
# conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

# %%
# testando o ETL
origem = "dados.xlsx"
destino = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

try:
    etl = ETL(origem, destino)
    etl.extract()
    etl.transform()
    etl.load()
except Exception as e:
    logging.error(f"Erro durante o processo ETL: {e}")
    raise