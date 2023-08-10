from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Microservice(models.Model):
    title = models.CharField(max_length=255)
    http_methods = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
