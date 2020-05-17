from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True, unique=True, help_text='Email Address')
    phone_no = models.CharField(unique=True, null=False, max_length=10, help_text='Phone Number')

    def __str__(self):
        return self.phone_no
