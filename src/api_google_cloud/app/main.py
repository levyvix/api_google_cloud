from db.database_client import DatabaseClient
from db.models import Customers
from fastapi import FastAPI
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/health_check")
async def root():
    return {"message": "OK"}


@app.get("/get_customers")
async def get_customers():
    client = DatabaseClient()

    with Session(client.engine) as session:
        results = session.query(Customers).all()
        return results


@app.get("/get_customers/{customer_id}")
async def get_customers_by_id(customer_id: str):
    client = DatabaseClient()

    with Session(client.engine) as session:
        results = session.query(Customers).filter(Customers.cd_customer == customer_id).all()
        return results
