from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('book/', views.book_room, name='book_room'),
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('rooms/', views.room_list, name='room_list'),
]
