from django.db import models
from pets import models as pet_model
# Create your models here.
class Ficha(models.Model):
    tipo_choice = (
        ('v', 'vacina'),
        ('p', 'procedimento cirurgico'),
        ('c', 'cuidados')
    )
    nome = models.CharField(max_length=40)
    tipo = models.CharField(max_length=1, choices=tipo_choice, null=True)
    data = models.DateField(null=True)
    pet = models.ForeignKey(pet_model.Pet, on_delete=models.CASCADE)