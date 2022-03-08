from django.contrib import admin
from django.urls import path, include
from pets.views import PetViewSet
from rest_framework import routers
from ficha.views import FichaViewSet
from chat.views import ChatViewSet

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'pets', PetViewSet, basename='Pet')
router.register(r'fichas', FichaViewSet, basename='Ficha')
router.register(r'chats', ChatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('accounts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
