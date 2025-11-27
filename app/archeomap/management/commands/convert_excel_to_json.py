import json
from django.core.management.base import BaseCommand


"""
создаем из эксель файла с базой данных файл json
"""


class Command(BaseCommand):
    help = "Конвертация эксель таблицы с памятниками в JSON"

    def handle(self, *args, **kwargs):
        with open("monuments.json", "r", encoding="utf-8") as file:
            data_list = json.load(file)




'''
1 - открываем эксель файл
2 - создаем json Док

цикл который проходит столько раз сколько строк в эксель таблице кроме первой строки
в теле цикла пробегаемся по столлбам  которые зашиты в специальном списке столбцов


'''