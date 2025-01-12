from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.
movies_list = {
    'harrypotter': 'Harry Potter je čaroděj.',
    'mortalcombat': 'Mortal Combat je zvláštní film.',
    'smrtvdesti': 'Smrt v dešti je arabská detektivka',
}

def allmovies_text(request, moviename):
    try:
        movie_info = movies_list[moviename]
        return HttpResponse(movie_info)
    except:
        return HttpResponseNotFound('Film nebyl nalezen.')
    
