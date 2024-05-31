from django.db import models
from django_jsonform.models.fields import ArrayField
# Create your models here.



class MonumentTest(models.Model):
    title = models.CharField(max_length=255)
    excavation_area = ArrayField(
        ArrayField(
            models.FloatField(),
            size=2,  # каждый вложенный массив должен содержать 2 элемента
        ),
        size=20  # максимальное количество вложенных массивов
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'MonumentTest'
        verbose_name_plural = 'MonumentTest'
