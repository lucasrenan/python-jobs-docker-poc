FROM python:3.8.9-alpine3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT ["python3", "/app/main.py"]
