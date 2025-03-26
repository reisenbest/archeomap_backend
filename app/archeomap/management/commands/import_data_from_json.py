import json
from django.core.management.base import BaseCommand
from archeomap.models.models import Monuments, Dating, Classification, CustomCategory, ResearchYears, ExcavationsSquare

"""
добавляет памятники (или обновляет данные для существующих (поле title) или добавляет тех, которых нет. 
json документ должен лежаать в корне (директория с manage.py)
json формируется из эксель дока скриптом
"""


class Command(BaseCommand):
    help = "Импортирует памятники из JSON, обновляя существующие"

    def handle(self, *args, **kwargs):
        with open("monuments.json", "r", encoding="utf-8") as file:
            data_list = json.load(file)
            
        ### ебейшая заглушка, убрать потом подумать как поправить. не нравится что нулл
        for data in data_list:
            if data['landmark'] == None:
                data['landmark'] = '' 

        for data in data_list:
            # Проверяем, есть ли объект с таким title, и обновляем его, если он есть
            monument, created = Monuments.objects.update_or_create(
                title=data["title"],
                defaults={
                    "name": data["name"],
                    "description": data["description"],
                    "landmark": data["landmark"],
                    "address": data["address"],
                    "latitude": data["latitude"],
                    "longitude": data["longitude"]
                }
            )

            # Обновляем связанные объекты ManyToMany
            monument.dating.clear()
            for dating_value in data.get("dating", []):
                dating_obj, _ = Dating.objects.get_or_create(dating_value=dating_value)
                monument.dating.add(dating_obj)

            monument.classification_category.clear()
            for classification_value in data.get("classification_category", []):
                classification_obj, _ = Classification.objects.get_or_create(classification_category_value=classification_value)
                monument.classification_category.add(classification_obj)

            # monument.custom_category.clear()
            # for custom_category_value in data.get("custom_category", []):
            #     custom_category_obj, _ = CustomCategory.objects.get_or_create(custom_category_value=custom_category_value)
            #     monument.custom_category.add(custom_category_obj)

            monument.research_years.clear()
            for year in data.get("research_years", []):
                research_years_obj, _ = ResearchYears.objects.get_or_create(year=year)
                monument.research_years.add(research_years_obj)

            monument.research_years.clear()
            for year in data.get("research_years", []):
                research_years_obj, _ = ResearchYears.objects.get_or_create(year=year)
                monument.research_years.add(research_years_obj)
            

            ### пока закомменчено тк есть пробелемы. обнулит существующие если в экскль таблице ничего не заполнено
            ### крч да разобраться надо с этим
            # if data.get("excavation_square"):
            #     excavation_squares = ExcavationsSquare.objects.filter(monument=monument)
                
            #     new_squares = [
            #         [float(coord[0]), float(coord[1])] for coord in data["excavation_square"]
            #     ]
                
            #     if excavation_squares.exists():
            #         # Берем первый объект (если вдруг есть несколько, хотя такого быть не должно)
            #         excavation = excavation_squares.first()
                    
            #         if excavation.excavation_square != new_squares:
            #             excavation.excavation_square = new_squares
            #             excavation.save()
                        
            #     else:
            #         ExcavationsSquare.objects.create(
            #             monument=monument,
            #             excavation_square=new_squares,
            #             description="Lorem ipsum"
            #         )
                    


            monument.save()
            
            action = "Добавлен" if created else "Обновлен"
            self.stdout.write(self.style.SUCCESS(f"{action} памятник: {monument.name}"))
