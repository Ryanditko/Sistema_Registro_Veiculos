import pandas as pd
import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, DataError
from datetime import datetime
import traceback

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
    Classe responsável pelo tratamento de exceções do processo ETL.
    Define decoradores específicos para cada etapa: extração, transformação e carregamento.
    """

    @staticmethod
    def handle_extraction_error(func):
        """
        Tratamento de exceções na EXTRAÇÃO.
        Exceções tratadas:
        - FileNotFoundError: Arquivo não encontrado.
        - EmptyDataError: Arquivo vazio.
        - ValueError: Problemas na leitura.
        - Exception: Qualquer outro erro.
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
                logger.error(f"[EXTRACTION ERROR] Erro na leitura dos dados: {e}")
                logger.error(traceback.format_exc())
                raise
            except Exception as e:
                logger.error(f"[EXTRACTION ERROR] Erro inesperado: {e}")
                logger.error(traceback.format_exc())
                raise
        return wrapper

    @staticmethod
    def handle_transformation_error(func):
        """
        Tratamento de exceções na TRANSFORMAÇÃO.
        Exceções tratadas:
        - KeyError: Coluna não encontrada.
        - ValueError: Erro de conversão de tipo.
        - TypeError: Operações inválidas.
        - Exception: Qualquer outro erro.
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
            except TypeError as e:
                logger.error(f"[TRANSFORMATION ERROR] Erro de tipo: {e}")
                logger.error(traceback.format_exc())
                raise
            except Exception as e:
                logger.error(f"[TRANSFORMATION ERROR] Erro inesperado: {e}")
                logger.error(traceback.format_exc())
                raise
        return wrapper

    @staticmethod
    def handle_loading_error(func):
        """
        Tratamento de exceções no CARREGAMENTO.
        Exceções tratadas:
        - IntegrityError: Violação de integridade.
        - OperationalError: Problemas de conexão.
        - DataError: Dados inválidos.
        - SQLAlchemyError: Erros gerais do SQLAlchemy.
        - Exception: Qualquer outro erro.
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except IntegrityError as e:
                logger.error(f"[LOADING ERROR] Violação de integridade: {e}")
                logger.error(traceback.format_exc())
                raise
            except OperationalError as e:
                logger.error(f"[LOADING ERROR] Erro operacional: {e}")
                logger.error(traceback.format_exc())
                raise
            except DataError as e:
                logger.error(f"[LOADING ERROR] Erro de dados: {e}")
                logger.error(traceback.format_exc())
                raise
            except SQLAlchemyError as e:
                logger.error(f"[LOADING ERROR] Erro SQLAlchemy: {e}")
                logger.error(traceback.format_exc())
                raise
            except Exception as e:
                logger.error(f"[LOADING ERROR] Erro inesperado: {e}")
                logger.error(traceback.format_exc())
                raise
        return wrapper