FROM python

RUN pip install flask && pip install entsoe-py

WORKDIR /app

COPY ./src .

CMD ["python", "app.py"]
