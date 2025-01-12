from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
movies_list = {
    'harrypotter': 'Harry Potter je čaroděj.',
    'mortalcombat': 'Mortal Combat je zvláštní film.',
    'smrtvdesti': 'Smrt v dešti je arabská detektivka.',
}

def allmovies_text(request, moviename):
    try:
        movie_info = movies_list[moviename]
        return HttpResponse(movie_info)
    except:
        return HttpResponseNotFound('Film nenalezen.')


def allmovies_number(request, movienumber):    
    movies_names_list = list(movies_list.keys())
    
    if movienumber > len(movies_names_list):
        return HttpResponseNotFound('Film nebyl nalezen.')

    current_movie = movies_names_list[movienumber - 1]
    redirect_url = reverse('movie_url', args=[current_movie])
    return HttpResponseRedirect(redirect_url)
