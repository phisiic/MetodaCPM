# Generated by Django 5.0.4 on 2024-04-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=20)),
                ('activityAmount', models.IntegerField()),
                ('eventAmount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='zdarzenie',
            name='float_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='zdarzenie',
            name='ti',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='zdarzenie',
            name='tj',
            field=models.IntegerField(default=0),
        ),
    ]
