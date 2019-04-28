from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название города')
    name_en = models.CharField(max_length=50, verbose_name='Название города анг.', default='-')
    city_id = models.IntegerField(verbose_name='Индекс', default=2025339)
    c_lon = models.FloatField(max_length=10, verbose_name='Долгота', default=113.5)
    c_lat = models.FloatField(max_length=10, verbose_name='Широта', default=52.03)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
