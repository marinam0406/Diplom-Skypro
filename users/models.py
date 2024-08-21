from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''
    User model with email field and abstract user fields.
    '''
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        '''
        Meta options for the User model.
        '''
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
