from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User for Gale which inherits the inbuilt Django User Model
class User(AbstractUser):

    is_manager = models.BooleanField(
        default=False,
        verbose_name='Are you a manager?'
    )

    def __str__(self):
        return self.user.username or ''

    class Meta:
        verbose_name = 'Gale User'
        verbose_name_plural = 'Gale Users'
