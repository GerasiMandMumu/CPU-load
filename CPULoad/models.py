from django.db import models

class InstantLoad(models.Model):
    cpu_load = models.CharField(max_length=255, verbose_name='Моментальная загрузка процессора')
    time = models.CharField(max_length=255, verbose_name="Время")

class AverageLoad(models.Model):
    cpu_load = models.CharField(max_length=255, verbose_name='Усредненная загрузка процессора')
    time = models.CharField(max_length=255, verbose_name="Время")