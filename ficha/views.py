from rest_framework import viewsets
from ficha.models import Ficha
from ficha.serializer import FichaSerializer

# Create your views here.
class FichaViewSet(viewsets.ModelViewSet):
    #queryset = Ficha.objects.all()
    serializer_class = FichaSerializer

    def get_queryset(self):
        queryset = Ficha.objects.all()
        pet = self.request.query_params.get("pet")
        if pet is not None:
            queryset = Ficha.objects.filter(pet=pet)
        return queryset