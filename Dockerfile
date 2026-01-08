FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt && adduser -D appuser

COPY src/ .

RUN chown -R appuser .

USER appuser

CMD ["python3", "app.py"]
