from django.db import models


class DatingChoices(models.TextChoices):
    UNKNOWN = 'Unknown', 'Unknown'
    NEOLITH = 'VI тыс. до н.э ', 'VI тыс. до н.э '
    BRONZE_AGE = 'II - нач. I тыс. до н.э', 'II - нач. I тыс. до н.э'
    IRON_AGE = 'I тыс. до н.э - кон. I тыс. н.э', 'I тыс. до н.э - нач I тыс. н.э'
    MEDIEVAL = 'кон. I тыс. н.э - нач. XVII в.', 'кон. I тыс. н.э - нач. XVII в.'
    XVII_1 = '1 пол. XVII в.', '1 пол. XVII в.'
    XVII_2 = '2 пол. XVII в.', '2 пол. XVII в.'
    XVIII_1 = '1 пол. XVIII в.', '1 пол. XVIII в.'
    XVIII_2 = '2 пол. XVIII в.', '2 пол. XVIII в.'
    XIX_1 = '1 пол. XIX в.', '1 пол. XIX в.'
    XIX_2 = '2 пол. XIX в.', '2 пол. XIX в.'
    XX_1 = '1 чт. XX в.', '1 чт. XX в.'


class ClassificationChoices(models.TextChoices):
    UNKNOWN = 'Unknown', 'Unknown'
    SANITARY_BURIALS = 'Санитарные захоронения', 'Санитарные захоронения'
    CEMETERIES = 'Исторические кладбища', 'Исторические кладбища'
    RELIGIOUS_BUILDINGS = 'Культовые сооружения (Храмы\Церкви\Часовни)', 'Культовые сооружения (Храмы\Церкви\Часовни)'
    RANDOM_FINDS = 'Клады\случайные находки', 'Клады\случайные находки'
    FORTIFICATIONS = 'Крепости\укрепления\фортификационные сооружения', 'Крепости\укрепления\фортификационные сооружения'
    LIVING_BUILDINGS = 'Жилые постройки', 'Жилые постройки'
    PUBLIC_BUILDINGS = 'Общественные постройки', 'Общественные постройки'
    FARM_BUILDINGS = 'Хозяйственные постройки', 'Хозяйственные постройки'
    INDUSTRIAL_BUILDINGS = 'Промышленные постройки', 'Промышленные постройки'
    MARITIME_BUILDINGS = 'Морские постройки', 'Морские постройки'
    INFRASTRUCTURE = 'Инфраструктурные объекты', 'Инфраструктурные объекты'
    PARKS_SCULPTURES = 'Парки\архитектура малых форм', 'Парки\архитектура малых форм'
    UNDERWATER = 'Подводные памятники', 'Подводные памятники'
    PALACES = 'Дворцы', 'Дворцы'
    CULTURAL_LAYER = 'Участок культурного слоя', 'Участок культурного слоя'
    BEFORE_CHRIST = 'Памятники доисторической эпохи', 'Памятники доисторической эпохи'  # категория по дате
    IRON_MIDDLE_AGE = 'Памятники Железного века и Средневековья', 'Памятники Железного века и Средневековья'  # категория по дате

    

class CustomCategoryChoices(models.TextChoices):
    NONE = 'NONE', 'NONE'
    WITH_LANDMARK = 'Памятники с обозначением на местности', 'Памятники с обозначением на местности'
    BEST = 'Уникальные археологические памятники', 'Уникальные археологические памятники'
    PERSONALITIES = 'Памятники, напрямую связанные с историческими личностями', 'Памятники, напрямую связанные с историческими личностями'
    FIRST_EXCAVATIONS = 'Первые археологические раскопки в Петербурге', 'Первые археологические раскопки в Петербурге'
    FIRST_BUILDERS_BURIAL = 'Захоронения первостроителей Петербурга', 'Захоронения первостроителей Петербурга'
    BATTLE_FIELD = 'Место сражения', 'Место сражения'