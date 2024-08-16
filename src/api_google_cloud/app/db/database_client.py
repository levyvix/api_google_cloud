import os

from sqlalchemy import MetaData, create_engine


class DatabaseClient:
    def __init__(self) -> None:
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.metadate = MetaData()
        self.engine = create_engine(f"postgresql://postgres:postgres@{self.db_host}:5432/postgres")
