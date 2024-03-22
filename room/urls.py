from django.urls import path

from .views import (
    room_list, 
    room_detail, 
    room_create, 
    room_edit, 
    room_delete)

urlpatterns = [
    path('rooms/', room_list, name='room_list'),
    path('rooms/<int:pk>/', room_detail, name='room_detail'),
    path('rooms/new/', room_create, name='room_create'),
    path('rooms/edit/<int:pk>/', room_edit, name='room_edit'),
    path('rooms/delete/<int:pk>/', room_delete, name='room_delete')
]