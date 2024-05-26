import environ
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

# Получаем путь к корневому каталогу проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Формируем путь к файлу .env в каталоге app
 

# Создаем объект среды
env = environ.Env()
env_file_path = os.path.join(BASE_DIR, '.env')
# Читаем переменные окружения из файла .env
env.read_env(env_file_path)

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username1 = env('ADMIN_USERNAME1')
            email1 = env('ADMIN_EMAIL1')
            password1 = env('ADMIN_PASSWORD1')
            print('Creating account for %s (%s)' % (username1, email1))
            admin1 = User.objects.create_superuser(email=email1, password=password1, username=username1)
            admin1.is_active = True
            admin1.is_admin = True
            admin1.save()

            username2 = env('ADMIN_USERNAME2')
            email2 = env('ADMIN_EMAIL2')
            password2 = env('ADMIN_PASSWORD2')
            print('Creating account for %s (%s)' % (username2, email2))
            admin2 = User.objects.create_superuser(email=email2, password=password2, username=username2)
            admin2.is_active = True
            admin2.is_admin = True
            admin2.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')