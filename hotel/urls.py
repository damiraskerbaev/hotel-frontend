from django.urls import path

from .views import (
    home_page, 
    hotel_list, 
    hotel_detail, 
    hotel_create, 
    hotel_edit, 
    hotel_delete)

urlpatterns = [
    path('', home_page, name='home_page'),
    path('hotels/', hotel_list, name='hotel_list'),
    path('hotels/<int:pk>/', hotel_detail, name='hotel_detail'),
    path('hotels/new/', hotel_create, name='hotel_create'),
    path('hotels/edit/<int:pk>/', hotel_edit, name='hotel_edit'),
    path('hotels/delete/<int:pk>/', hotel_delete, name='hotel_delete')
]