from django.db import models
from django.contrib.auth import get_user_model


class Chat(models.Model):
    messagem = models.CharField(max_length=254)
    hour = models.CharField(max_length=4)
    data = models.DateField(null=True)
    sender = models.ForeignKey(get_user_model(), related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), related_name='receiver', on_delete=models.DO_NOTHING)
