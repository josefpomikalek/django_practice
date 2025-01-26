from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, 'netflix/index.html')

def all_movies_page(request):
    return render(request, 'netflix/all_movies.html')

