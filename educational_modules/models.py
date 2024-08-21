from django.db import models


class EduModel(models.Model):
    number = models.IntegerField(unique=True, db_index=True, verbose_name='Номер модели')
    name = models.CharField(max_length=30, unique=True, db_index=True, verbose_name='Название модели')
    description = models.TextField(verbose_name='Описание модели')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        ordering = ['number',]
