from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
from .utils import image_upload_to, make_slug
from .choices import ClassificationChoices, CustomCategoryChoices, DatingChoices, IconChoices
from django.core.validators import MinValueValidator, MaxValueValidator
from django_jsonform.models.fields import ArrayField
# Create your models here.



class Monuments(models.Model):
    #TODO: валидатор написать должно начинаться с на ^\d{4}
    title = models.CharField(max_length=255, unique=True,
                            blank=False, verbose_name='Название памятника с идентификатором')
    name = models.CharField(max_length=255, blank=False, 
                            verbose_name='Название памятника (для пользователей)')
    description = models.TextField(verbose_name='Краткое описание', 
                                   default='Lorem ipsum', blank=True)
    landmark = models.TextField(verbose_name='Что сейчас на месте памятника', 
                                   default='Lorem ipsum', blank=True)
    address = models.CharField(verbose_name='Административный адрес',
                                default='Lorem ipsum',
                                max_length=255)
    slug = models.SlugField(max_length=255, unique=True, 
                            verbose_name="Slug-name", 
                            null=True, blank=True)
    visible = models.BooleanField(default=False, verbose_name='Видимость записи')
    #TODO: подумать о том как легко организовать запрос к базе чтобы легко было отрисовывать. оптимизация
    latitude = models.DecimalField(verbose_name="Широта",
                                 max_digits=9, decimal_places=6,
                                 validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
                                 blank=False)
    #TODO: подумать о том как легко организовать запрос к базе чтобы легко было отрисовывать. оптимизация
    longitude = models.DecimalField(verbose_name='Долгота',
                                    max_digits=9, decimal_places=6,
                                    validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
                                    blank=False)
    dating = models.ManyToManyField('Dating',
                                     verbose_name='Датировка',
                                     blank=True)
    classification_category = models.ManyToManyField('Classification',
                                                      verbose_name='Категория',
                                                      blank=True)
    custom_category = models.ManyToManyField('CustomCategory',  
                                             verbose_name='Дополнительная категория',
                                             blank=True,)
    research_years = models.ManyToManyField('ResearchYears',
                                            verbose_name='Годы исследования',
                                            blank=True,)
    authors = models.ManyToManyField('Authors',
                                     verbose_name='Авторы раскопок',
                                     blank=True)
    organizations = models.ManyToManyField('Organizations',
                                           verbose_name='Организация',
                                           blank=True,)
    icon_choice = models.CharField(verbose_name='Выбор иконки',
                                   max_length=20,
                                   choices=IconChoices,
                                   default=IconChoices.RED)

    class Meta:
        #TODO: посмотерть как класс Мета оформляет Мело в книге по джанго
        verbose_name = 'Археологические памятники'
        verbose_name_plural = 'Археологические памятники'

    def get_absolute_url(self):
        return reverse('monumentlist', kwargs={'monument_slug': self.slug})
    
    #TODO: при изменении названия памятника слаг не пересохраняется, остается прежним
    def save(self, *args, **kwargs):
        if not self.slug and self.name:  
            self.slug = make_slug(self.name)
        super().save(*args, **kwargs)  
        
    def __str__(self):
        return self.name


class Dating(models.Model):
    dating_value = models.CharField(max_length=255,
                              choices=DatingChoices.choices,
                              unique=True,
                              verbose_name='Датировка памятника')

    class Meta:
        verbose_name = 'Датировка памятника'
        verbose_name_plural = 'Датировка памятника'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.dating_value}'
    
class Classification(models.Model):
    classification_category_value = models.CharField(max_length=255,
                                               choices=ClassificationChoices.choices,
                                               unique=True,
                                               verbose_name='Тип')

    class Meta:
        verbose_name = 'Классификация памятника'
        verbose_name_plural = 'Классификация памятника'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.classification_category_value}'

class CustomCategory(models.Model):
    custom_category_value = models.CharField(max_length=255,
                                       choices=CustomCategoryChoices.choices,
                                       unique=True,
                                       verbose_name='Кастомная категория')

    class Meta:
        verbose_name = 'Кастомная категория'
        verbose_name_plural = 'Кастомная категория'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.custom_category_value}'
    
#TODO: сделать валидацию для поля year
class ResearchYears(models.Model):
    year = models.IntegerField(unique=True, 
                               verbose_name='Год исследования', 
                               blank=False, 
                               validators=[MinValueValidator(1700), MaxValueValidator(2100)])

    class Meta:
        verbose_name = 'Года раскопок'
        verbose_name_plural = 'Года раскопок'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.year}'

class Authors(models.Model):
    #TODO: добавить валидацию
    author = models.CharField(unique=True, verbose_name='Археолог', max_length=255, blank=False)

    class Meta:
        verbose_name = 'Список археологов'
        verbose_name_plural = 'Cписок археологов'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author}'


class Organizations(models.Model):
    organization = models.CharField(unique=True, verbose_name='Организация', 
                                    max_length=255, blank=True)

    class Meta:
        verbose_name = 'Список организаций'
        verbose_name_plural = 'Список организаций'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.organization}'
    
class Sources(models.Model):
    monument = models.ForeignKey(Monuments, on_delete=models.CASCADE, 
                                 related_name='sources', to_field='title')
    title = models.TextField(verbose_name='Библиографическая ссылка на источник')
    link = models.URLField(max_length=255, blank=True, null=True,
                           verbose_name='Ссылка на источник если есть')
    what_is = models.CharField(max_length=255, verbose_name='Кратко об источнике', blank=True)
    class Meta:
        verbose_name = 'Список источников'
        verbose_name_plural = 'Список источников'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

class Content(models.Model):
    monument = models.ForeignKey(Monuments, on_delete=models.CASCADE, 
                                 related_name='content', to_field='title')
    title = models.CharField(max_length=255,
                             verbose_name='Тектовое описание единицы контента',
                             blank=False)
    link = models.URLField(max_length=255, unique=True, blank=False,
                           verbose_name='Ссылка на контент')
    
    class Meta:
        verbose_name = 'Список аудио-видео контента для памятников'
        verbose_name_plural = 'Список аудио-видео контента для памятников'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

class Images(models.Model):
    monument = models.ForeignKey(Monuments, on_delete=models.CASCADE, related_name='images', to_field='title')
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Изображение', blank=True, null=True)
    description = models.TextField(verbose_name='Подпись к картинке', default='Lorem ipsum')
    link = models.URLField(max_length=255,  blank=True, null=True,
                           verbose_name='Ссылка на изображение')
    class Meta:
        verbose_name = 'Изображения для странички с описанием памятника'
        verbose_name_plural = 'Изображения для странички с описанием памятника'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.monument}'

class ExcavationsSquare(models.Model):
    monument = models.ForeignKey(Monuments, on_delete=models.CASCADE, 
                                 related_name='excavations_square', to_field='title')
    excavation_square = ArrayField(
        ArrayField(
            models.DecimalField(max_digits=15, decimal_places=12),
            size=2,  # каждый вложенный массив должен содержать 2 элемента. 1 число широта, второе долгота точки
        ),
        size=100,  # максимальное количество вложенных массивов
        blank=True,  # поле необязательно для заполнения
        null=True    # разрешить хранение NULL значений в базе данных
    )
    description = models.TextField(verbose_name='Примечание, откуда взяты координаты', 
                                   default='Lorem ipsum', blank=True)
    
    class Meta:
        verbose_name = 'Координаты площади раскопок'
        verbose_name_plural = 'Координаты площади раскопок'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.monument}'

   