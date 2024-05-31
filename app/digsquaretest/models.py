from django.db import models

# Create your models here.

from django.db import models
from django.contrib.postgres.fields import ArrayField

class MonumentTest(models.Model):
    title = models.CharField(max_length=255)
    excavation_area = ArrayField(
        ArrayField(
            models.FloatField(),
            size=2,  # Внутренний массив всегда содержит 2 элемента (широта и долгота)
        ),
        size=None,  # Внешний массив может содержать произвольное количество элементов (пар координат)
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'MonumentTest'
        verbose_name_plural = 'MonumentTest'
