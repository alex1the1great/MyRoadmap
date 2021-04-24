from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True, blank=False)

    def __str__(self):
        return self.username
