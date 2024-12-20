from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define a pasta para upload de arquivos
IMAGES_FOLDER = '/app/static/files/img'

SECRECT_KEY = '###$$$@@@'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123@localhost:5432/bug_shop'


# Conexão com o banco de dados
class DBConnection:

    def __init__(self) -> None:
        self.__connection_string = SQLALCHEMY_DATABASE_URI
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string, pool_size=50)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        self.__engine.dispose()

