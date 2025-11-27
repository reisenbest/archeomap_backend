#!/bin/bash
set -e

### === CONFIG ===
POSTGRES_CONTAINER_NAME="<<<POSTGRES_CONTAINER_NAME>>>"
BACKEND_CONTAINER_NAME="<<<BACKEND_CONTAINER_NAME>>>"
DB_USER="<<<DB_USER>>>"
DB_NAME="<<<DB_NAME>>>"
BASE_BACKUP_DIR="/root/archeomap_backup" ### example: /root/archeomap_backup
VPS_IP="<<<VPS_IP>>>"


# добавляем дату к имени папки
DATE=$(date +%F)   # YYYY-MM-DD
BACKUP_DIR="${BASE_BACKUP_DIR}_${DATE}"
DB_BACKUP_FILENAME="archeomap_db_backup_${DATE}.sql"
MEDIA_BACKUP_FILENAME="archeomap_media_backup_${DATE}.tar.gz"
### ===============

echo "[1/8] Создаю папку $BACKUP_DIR..."
mkdir -p $BACKUP_DIR

echo "[2/8] Дамп базы..."
docker exec -t $POSTGRES_CONTAINER_NAME pg_dump -U "$DB_USER" "$DB_NAME" > "$BACKUP_DIR/$DB_BACKUP_FILENAME"

echo "[3/8] Архив медиа..."
docker exec $BACKEND_CONTAINER_NAME tar czf - -C /app/media . > "$BACKUP_DIR/$MEDIA_BACKUP_FILENAME"

echo "[4/8] Список файлов в backup/"
ls -lh $BACKUP_DIR

echo "[5/8] Бэкап готов на сервере."
echo "Теперь скачайте его на локальную машину:"
echo
echo "  scp root@<<<VPS_IP>>>:$BACKUP_DIR/* ./archeomap_backup/"
echo
echo "[6/8] После скачивания можно удалить:"
echo "  rm -r $BACKUP_DIR"
echo
echo "Готово!"

### чтобы исполнить скрипт: nano <<<script_name>>>.sh > chmod +x /root/<<<script_name>>>.sh >  /root/<<<script_name>>>.sh > rm -r $BACKUP_DIR"