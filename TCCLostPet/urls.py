from django.contrib import admin
from django.urls import path, include
from pets.views import PetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('accounts.urls')),
]
