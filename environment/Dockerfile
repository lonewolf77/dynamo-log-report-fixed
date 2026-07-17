FROM python:3.12-slim@sha256:01d51c70e28f1141df9ddf7d5ca4ba1fb0a739be03657b98d1a3c6d7d8e8740f

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
