from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
from .utils import image_upload_to
from .choices import ClassificationChoices, CustomCategoryChoices, DatingChoices

class MODELNAMERetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = MODELNAME.objects.all()
    serializer_class = MODELNAMEModelSerializer




# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=255,)
    latitude = models.FloatField(default=10)
    longitude = models.FloatField(default=10)
    category = models.ManyToManyField("archeomap.TestCategory", verbose_name=("категория"))

    def __str__(self):
        return self.name


class TestCategory(models.Model):
    category = models.CharField(max_length=255,)

    def __str__(self):
        return self.category


class Monuments(models.Model):
    #TODO: валидатор написать должно заканчиваться на _\d{3}
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
                            db_index=True, verbose_name="Slug-name", 
                            null=True, blank=True)
    visible = models.BooleanField(default=True, verbose_name='Видимость записи')

    #TODO: подумать о том как легко организовать запрос к базе чтобы легко было отрисовывать. оптимизация
    latitude = models.FloatField(verbose_name="Широта",
                                 validators=[MinValueValidator(-90), MaxValueValidator(90)])
    #TODO: подумать о том как легко организовать запрос к базе чтобы легко было отрисовывать. оптимизация
    longitude = models.FloatField(verbose_name='Долгота',
                                  validators=[MinValueValidator(-180), MaxValueValidator(180)])
    sources = models.ManyToManyField('Sources', 
                                     verbose_name='Список использованных источников') #список источников использованных
    content = models.ManyToManyField('Content', 
                                     verbose_name='Аудио-видео контент') #аудио-видео контент про памятник 
    dating = models.ManyToManyField('Dating',
                                     verbose_name='Датировка')
    classification_category = models.ManyToManyField('Classification',
                                                      verbose_name='Категория')
    custom_category = models.ManyToManyField('CustomCategory', blank=True, 
                                             verbose_name='Дополнительная категория')
    research_years = models.ManyToManyField('ResearchYears', blank=True,
                                            verbose_name='Годы исследования')
    authors = models.ManyToManyField('Authors', blank=True,
                                     verbose_name='Авторы раскопок')
    organizations = models.ManyToManyField('Organizations', blank=True,
                                           verbose_name='Организация')

    class Meta:
        #TODO: посмотерть как класс Мета оформляет Мело в книге по джанго
        verbose_name = 'Археологические памятники'
        verbose_name_plural = 'Археологические памятники'

    def get_absolute_url(self):
        return reverse('monumentlist', kwargs={'monument_slug': self.slug})
    #TODO: разобраться с слагом, сейчас отдает только цифры в конце
    def save(self, *args, **kwargs):
        if not self.slug and self.title:  
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)  
        
    def __str__(self):
        return self.title

class Dating(models.Model):
    dating_value = models.CharField(max_length=255,
                              choices=DatingChoices.choices,
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
    year = models.IntegerField(unique=True, verbose_name='Год исследования', blank=False)

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
        return f'{self.what_is}'

class Content(models.Model):
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

    class Meta:
        verbose_name = 'Изображения для странички с описанием памятника'
        verbose_name_plural = 'Изображения для странички с описанием памятника'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.monument}'

