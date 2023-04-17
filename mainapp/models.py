from django.db import models

# Create your models here.


class AzsDB(models.Model):
    number_azs = models.CharField(max_length=50, verbose_name='Номер АЗС')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    latitude = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Долгота')
    DT = models.CharField(max_length=20, verbose_name='ДТ', blank=True, null=True)
    DT_Taneko = models.CharField(max_length=20, verbose_name='ДТ_танеко', blank=True, null=True)
    DT_winter = models.CharField(max_length=20, verbose_name='ДТ_зимнее', blank=True, null=True)
    DT_arctic = models.CharField(max_length=20, verbose_name='ДТ_арктика', blank=True, null=True)

