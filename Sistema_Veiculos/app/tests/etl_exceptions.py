# %%
# Definindo os tratamentos de exceções para os testes

import pandas as pd
import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, DataError
from datetime import datetime
import traceback
import json
import os
# %%
# Configurando o logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl_errors.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ETL')

class ETLExceptionHandler:
    """
    Classe responsável por gerenciar o tratamento de exceções do processo ETL.
    Implementa decoradores para cada etapa do processo (Extração, Transformação e Carregamento).
    """

    @staticmethod
    def handle_extraction_error(func):
        """
        Decorador para tratamento de exceções na etapa de extração de dados.
        
        Trata as seguintes exceções:
        - FileNotFoundError: Quando o arquivo fonte não é encontrado
        - EmptyDataError: Quando o arquivo está vazio ou não contém dados
        - ValueError: Quando há erro na leitura ou conversão dos dados
        - PermissionError: Quando não há permissão para acessar o arquivo
        - json.JSONDecodeError: Quando há erro na leitura de arquivos JSON
        - Exception: Para erros não previstos
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except FileNotFoundError as e:
                logger.error(f"[EXTRACTION ERROR] Arquivo não encontrado: {e}")
                logger.error(traceback.format_exc())
                raise
            except pd.errors.EmptyDataError as e:
                logger.error(f"[EXTRACTION ERROR] Arquivo vazio ou sem dados: {e}")
                logger.error(traceback.format_exc())
                raise
            except ValueError as e:
                logger.error(f"[EXTRACTION ERROR] Erro de leitura ou conversão de dados: {e}")
                logger.error(traceback.format_exc())
                raise
            except PermissionError as e:
                logger.error(f"[EXTRACTION ERROR] Erro de permissão ao acessar arquivo: {e}")
                logger.error(traceback.format_exc())
                raise
            except json.JSONDecodeError as e:
                logger.error(f"[EXTRACTION ERROR] Erro ao decodificar JSON: {e}")
                logger.error(traceback.format_exc())
                raise
            except Exception as e:
                logger.error(f"[EXTRACTION ERROR] Erro inesperado: {e}")
                logger.error(traceback.format_exc())
                raise
        return wrapper
# %%
    @staticmethod
    def handle_transformation_error(func):
        """
        Decorador para tratamento de exceções na etapa de transformação de dados.
        
        Trata as seguintes exceções:
        - KeyError: Quando uma coluna necessária não existe no DataFrame
        - ValueError: Quando há erro na conversão de tipos de dados
        - ParserError: Quando há erro no parsing dos dados
        - DtypeWarning: Avisos sobre incompatibilidade de tipos de dados
        - TypeError: Quando há erro de tipo na operação
        - AttributeError: Quando há erro ao acessar atributo
        - Exception: Para erros não previstos
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError as e:
                logger.error(f"[TRANSFORMATION ERROR] Coluna ausente no DataFrame: {e}")
                logger.error(traceback.format_exc())
                raise
            except ValueError as e:
                logger.error(f"[TRANSFORMATION ERROR] Erro de conversão de tipo: {e}")
                logger.error(traceback.format_exc())
                raise
            except pd.errors.ParserError as e:
                logger.error(f"[TRANSFORMATION ERROR] Erro ao fazer parse dos dados: {e}")
                logger.error(traceback.format_exc())
                raise
            except pd.errors.DtypeWarning as e:
                logger.warning(f"[TRANSFORMATION WARNING] Aviso sobre tipo de dados: {e}")
                return func(*args, **kwargs)
            except TypeError as e:
                logger.error(f"[TRANSFORMATION ERROR] Erro de tipo na operação: {e}")
                logger.error(traceback.format_exc())
                raise
            except AttributeError as e:
                logger.error(f"[TRANSFORMATION ERROR] Erro ao acessar atributo: {e}")
                logger.error(traceback.format_exc())
                raise
            except Exception as e:
                logger.error(f"[TRANSFORMATION ERROR] Erro inesperado: {e}")
                logger.error(traceback.format_exc())
                raise
        return wrapper
# %%
    @staticmethod
    def handle_loading_error(func):
        """
        Decorador para tratamento de exceções na etapa de carregamento de dados.
        
        Trata as seguintes exceções:
        - IntegrityError: Quando há violação de restrições de integridade do banco
        - OperationalError: Quando há problemas na conexão com o banco
        - DataError: Quando há erro nos dados sendo inseridos
        - SQLAlchemyError: Para erros gerais do SQLAlchemy
        - TimeoutError: Quando há timeout na conexão
        - ConnectionError: Quando há erro de conexão
        - Exception: Para erros não previstos
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except IntegrityError as e:
                logger.error(f"[LOADING ERROR] Violação de integridade: {e}")
                logger.error(traceback.format_exc())
                raise
            except OperationalError as e:
                logger.error(f"[LOADING ERROR] Erro operacional na conexão com o banco: {e}")
                logger.error(traceback.format_exc())
                raise
            except DataError as e:
                logger.error(f"[LOADING ERROR] Erro de dados: {e}")
                logger.error(traceback.format_exc())
                raise
            except SQLAlchemyError as e:
                logger.error(f"[LOADING ERROR] Erro do SQLAlchemy: {e}")
                logger.error(traceback.format_exc())
                raise
            except TimeoutError as e:
                logger.error(f"[LOADING ERROR] Timeout na conexão com o banco: {e}")
                logger.error(traceback.format_exc())
                raise
            except ConnectionError as e:
                logger.error(f"[LOADING ERROR] Erro de conexão com o banco: {e}")
                logger.error(traceback.format_exc())
                raise
            except Exception as e:
                logger.error(f"[LOADING ERROR] Erro inesperado: {e}")
                logger.error(traceback.format_exc())
                raise
        return wrapper

