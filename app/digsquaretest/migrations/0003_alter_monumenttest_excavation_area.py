# Generated by Django 5.0.4 on 2024-05-31 08:32

import django_jsonform.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digsquaretest', '0002_alter_monumenttest_excavation_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monumenttest',
            name='excavation_area',
            field=django_jsonform.models.fields.ArrayField(base_field=models.FloatField(), size=20),
        ),
    ]
