FROM python:3.9-slim

RUN apt-get -y update; apt-get -y install curl

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--log-config", "logging_config.yaml"]
