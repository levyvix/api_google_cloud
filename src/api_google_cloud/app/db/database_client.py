from sqlalchemy import MetaData, create_engine
import os


class DatabaseClient:

    def __init__(self) -> None:
        self.db_host = os.getenv('DB_HOST', 'host.docker.internal')
        self.metadate = MetaData()
        self.engine = engine = create_engine(
            f'postgresql://postgres:postgres@{self.db_host}:5432/postgres')
