# Generated by Django 5.0.4 on 2024-05-31 08:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digsquaretest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monumenttest',
            name='excavation_area',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None),
        ),
    ]
