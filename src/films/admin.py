from django.contrib import admin
from .models import Actor, Genre, Director, Movie, Writer


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Writer)
admin.site.register(Movie)