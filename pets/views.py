from rest_framework import viewsets
from rest_framework.response import Response

from pets.models import Pet
from pets.serializer import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    #queryset = Pet.objects.all()
    #serializer_class = PetSerializer
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()
        codColeira = self.request.query_params.get("codColeira")
        if codColeira is not None:
            queryset = Pet.objects.filter(codColeira=codColeira)
        return queryset
