from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)
