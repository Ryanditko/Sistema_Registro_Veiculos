import os
from logging.config import fileConfig

from dotenv import load_dotenv
from sqlalchemy import create_engine, engine_from_config, pool

from alembic import context
from modelos.base import Base
from modelos.tb_proprietario import Proprietario
from modelos.tb_veiculo_registrado import VeiculoRegistrado
from modelos.tb_banco import Banco
from modelos.tb_empresa import Empresa
from modelos.tb_pessoa import Pessoa
from modelos.tb_caminhao import Caminhao
from modelos.tb_carro import Carro
from modelos.tb_dono import Dono

load_dotenv()
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.Base.metadata
target_metadata = Proprietario.Base.metadata
target_metadata = VeiculoRegistrado.Base.metadata
target_metadata = Banco.Base.metadata
target_metadata = Empresa.Base.metadata
target_metadata = Pessoa.Base.metadata
target_metadata = Caminhao.Base.metadata
target_metadata = Carro.Base.metadata
target_metadata = Dono.Base.metadata


def run_migrations_offline():
    usuario = os.getenv("USUARIO")
    senha = os.getenv("SENHA")
    host = os.getenv("HOST")
    banco_de_dados = os.getenv("BANCO_DE_DADOS")
    url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    usuario = os.getenv("USUARIO")
    senha = os.getenv("SENHA")
    host = os.getenv("HOST")
    banco_de_dados = os.getenv("BANCO_DE_DADOS")
    url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()