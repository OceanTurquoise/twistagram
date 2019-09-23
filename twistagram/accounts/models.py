from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    icon = models.ImageField(upload_to="image/", blank=True, null=True)

    def get_absolute_url(self):
        return reverse(
        'ginstagram:profile', kwargs={'username': self.username})
