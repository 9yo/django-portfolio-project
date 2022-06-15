from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.number}'

class ContactBook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500, blank=True, null=True)
    contacts = models.ManyToManyField(Contact)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
