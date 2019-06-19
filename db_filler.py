"""
Script that will fill the database with cult classic films from the wikipedia page
"""
from string import ascii_uppercase
import movie_titles
import imdb_info


base_link = 'https://en.wikipedia.org/wiki/List_of_cult_films:_'
titles = []
for char in ascii_uppercase:
    webpage = base_link + char
    titles.append(movie_titles.get_titles(webpage))

# for thing in titles:
#     for movie in thing:
#         print(movie)
        # year, title = movie.split('||')
        # info = imdb_info.get_movie_info(title, int(year))
        # print(title, info['director'])