from rest_framework import viewsets
from ficha.models import Ficha
from ficha.serializer import FichaSerializer

# Create your views here.
class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer