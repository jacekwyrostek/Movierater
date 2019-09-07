from django.contrib import admin
from django.urls import path, include
from .views import movieList, addMovie, editMovie

urlpatterns = [
    path('list/', movieList),
    path('add/', addMovie),
    path('edit/<int:id>', editMovie),
]
