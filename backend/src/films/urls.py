from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.MovieList.as_view(), name='all'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='detail'),
]