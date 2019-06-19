"""
Script to get all movies from a web page
"""
from bs4 import BeautifulSoup as bs
import requests


def get_titles(webpage):
    """
    A function to get the titles from a wikipedia webpage that was passed in.
    This was an ad-hoc script to get all the movies from the Cult Classic Films table,
    there are no guarantees that this will work on any other wikipedia page let alone web page.
    The all_titles object has two attributes that need to be explained

    ['nice']    - titles that worked well with the script
    ['naughty'] - titles that didn't work well with the script
                    ie. the years are formatted different or it is a series
                    not to be misinterpreted as titles of 18+ movies

    :param webpage: A link to the wikipedia webpage that has movies to scrape

    :return: Object with ['nice'] titles that worked well with script and ['naughty'] titles that didn't
    """
    page = requests.get(webpage)
    soup = bs(page.text, 'html.parser')

    table = soup.find('table', {'class': 'wikitable'})
    all_titles = dict()
    titles = []
    troublesome_titles = []
    for italic in table.find_all('i'):
        if italic.find('a'):
            title = italic.find('a')['title']
            if 'l:' in title:
                title = title.split('l:')[1].strip()
            year = italic.findNext('td').get_text().strip()
            title = year + '||' + title
            if '(' in title:
                title = title.split('(')[0]

            if len(year) == 4 and '-' not in year:
                titles.append(title)
            else:
                troublesome_titles.append(title)

    all_titles['nice'] = titles
    all_titles['trouble'] = troublesome_titles

    return all_titles


if __name__ == '__main__':
    print("Doing a trial run. Grabbing all titles from 'cult classics: A'")
    my_titles = get_titles('https://en.wikipedia.org/wiki/List_of_cult_films:_W')
    print("Titles have been loaded. Printing titles")
    print("========================================")
    print("========================================")
    print("========================================")
    for year_title in my_titles:
        print(year_title)