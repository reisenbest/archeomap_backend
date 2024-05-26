from django.db import models
from .choices import BibliographyMainCategoryChoices, BibliographySubCategoryChoices
from django.core.validators import MinValueValidator, MaxValueValidator


class Bibliography(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Топик источника для админ-панели', blank=True)
    source = models.TextField(verbose_name='Объект библиографии (ссылка)')
    link = models.URLField(max_length=255, blank=True, null=True,
                           verbose_name='Ссылка на источник если есть')
    what_is = models.CharField(
        max_length=255, verbose_name='Кратко об источнике (пояснение для пользователя)', blank=True)
    publication_date = models.IntegerField(verbose_name='Год публикации', blank=True, null=True,
                                           validators=[MinValueValidator(1700), MaxValueValidator(2100)])
    source_identificator = models.CharField(
        max_length=255, verbose_name='DOI\ISBN', blank=True)
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name="Slug-name",
                            null=True, blank=True)
    visible = models.BooleanField(
        default=True, verbose_name='Видимость записи')
    main_category = models.CharField(
        max_length=100,
        choices=BibliographyMainCategoryChoices.choices,
        verbose_name='Главная категория (область знаний)',
        default=BibliographyMainCategoryChoices.UNKNOWN
    )
    sub_category = models.CharField(
        max_length=100,
        choices=BibliographySubCategoryChoices.choices,
        verbose_name='Тип источника',
        default=BibliographySubCategoryChoices.UNKNOWN
    )

    class Meta:
        verbose_name = 'Библиография'
        verbose_name_plural = 'Библиография'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'
