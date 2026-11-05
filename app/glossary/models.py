from django.db import models
from .utils import image_upload_to, make_slug

class GlossaryTerm(models.Model):
    title = models.CharField(verbose_name="Название термина", max_length=200, unique=True,)

    short_definition = models.TextField(verbose_name="Короткое определение", help_text="Показывается во всплывающем пояснении к слову.",)

    description = models.TextField(verbose_name="Полная статья о термине", blank=True, help_text="Подробный текст для отдельной страницы термина.",)

    slug = models.SlugField(max_length=255, unique=True, blank=True,
                            verbose_name="Slug-name для адресной строки")

    is_published = models.BooleanField(verbose_name="Опубликован", default=False,)

    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True,)

    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True,
)
    
    class Meta:
        verbose_name = "Термин словаря"
        verbose_name_plural = "Термины словаря"
        ordering = ["title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_slug(self.title)

            # Если сохраняются только отдельные поля,
            # включаем в них созданный slug.
            if kwargs.get("update_fields") is not None:
                kwargs["update_fields"] = set(kwargs["update_fields"]) | {"slug"}

        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title


class GlossaryImages(models.Model):
    glossary_term = models.ForeignKey(GlossaryTerm, on_delete=models.CASCADE,
                                       related_name="images", verbose_name="Термин",)

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Изображение', blank=True, null=True)
    description = models.TextField(verbose_name='Подпись к картинке', default='Lorem ipsum')
    
    link = models.URLField(max_length=255,  blank=True,
                           verbose_name='Ссылка на изображение')
    
    class Meta:
        verbose_name = 'Изображения для статьи термина'
        verbose_name_plural = 'Изображения для статей терминов'
        

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Изображение: {self.glossary_term.title}"