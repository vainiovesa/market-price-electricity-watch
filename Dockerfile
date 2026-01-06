FROM python

RUN pip install flask && pip install entsoe-py

WORKDIR /app

COPY . .

CMD ["python", "src/app.py"]
