"""
Script that will fill the database with cult classic films from the wikipedia page
"""
from string import ascii_uppercase
import movie_titles


base_link = 'https://en.wikipedia.org/wiki/List_of_cult_films:_'
titles = []
for char in ascii_uppercase:
    webpage = base_link + char
    titles.append(movie_titles.get_titles(webpage)['nice'])

for thing in titles:
    for movie in thing:
        print(movie)