from django.urls import path
from . import views
from django_filters.views import FilterView
from .filters import MovieFilter


app_name = 'movies'

urlpatterns = [
    # path('', views.MovieList.as_view(), name='all'),
    path('search/', FilterView.as_view(filterset_class=MovieFilter,
                                       template_name='films/movie_list.html'),
                                       name='search'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='detail'),
]