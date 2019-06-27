import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

import django
django.setup()

from films.models import Actor, Genre, Director, Movie
from slugify import slugify
import urllib.request


def downloader(movie):
    file_name = slugify(movie.name + str(movie.year) + ".jpg")
    urllib.request.urlretrieve(movie.cover_url, file_name)
    return file_name