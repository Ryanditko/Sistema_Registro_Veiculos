# %%
# imports
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelos.user import User

load_dotenv()

# %%
# conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")
url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"


engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

# %%
# gerando dados de exemplo
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "email": [
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com",
        "david@example.com",
        "eve@example.com",
    ],
}

df = pd.DataFrame(data)
# %%
# gerando objetos da classe User a partir do DataFrame
registros = User.from_dataframe(df)

# %%
# incluindo registros no banco de dados
session.add_all(registros)
session.commit()

# %%
