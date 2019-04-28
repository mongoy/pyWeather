# Generated by Django 2.1.7 on 2019-04-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='c_lat',
            field=models.FloatField(default=52.03, max_length=10, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='city',
            name='c_lon',
            field=models.FloatField(default=113.5, max_length=10, verbose_name='Долгота'),
        ),
        migrations.AddField(
            model_name='city',
            name='city_id',
            field=models.IntegerField(default=2025339, verbose_name='Индекс'),
        ),
    ]
