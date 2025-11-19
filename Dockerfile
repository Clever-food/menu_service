FROM python:3.10

WORKDIR /project

COPY ./requirements.txt .

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

COPY . .

ENTRYPOINT [ "sh", "-c", "uvicorn --host 0.0.0.0 --port 8001 main:app"]