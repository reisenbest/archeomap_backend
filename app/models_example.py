# Create your models here.

#основной файл с моделями
from django.db import models
from django.urls import reverse

from .models_choices import DatingChoices, ClassificationChoices, CustomCategoryChoices
from map.functions import image_upload_to, markers_upload_to


# TODO: добавить модель с списком литературы два поля CharField с названием и urlfield необязательное со ссылкой

#базовая модель к которой все подключаются
class MonumentsBase(models.Model):
    title = models.CharField(unique=True, max_length=255, blank=False,
                            verbose_name='Название памятника с идентификатором')
    name = models.CharField(unique=True, max_length=255, blank=False,
                            verbose_name='Название памятника')
    description = models.TextField(verbose_name='Краткое описание', default='Lorem ipsum', blank=True)
    administrative_address = models.CharField(verbose_name='Административный адрес',
                                              default='Lorem ipsum',
                                              max_length=255)
    landmark = models.BooleanField(default=False, verbose_name='Обозначение памятника на местности')
    latitude = models.FloatField(blank=True, verbose_name='Широта')
    longitude = models.FloatField(blank=True, verbose_name='Долгота')
    dating = models.ManyToManyField('Dating')
    classification_category = models.ManyToManyField('Classification')
    custom_category = models.ManyToManyField('CustomCategory')
    research_years = models.ManyToManyField('ResearchYears', blank=True)
    authors = models.ManyToManyField('Authors', blank=True)
    organizations = models.ManyToManyField('Organizations', blank=True)
    audio = models.CharField(max_length=255, blank=True, default='Отсутствует',
                             verbose_name='Ссылка на аудио-файл')
    video = models.CharField(max_length=255, blank=True, default='Отсутствует',
                             verbose_name='Ссылка на видео-файл')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=False)
    visible = models.BooleanField(default=True, verbose_name='Видимость записи')
    marker_image = models.ForeignKey('MarkersForPopup', null=True, on_delete=models.SET_NULL,
                                     related_name='image')

    class Meta:
        verbose_name = 'Археологические памятники'
        verbose_name_plural = 'Археологические памятники'

    def get_absolute_url(self):
        return reverse('monumentlist', kwargs={'monument_slug': self.slug})

    def __str__(self):
        return self.title


class Dating(models.Model):
    dating_value = models.CharField(max_length=255,
                              choices=DatingChoices.choices,
                              verbose_name='Датировка памятника')

    class Meta:
        verbose_name = 'Датировка памятника'
        verbose_name_plural = 'Датировка памятника'

    def __str__(self):
        return self.dating_value


class Classification(models.Model):
    classification_category_value = models.CharField(max_length=255,
                                               choices=ClassificationChoices.choices,
                                               verbose_name='Тип')

    class Meta:
        verbose_name = 'Классификация памятника'
        verbose_name_plural = 'Классификация памятника'

    def __str__(self):
        return self.classification_category_value


class CustomCategory(models.Model):
    custom_category_value = models.CharField(max_length=255,
                                       choices=CustomCategoryChoices.choices,
                                       verbose_name='Кастомная категория')

    class Meta:
        verbose_name = 'Кастомная категория'
        verbose_name_plural = 'Кастомная категория'

    def __str__(self):
        return self.custom_category_value


class ResearchYears(models.Model):
    year = models.IntegerField(unique=True, verbose_name='Год исследования', blank=True)

    class Meta:
        verbose_name = 'Года раскопок'
        verbose_name_plural = 'Года раскопок'

    def __str__(self):
        return str(self.year)


class Authors(models.Model):
    author = models.CharField(unique=True, verbose_name='Археолог', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Список археологов'
        verbose_name_plural = 'список археологов'

    def __str__(self):
        return self.author


class Organizations(models.Model):
    organization = models.CharField(unique=True, verbose_name='Организация', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Список организаций'
        verbose_name_plural = 'Список организаций'

    def __str__(self):
        return self.organization



class ImagesGallery(models.Model):
    monument = models.ForeignKey(MonumentsBase, on_delete=models.CASCADE, related_name='images', to_field='title')
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Изображение', blank=True, null=True)
    description = models.TextField(verbose_name='Подпись к картинке', default='Lorem ipsum')

    class Meta:
        verbose_name = 'Изображения для попапов'
        verbose_name_plural = 'Изображения для попапов'

    def __str__(self):
        return str(self.monument)

class MarkersForPopup(models.Model):
    title = models.CharField(max_length=255, null=True,
                             choices=ClassificationChoices.choices,
                             verbose_name='Тип', default=ClassificationChoices.NONE)
    marker_image = models.ImageField(upload_to=markers_upload_to, verbose_name='Маркер', blank=True, null=True)

    class Meta:
        verbose_name = 'Маркеры для попапов'
        verbose_name_plural = 'Маркеры для попапов'

    # def get_absolute_url(self):
    #     return reverse('addimagestomonument')

    def __str__(self):
        return str(self.title)





