from django.contrib import admin
from django.urls import path, include
from .views import movieList

urlpatterns = [
    path('list/', movieList)
]
