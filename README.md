Археологическая карта СПб. Backend 

тест коммит

### Running
* скопировать ./.env.example в ./.env
* скопировать ./app/.env.example в ./app/.env, заполнить SecretKey рандомными значениями

команды:
pyhton manage.py import_data - загрузка данных о памятнкиах из json в базу
pyhton manage.py set_authors - загрузка данныех об авторах в базу
python manage.py set_organizations - загрузка данных об организация



