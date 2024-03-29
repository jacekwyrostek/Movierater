from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


def movieList(request):
    movies=Movie.objects.all()
    return render(request, 'movie_list.html',{'movies':movies})

@login_required
def addMovie(request):
    form=MovieForm(request.POST or None, request.FILES or None,)
    if form.is_valid():
        form.save()
        return redirect(movieList)
    return render(request, 'movie_form.html', {'form':form})

@login_required
def editMovie(request, id):
    movie=get_object_or_404(Movie, pk=id)
    form=MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect(movieList)
    return render(request, 'movie_form.html', {'form':form})

@login_required
def deleteMovie(request, id):
    movie=get_object_or_404(Movie, pk=id)
    if request.method=='POST':
        movie.delete()
        return redirect(movieList)
    return render(request, 'delete_movie.html', {'movie':movie})
