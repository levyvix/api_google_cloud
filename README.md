# api_google_cloud

## Docker

Postgres

```bash
cd docker/postgres
docker-compose up -d
```

API

```bash
docker-compose up -d
```

## Local

Postgres

```bash
cd docker/postgres
docker-compose up -d
```

Posgres Data

```bash
cd src/api_google_cloud/database
python3 create_tables.py
python3 populate_tables.py
```

API

```bash
python -m venv .venv
source .venv/bin/activate
pip install pdm
pdm install
pdm run fastapi dev src/api_google_cloud/app/main.py
```

## Docker compose

```bash
docker-compose up -d
```

```bash
docker-compose down
```
