from django.core.management.base import BaseCommand
from archeomap.models.models import ResearchYears


class Command(BaseCommand):
    help = 'Заполняет ResearchYears годами с 1900 по 2040'
    def handle(self, *args, **kwargs):
        list_of_years = [year for year in range(1900, 2041)] 

        for year in list_of_years:
          year, created = ResearchYears.objects.update_or_create(year=year, defaults={'year':year})

          if created == True:
             self.stdout.write(f'Год {year} добавлен в ResearchYears')
          else:
            self.stdout.write(f'Год {year} уже существует в ResearchYears')  

