### Descrição
Neste repositório armazenamos o projeto de mapeamento objeto-relacional para gerenciamento de migrações e interação com banco de dados.

1. Interação com o banco de dados
Para utilizar as classes correspondentes às tabelas do banco, basta importá-las: `from modelos import *`
As formas de interagir com o banco de dados por meio das classes são descritas na [documentação](https://docs.sqlalchemy.org/en/20/orm/) do SQLAlchemy ORM.

2. Migração do banco de dados
Para realizar uma alteração no banco de dados, deve-se alterar diretamente as classes correspondentes às tabelas. Após realizar uma alteração, para fazer a migração do banco, deve-se adotar os seguintes passos:
    - Definir as credenciais de conexão com o banco no arquivo `.env`
        ```
        USUARIO=<usuario>
        SENHA=<senha>
        HOST=<host>
        BANCO_DE_DADOS=<banco de dados>
        ```
    - Deletar o conteúdo da tabela `alembic_version` no banco de dados e qualquer arquivo presente em `alembic\versions`
    - Executar o comando `python -m alembic revision --autogenerate`
    - Checar o arquivo de migração `.py` gerado automaticamente na pasta `alembic\versions`
    - Executar o comando `python -m alembic upgrade head`

### Autores
- [Vitor Furlan de Oliveira](mailto:vitor.foliveira@faculdadeimpacta.com.br)