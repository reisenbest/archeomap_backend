import environ
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

# Получаем путь к корневому каталогу проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Формируем путь к файлу .env в каталоге app
env_file_path = os.path.join(BASE_DIR, 'app', '.env')

# Создаем объект среды
env = environ.Env()

# Читаем переменные окружения из файла .env
env.read_env(env_file_path)

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = env('ADMIN_USERNAME')
            email = env('ADMIN_EMAIL')
            password = env('ADMIN_PASSWORD')
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(email=email, password=password, username=username)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')