# Generated by Django 2.1.7 on 2019-04-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20190428_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name_en',
            field=models.CharField(default='-', max_length=50, verbose_name='Название города анг.'),
        ),
    ]