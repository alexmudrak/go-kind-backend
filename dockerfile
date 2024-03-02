FROM python:3.8

RUN mkdir -p /app
WORKDIR /app

RUN useradd -u 1000 -d /app -M uvicorn

COPY ./api ./
RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/"

EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]