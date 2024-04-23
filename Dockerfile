FROM python:3.12-alpine3.19

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /temp/requirements.txt
COPY app /app

RUN chmod -R 777 /app

WORKDIR /app

EXPOSE 5432

RUN apk add --no-cache postgresql-client build-base postgresql-dev
# Устанавливаем обновления и необходимые модули

RUN pip install -r /temp/requirements.txt

RUN adduser -D service-user

USER service-user
