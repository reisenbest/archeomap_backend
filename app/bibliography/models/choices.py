from django.db import models

class BibliographyMainCategoryChoices(models.TextChoices):
    UNKNOWN = 'Unknown', 'Unknown'
    URBAN_ARCHEOLOGY = 'Городская археология', 'Городская археология'
    SPB_АRCHELOGY = 'Археология Санкт-Петербурга', 'Археология Санкт-Петербурга'

class BibliographySubCategoryChoices(models.TextChoices):
    UNKNOWN = 'Unknown', 'Unknown'
    BOOK = 'Книги', 'Книги'
    ARTICLE = 'Статьи', 'Статьи'
    POPULAR_LECTION = 'Образовательные видео\Научно-популярные лекции', 'Образовательные видео\Научно-популярные лекции'
    DIGITAL_CONTENT = 'Цифровые проекты','Цифровые проекты'
    LAWS_AND_REGULATIONS = 'Законодательные акты и другие нормативные документы', 'Законодательные акты и другие нормативные документы'
    OTHER = 'Другое', 'Другое'

