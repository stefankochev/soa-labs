FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0"]
