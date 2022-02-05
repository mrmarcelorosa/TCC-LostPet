from django.db import models
from django.contrib.auth import get_user_model

class Pet(models.Model):
    porte_choice= (
        ('p', 'pequeno'),
        ('m', 'médio'),
        ('g', 'grande')
    )
    sexo_choice = (
        ('m', 'macho'),
        ('f', 'fêmea')
    )

    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=40)
    raca = models.CharField(max_length=20)
    codColeira = models.CharField(max_length=40)
    dataNascimento = models.DateField(null=True)
    castrado = models.BooleanField(default=False)
    porte = models.CharField(max_length=1, choices=porte_choice,null=True)
    sexo = models.CharField(max_length=1,choices=sexo_choice,null=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
