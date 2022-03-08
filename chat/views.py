from rest_framework import viewsets
from chat.models import Chat
from chat.serializer import ChatSerializer

# Create your views here.


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
