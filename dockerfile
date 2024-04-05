FROM python:3.11

RUN mkdir -p /app
WORKDIR /app

RUN useradd -u 1000 -d /app -M uvicorn

COPY ./src ./
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/"

EXPOSE 8000
CMD ["uvicorn", "main:app", "--ssl-keyfile", "./certificates/key.pem", "--ssl-certfile", "./certificates/cert.pem", "--host", "0.0.0.0", "--port", "8000", "--reload"]
