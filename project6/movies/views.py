from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, 'movies/index.html')


def all_movies(request):
    return render(request, 'movies/all-movies.html')


def movie_detail(request):
    return render(request, 'movies/movie-detail.html')

