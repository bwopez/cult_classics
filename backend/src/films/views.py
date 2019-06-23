from django.shortcuts import render
from django.views import generic

from . import models


class MovieList(generic.ListView):
    model = models.Movie


class MovieDetailView(generic.DetailView):
    context_object_name = 'movie_detail'
    model = models.Movie
