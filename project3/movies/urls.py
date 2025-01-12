# URLS v aplikaci
from django.urls import path
from . import views

urlpatterns = [
    path('<int:movienumber', views.allmovies_number),
    path('<str:moviename>', views.allmovies_text),
]
