from django.contrib import admin
from ficha.models import Ficha


class Fichas(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('id', 'nome')


admin.site.register(Ficha, Fichas)
