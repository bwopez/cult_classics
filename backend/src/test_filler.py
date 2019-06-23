import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

import django
django.setup()

from films.models import Actor, Genre, Director, Movie

if __name__ == "__main__":
    json_file = open('../../json/movie_time.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)

    for obj in json_data:
        movie_name = obj['title']
        movie_year = obj['year']
        movie_runtime = 0
        if 'runtimes' in obj.keys():
            movie_runtime = int(obj['runtimes'][0])
        if 'rating' in obj.keys():
            movie_rating = float(obj['rating'])
        if 'cover url' in obj.keys():
            movie_cover_url = obj['cover url']
        if 'plot outline' in obj.keys():
            movie_plot_outline = obj['plot outline']

        movie_cast = set()
        movie_directors = set()
        movie_genres = set()
        if 'cast' in obj.keys():
            for person in obj['cast']:
                movie_cast.add(person)
        if 'directors' in obj.keys():
            for person in obj['directors']:
                movie_directors.add(person)
        if 'genres' in obj.keys():
            for genre in obj['genres']:
                movie_genres.add(genre)

        # adding the actors, directors, genres
        print("Creating movie: " + movie_name)
        my_movie = Movie.objects.get_or_create(name=movie_name, year=movie_year,
                                               runtime=movie_runtime, rating=movie_rating,
                                               cover_url=movie_cover_url, plot_outline=movie_plot_outline)[0]
        print("Successfully created movie: " + movie_name)
        for actor_name in movie_cast:
            actor = Actor.objects.get_or_create(name=actor_name)[0]
            my_movie.cast.add(actor)
        print("Added actors.")

        for director_name in movie_directors:
            director = Director.objects.get_or_create(name=director_name)[0]
            my_movie.directors.add(director)
        print("Added directors")

        for genre_name in movie_genres:
            genre = Genre.objects.get_or_create(name=genre_name)[0]
            my_movie.genres.add(genre)
        print("Added genres")