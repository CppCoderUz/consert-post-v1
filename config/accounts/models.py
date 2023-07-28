from django.db import models
from django.contrib.auth.models import AbstractUser





class User(AbstractUser):

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} ({self.username})'


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = '1. Userlar'