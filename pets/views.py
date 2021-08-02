from rest_framework import viewsets
from pets.models import Pet
from pets.serializer import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer