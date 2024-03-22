from django.contrib.admin import *

from .models import Room

@register(Room)

class RoomAdmin(ModelAdmin):

    list_display = ('id', 'number', 'price_per_night')
    list_display_links = ('id', 'number', 'price_per_night')