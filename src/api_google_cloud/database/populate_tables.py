from faker import Faker
from sqlalchemy import MetaData
from db import get_engine
from hashlib import sha256


class GennerateData:
    faker = Faker("pt_BR")
    metadata = MetaData()
    engine = get_engine()

    def __init__(self, table_name, n_records) -> None:
        self.table_name = table_name
        self.n_records = n_records

        with self.engine.connect() as conn:
            self.metadata.reflect(bind=conn)

        self.tables = self.metadata.tables

    def create_data(self):
        if self.table_name not in self.tables:
            print(f"{self.table_name} does not exist")

        if self.table_name == "customers":
            with self.engine.begin() as conn:
                for _ in range(self.n_records):
                    fake_customer_to_insert = self._insert_fake_customers()

                    conn.execute(fake_customer_to_insert)

    def _insert_fake_customers(self):
        table = self.tables[self.table_name]

        insert_command = table.insert().values(
            cd_customer=sha256(self.faker.cpf().encode("utf-8")).hexdigest(),
            nm_customer=self.faker.name(),
            st_email=self.faker.email(),
            st_phone=self.faker.phone_number(),
            sg_state=self.faker.state_abbr(),
            dt_birth=self.faker.date(),
        )

        return insert_command


if __name__ == "__main__":
    GennerateData("customers", 100).create_data()
