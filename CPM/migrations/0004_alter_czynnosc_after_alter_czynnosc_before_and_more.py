# Generated by Django 5.0.4 on 2024-05-09 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPM', '0003_alter_czynnosc_after_alter_czynnosc_before'),
    ]

    operations = [
        migrations.AlterField(
            model_name='czynnosc',
            name='after',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='czynnosc',
            name='before',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='czynnosc',
            name='duration',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
