# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /root

EXPOSE 8000

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "uvicorn", "main:app"]