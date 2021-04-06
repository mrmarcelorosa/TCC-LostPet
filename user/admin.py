from django.contrib import admin
from user.models import User


class Users(admin.ModelAdmin):
    list_display = ('id', 'name', 'tel')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(User, Users)
