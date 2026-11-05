from django.db import models
from .utils import article_image_upload_to, article_preview_image_upload_to
# Create your models here.


class Articles(models.Model):
    title = models.CharField(verbose_name='Название статьи',
                             max_length=255, unique=True,)

    preview_text = models.TextField(verbose_name='Текст превью',
                                    help_text='Короткий анонс статьи, который должен заинтересовать читателя.',
                                    default='Lorem ipsum', blank=True)
    
    main_text = models.TextField(verbose_name='Основное содержание статьи',
                                 default='Lorem ipsum', blank=True)
    
    slug = models.SlugField(verbose_name='Slug для адреса статьи',
                            max_length=255, unique=True)

    categories = models.ManyToManyField('Categories',
                                        verbose_name='Категории статьи',
                                        related_name='articles',
                                        blank=True)

    tags = models.ManyToManyField('Tags',
                                  verbose_name='Теги статьи',
                                  related_name='articles',
                                  blank=True)

    authors = models.ManyToManyField('Authors',
                                  verbose_name='Авторы статьи',
                                  related_name='articles',
                                  blank=True)

    
    is_published = models.BooleanField(verbose_name='Статус публикации',
                                       default=False)

    created_at = models.DateTimeField(verbose_name='Время создана',
                                      auto_now_add=True,)

    updated_at = models.DateTimeField(verbose_name='Время изменения',
                                      auto_now=True)



    class Meta: 
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
        

class Categories(models.Model):
  article_category_value = models.CharField(verbose_name='Название категори',
                                            max_length=255, unique=True, help_text='Категории для фильтрации статей')

  class Meta: 
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
    ordering = ['article_category_value']

  def save(self, *args, **kwargs):
          super().save(*args, **kwargs)

  def __str__(self):
    return self.article_category_value


class Tags(models.Model):
  article_tag_value = models.CharField(verbose_name='Наименование тега',
                                       max_length=200, unique=True, help_text='Теги для образовательных статей')

  class Meta:
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'
    ordering = ['article_tag_value']

  def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

  def __str__(self):
    return self.article_tag_value

class Authors(models.Model):

    author = models.CharField(unique=True, verbose_name='Археолог', max_length=255, blank=False)

    class Meta:
        verbose_name = 'Список авторов статьи'
        verbose_name_plural = 'Список авторов статьи'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author}'



class ArticleImages(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE,
                                verbose_name='Статья', related_name='images')

    image = models.ImageField(upload_to=article_image_upload_to,
                              verbose_name='Изображение',
                              blank=True, null=True)

    description = models.TextField(verbose_name='Подпись к картинке', default='Lorem ipsum')
    
    link = models.URLField(max_length=255,  blank=True, null=True,
                               verbose_name='Ссылка на изображение')

    class Meta:
        verbose_name = 'Фотогрфия статьи'
        verbose_name_plural = 'Фотографии статей'

    def __str__(self):
        return f'{self.article} - {self.description}'
    

class ArticlePreviewImage(models.Model):
    article = models.OneToOneField(
        Articles,
        verbose_name='Статья',
        on_delete=models.CASCADE,
        related_name='preview_image',
    )

    image = models.ImageField(
        verbose_name='Изображение превью',
        upload_to=article_preview_image_upload_to,
    )

    class Meta:
        verbose_name = 'Превью изорбражение статьи'
        verbose_name_plural = 'Превью изображения статей'

    def __str__(self):
        return f'Превью изображение статьи: {self.article}'