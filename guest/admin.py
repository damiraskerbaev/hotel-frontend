from django.contrib.admin import *

from .models import Guest

@register(Guest)

class GuestAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')