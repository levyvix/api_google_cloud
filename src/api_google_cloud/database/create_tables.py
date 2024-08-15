from sqlalchemy import MetaData, Table, Column, String, Date
from db import get_engine


class CustomersTable:
    def __init__(self):
        self.engine = get_engine()

        self.metadata = MetaData()

        self.customers_table = Table(
            "customers",
            self.metadata,
            Column("cd_customer", String(256), primary_key=True),
            Column("nm_customer", String(135), primary_key=False),
            Column("st_email", String(135), primary_key=False),
            Column("st_phone", String(135), primary_key=False),
            Column("sg_state", String(2), primary_key=False),
            Column("dt_birth", Date, primary_key=False)
        )

    def create(self):
        with self.engine.begin() as conn:
            self.metadata.create_all(conn)
            for table in self.metadata.tables:
                print(f"Table {table} created")


if __name__ == "__main__":
    CustomersTable().create()
