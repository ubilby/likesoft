FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

RUN apt-get install -y gcc

RUN apt-get install -y python3-dev default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    MYSQLCLIENT_CFLAGS=$(mysql_config --cflags) MYSQLCLIENT_LDFLAGS=$(mysql_config --libs) pip install -r requirements.txt --no-cache-dir

COPY . .
