from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('name', max_length=40)
    tel = models.BigIntegerField('tel')
    password = models.CharField('password', max_length=10)
