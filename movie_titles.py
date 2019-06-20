"""
Script to get all movies from a web page
"""
from bs4 import BeautifulSoup as bs
import requests
import csv


def get_titles(webpage):
    """
    A function to get the titles from a wikipedia webpage that was passed in.
    This was an ad-hoc script to get all the movies from the Cult Classic Films table,
    there are no guarantees that this will work on any other wikipedia page let alone web page.

    :param webpage: A link to the wikipedia webpage that has movies to scrape

    :return: all titles from the wikipedia table
    """
    page = requests.get(webpage)
    soup = bs(page.text, 'html.parser')

    table = soup.find('table', {'class': 'wikitable'})
    titles = []
    for tr in table.find_all('tr')[1:]:
        movie = []
        movie_obj = dict()
        for td in tr.find_all('td'):
            movie.append(td.get_text().strip())
        if '(' in movie[0]:
            movie_obj['name'] = movie[0].split('(')[0]
        else:
            movie_obj['name'] = movie[0]
        movie_obj['year'] = movie[1]
        movie_obj['directors'] = movie[2]
        titles.append(movie_obj)

    return titles


if __name__ == '__main__':
    print("Doing a trial run. Grabbing all titles from 'cult classics: C'")
    my_titles = get_titles('https://en.wikipedia.org/wiki/List_of_cult_films:_C')
    print("Titles have been loaded. Printing titles")
    print("========================================")
    print("========================================")
    print("========================================")
    for title in my_titles:
        if len(title['year']) == 4:
            print(title['name'] + " || " + title['year'] + " || " + title['directors'])
        else:
            file = 'trash_can.csv'
            f = open(file, 'w+')
            f.write(title['name'] + " || " + title['year'] + " || " + title['directors'])
            f.write('\n')