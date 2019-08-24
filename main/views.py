from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def movieList(request):
    text='this text from views'
    movies=['Avatar','Titanic','American Sniper']
    return render(request, 'movie_list.html',{'text':text, 'movies':movies})
