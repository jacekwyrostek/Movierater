from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def movieList(request):
    movies=Movie.objects.all()
    return render(request, 'movie_list.html',{'movies':movies})

def addMovie(request):
    form=MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(movieList)
    return render(request, 'new_movie.html', {'form':form})
