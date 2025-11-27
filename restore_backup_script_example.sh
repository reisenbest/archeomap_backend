#!/bin/bash
set -e

### === CONFIG ===
# Контейнеры
DOCKER_DB_CONTAINER_NAME="<<<DOCKER_DB_CONTAINER_NAME>>>"
DOCKER_BACKEND_CONTAINER_NAME="<<<DOCKER_BACKEND_CONTAINER_NAME>>>"

# База данных
DB_USER="<<<DB_USER>>>"
DB_NAME="<<<DB_NAME>>>"

# Пути на VPS
BACKUP_DIR="<<<BACKUP_DIR>>>"

# Имена файлов бэкапа
DB_BACKUP_FILENAME="<<<DB_BACKUP_FILENAME.SQL>>>" 
MEDIA_BACKUP_FILENAME="<<<MEDIA_BACKUP_FILENAME.TAR.GZ>>>" 

# VPS данные
VPS_USER="<<<USERNAME>>>"
VPS_IP="<<<VPS_IP>>>"

# Опция удаления временных файлов после восстановления
DELETE_BACKUP_AFTER_RESTORE=true
### ===============

echo "[1/6] Переносим медиа архив в контейнер backend..."
docker cp "$BACKUP_DIR/$MEDIA_BACKUP_FILENAME" "$DOCKER_BACKEND_CONTAINER_NAME:/tmp/"

echo "[2/6] Удаляем старую папку monuments полностью..."
docker exec -i "$DOCKER_BACKEND_CONTAINER_NAME" rm -rf /app/media/monuments

echo "[3/6] Распаковываем медиа архив (замена папки monuments)..."
docker exec -i "$DOCKER_BACKEND_CONTAINER_NAME" tar xzf "/tmp/$MEDIA_BACKUP_FILENAME" -C /app/media

echo "[4/6] Удаляем архив из контейнера..."
docker exec --user root "$DOCKER_BACKEND_CONTAINER_NAME" rm -f "/tmp/$MEDIA_BACKUP_FILENAME"

echo "[5/6] Пересоздаём базу данных..."
docker exec -i "$DOCKER_DB_CONTAINER_NAME" psql -U "$DB_USER" -c "DROP DATABASE IF EXISTS $DB_NAME;"
docker exec -i "$DOCKER_DB_CONTAINER_NAME" psql -U "$DB_USER" -c "CREATE DATABASE $DB_NAME;"

echo "[6/6] Восстанавливаем SQL дамп..."
cat "$BACKUP_DIR/$DB_BACKUP_FILENAME" | docker exec -i "$DOCKER_DB_CONTAINER_NAME" psql -U "$DB_USER" -d "$DB_NAME"

if [ "$DELETE_BACKUP_AFTER_RESTORE" = true ]; then
    echo "[+] Удаляем бэкап с VPS..."
    rm -f "$BACKUP_DIR/$DB_BACKUP_FILENAME" "$BACKUP_DIR/$MEDIA_BACKUP_FILENAME"
fi

echo "✅ Восстановление завершено!"

### чтобы исполнить скрипт: nano <<<script_name>>>.sh > chmod +x /root/<<<script_name>>>.sh >  /root/<<<script_name>>>.sh > rm -r $BACKUP_DIR"