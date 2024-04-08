#FROM python:3.10
FROM mcr.microsoft.com/devcontainers/python:3.10

WORKDIR /app
COPY ./.docker/fastapi/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ../fastapi ./


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]