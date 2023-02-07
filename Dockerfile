FROM python:3.10-slim-buster

LABEL maintainer="Saeid Bostandoust <ssbostan@yahoo.com>"

EXPOSE 8080

ENV NEPTUNE_API_ENV=production
ENV NEPTUNE_API_DEBUG=0
ENV NEPTUNE_API_TESTING=0
ENV NEPTUNE_API_DATABASE_URI=None

WORKDIR /opt/app

RUN apt-get update && apt-get install -y build-essential \
  libffi-dev libssl-dev python3-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ./start
