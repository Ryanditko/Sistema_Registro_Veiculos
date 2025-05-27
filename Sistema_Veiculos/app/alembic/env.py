import os
import sys
from logging.config import fileConfig

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

from modelos.base import Base
from modelos.tb_banco import Banco
from modelos.tb_caminhao import Caminhao
from modelos.tb_carro import Carro
from modelos.tb_dono import Dono
from modelos.tb_empresa import Empresa
from modelos.tb_pessoa import Pessoa
from modelos.tb_proprietario import Proprietario
from modelos.tb_veiculo_registrado import VeiculoRegistrado

load_dotenv()

from sqlalchemy import create_engine, engine_from_config, pool

from alembic import context

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.Base.metadata
target_metadata = Banco.Base.metadata
target_metadata = Caminhao.Base.metadata
target_metadata = Carro.Base.metadata
target_metadata = Dono.Base.metadata
target_metadata = Empresa.Base.metadata
target_metadata = Pessoa.Base.metadata
target_metadata = Proprietario.Base.metadata
target_metadata = VeiculoRegistrado.Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """

    usuario = os.getenv("USUARIO")
    senha = os.getenv("SENHA")
    host = os.getenv("HOST")
    banco_de_dados = os.getenv("BANCO_DE_DADOS")
    url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

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