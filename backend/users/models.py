from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import username_validator


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True,
        validators=[username_validator]
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
    )
    created = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='account_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='account_user_permissions'
    )
