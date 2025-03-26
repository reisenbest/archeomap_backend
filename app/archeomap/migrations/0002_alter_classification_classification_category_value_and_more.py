# Generated by Django 5.0.4 on 2025-03-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archeomap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='classification_category_value',
            field=models.CharField(choices=[('Не определено', 'Не определено'), ('Unknown', 'Unknown'), ('Санитарные захоронения', 'Санитарные захоронения'), ('Исторические кладбища', 'Исторические кладбища'), ('Одиночные захоронения', 'Одиночные захоронения'), ('Погребения в пределах храмового комплекса', 'Погребения в пределах храмового комплекса'), ('Культовые сооружения (Храмы\\Церкви\\Часовни)', 'Культовые сооружения (Храмы\\Церкви\\Часовни)'), ('Клады\\случайные находки', 'Клады\\случайные находки'), ('Крепости\\укрепления\\фортификационные сооружения', 'Крепости\\укрепления\\фортификационные сооружения'), ('Жилые постройки', 'Жилые постройки'), ('Общественные постройки', 'Общественные постройки'), ('Хозяйственные постройки', 'Хозяйственные постройки'), ('Промышленные постройки', 'Промышленные постройки'), ('Морские постройки', 'Морские постройки'), ('Постройки неизвестного назначения', 'Постройки неизвестного назначения'), ('Инфраструктурные объекты', 'Инфраструктурные объекты'), ('Парки\\архитектура малых форм', 'Парки\\архитектура малых форм'), ('Подводные памятники', 'Подводные памятники'), ('Дворцы', 'Дворцы'), ('Участок культурного слоя', 'Участок культурного слоя'), ('Памятники доисторической эпохи', 'Памятники доисторической эпохи'), ('Памятники Железного века и Средневековья', 'Памятники Железного века и Средневековья'), ('Памятники эпохи шведского владычества', 'Памятники эпохи шведского владычества')], max_length=255, unique=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='customcategory',
            name='custom_category_value',
            field=models.CharField(choices=[('NONE', 'NONE'), ('Памятники с обозначением на местности', 'Памятники с обозначением на местности'), ('Уникальные археологические памятники', 'Уникальные археологические памятники'), ('Памятники, напрямую связанные с историческими личностями', 'Памятники, напрямую связанные с историческими личностями'), ('Первые археологические раскопки в Петербурге', 'Первые археологические раскопки в Петербурге'), ('Захоронения первостроителей Петербурга', 'Захоронения первостроителей Петербурга'), ('Места сражений', 'Места сражений'), ('Расположение раскопов', 'Расположение раскопов')], max_length=255, unique=True, verbose_name='Кастомная категория'),
        ),
        migrations.AlterField(
            model_name='dating',
            name='dating_value',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('VI-IV тыс. до н.э ', 'VI-IV тыс. до н.э '), ('III - нач. I тыс. до н.э', 'III - нач. I тыс. до н.э'), ('I тыс. до н.э - кон. I тыс. н.э', 'I тыс. до н.э - нач I тыс. н.э'), ('кон. I тыс. н.э - нач. XVII в.', 'кон. I тыс. н.э - нач. XVII в.'), ('1 пол. XVII в.', '1 пол. XVII в.'), ('2 пол. XVII в.', '2 пол. XVII в.'), ('1 пол. XVIII в.', '1 пол. XVIII в.'), ('2 пол. XVIII в.', '2 пол. XVIII в.'), ('1 пол. XIX в.', '1 пол. XIX в.'), ('2 пол. XIX в.', '2 пол. XIX в.'), ('1 чт. XX в.', '1 чт. XX в.')], max_length=255, unique=True, verbose_name='Датировка памятника'),
        ),
    ]
