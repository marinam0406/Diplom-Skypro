from django.db import models


class EduModel(models.Model):
    '''
    Model for storing information about learning modules.
    '''
    number = models.IntegerField(unique=True, db_index=True, verbose_name='Номер модуля')
    name = models.CharField(max_length=30, unique=True, db_index=True, verbose_name='Название модуля')
    description = models.TextField(verbose_name='Описание модуля')

    def __str__(self):
        return self.name

    class Meta:
        '''
        Meta options for EduModel model.
        '''
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['number',]
