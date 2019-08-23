from django.contrib import admin
from .models import Movie
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields=('name','description', 'year')
    list_display=('name', 'year','imdbRating')
    list_filter=('year','imdbRating')
    search_fields=('name', 'year')
