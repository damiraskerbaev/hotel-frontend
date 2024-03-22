from django.contrib.admin import *

from .models import Booking

@register(Booking)

class BookingAdmin(ModelAdmin):

    list_display = ('id', 'room', 'guest')
    list_display_links = ('id', 'room', 'guest')