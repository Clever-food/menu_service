FROM python:3.10-slim

WORKDIR /project

COPY ./requirements.txt .

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

RUN apt-get update

COPY . .

ENTRYPOINT [ "sh", "-c", "uvicorn --host 0.0.0.0 --port 8001 main:app"]