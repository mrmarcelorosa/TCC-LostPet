from django.contrib import admin
from chat.models import Chat


class Chats(admin.ModelAdmin):
    list_display = ('id', 'sender')
    search_fields = ('id', 'sender')


admin.site.register(Chat, Chats)
