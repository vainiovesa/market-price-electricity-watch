FROM python:3.12-alpine AS build-stage

WORKDIR /wheels

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps -r requirements.txt

FROM python:3.12-alpine

WORKDIR /app

COPY --from=build-stage /wheels /wheels

COPY src/ .

RUN pip install --no-cache-dir /wheels/*.whl && \
 rm -rf /wheels && \
 adduser -D appuser && \ 
 chown -R appuser .

USER appuser

CMD ["python", "app.py"]
