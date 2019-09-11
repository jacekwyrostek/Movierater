from django.contrib import admin
from django.urls import path, include
from .views import movieList, addMovie, editMovie, deleteMovie

urlpatterns = [
    path('list/', movieList, name='movieList'),
    path('add/', addMovie, name='addMovie'),
    path('edit/<int:id>', editMovie, name='editMovie'),
    path('delete/<int:id>', deleteMovie, name='deleteMovie'),
]
