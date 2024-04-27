FROM python:3.12-alpine3.19

#неотбуферизованного вывода для интерпретатора Python
ENV PYTHONUNBUFFERED=1 

#предотвращает создание файлов .pyc
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

COPY app /app

# Устанавливаем права для всего приложения
RUN chmod -R 777 /app

# Устанавливаем разрешения на запись для папки static и media, если они уже существуют
RUN mkdir -p /app/static && chmod -R 777 /app/static
RUN mkdir -p /app/media && chmod -R 777 /app/media

WORKDIR /app

EXPOSE 8000

EXPOSE 5432
RUN apk add --no-cache postgresql-client build-base postgresql-dev

RUN adduser -D service-user

USER service-user

CMD ["gunicorn", "app.wsgi:application", "-b", "0.0.0.0:8000"]
