from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
movies_list = {
    'harrypotter': 'Harry Potter je čaroděj.',
    'mortalcombat': 'Mortal Combat je zvláštní film.',
    'smrtvdesti': 'Smrt v dešti je arabská detektivka.',
}

def index(request):
    content = ''
    
    movies_names = list(movies_list.keys())
    content += '<ul>'
    for one_movie in movies_names:
        url = reverse('movie_url', args=[one_movie])
        content += f'<li><a href="{url}">{one_movie}</a></li>'
    content += '</ul>'
    return HttpResponse(content)


def allmovies_text(request, moviename):
    try:
        # movie_info = movies_list[moviename]
        response_data = render_to_string ('movies/movie.html')
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('Film nenalezen.')


def allmovies_number(request, movienumber):    
    movies_names_list = list(movies_list.keys())
    
    if movienumber > len(movies_names_list):
        return HttpResponseNotFound('Film nebyl nalezen.')

    current_movie = movies_names_list[movienumber - 1]
    redirect_url = reverse('movie_url', args=[current_movie])
    return HttpResponseRedirect(redirect_url)
