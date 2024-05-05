FROM python:3.12-alpine3.19

# Неотбуферизованный вывод для интерпретатора Python
ENV PYTHONUNBUFFERED=1 

# Предотвращает создание файлов .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

# Копируем приложение
COPY app /app

# Устанавливаем права для всего приложения
RUN chmod -R 777 /app

# Устанавливаем разрешения на запись для папок static и media, если они уже существуют
RUN mkdir -p /app/static && chmod -R 777 /app/static
RUN mkdir -p /app/media && chmod -R 777 /app/media

# Создаем папку monuments и даем права на доступ
RUN mkdir -p /app/media/monuments && chmod -R 777 /app/media/monuments

# Рабочая директория
WORKDIR /app

# Открываем порты
EXPOSE 8000
EXPOSE 5432

# Устанавливаем дополнительные зависимости
RUN apk add --no-cache postgresql-client build-base postgresql-dev

# Создаем пользователя и добавляем его в группу root
RUN adduser -D -G root service-user

# Устанавливаем пользователя по умолчанию
USER service-user

# Команда по умолчанию для запуска приложения
CMD ["gunicorn", "app.wsgi:application", "-b", "0.0.0.0:8000"]
