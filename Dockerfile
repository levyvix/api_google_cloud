FROM python:3.11-slim-bullseye

WORKDIR /app

COPY pyproject.toml pdm.lock ./

RUN pip install pdm && pdm install

COPY /src/api_google_cloud/app ./

EXPOSE 8000


ENV DB_HOST=host.docker.internal

CMD [ "pdm", "run" ,"fastapi", "run", "/app/main.py", "--host=0.0.0.0", "--port=8000" ]