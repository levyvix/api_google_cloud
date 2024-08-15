from sqlalchemy import create_engine, MetaData, Table, Column, String, Date


def get_engine():
    engine = create_engine(
        'postgresql://postgres:postgres@localhost:5432/postgres')

    return engine
