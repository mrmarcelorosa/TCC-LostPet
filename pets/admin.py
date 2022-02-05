from django.contrib import admin
from pets.models import Pet


class Pets(admin.ModelAdmin):
    list_display = ('id', 'nome', 'raca')
    search_fields = ('id','nome')


admin.site.register(Pet, Pets)
# Register your models here.
