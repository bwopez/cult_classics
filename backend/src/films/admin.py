from django.contrib import admin
from .models import Actor, Genre, Director, Movie


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Movie)