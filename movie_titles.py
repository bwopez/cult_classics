"""
Script to get all movies from a web page
"""
from bs4 import BeautifulSoup as bs
import requests
import wikipedia
import re


def get_year(title, lang='en'):
    """

    :param title:
    :param lang:
    :return:
    """
    wikipedia.set_lang(lang)
    summary = wikipedia.WikipediaPage(title=title).summary
    match = re.search('\d{4}', summary)
    if match:
        year = match.group(0)
    else:
        year = "unknown"
    return year


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
    for italic in table.find_all('i'):
        if italic.find('a'):
            title = italic.find('a')['title']
            language = 'en'
            match = re.search('[a-z][a-z]:', title)
            if match and match.group(0) == title[:len(match.group(0))]:
                language, title = title.split(match.group(0)[-1])
            year = get_year(title, language)

            title = year + '||' + title
            if '(' in title:
                title = title.split('(')[0]

            titles.append(title)
            print(title)

    return titles


if __name__ == '__main__':
    print("Doing a trial run. Grabbing all titles from 'cult classics: C'")
    my_titles = get_titles('https://en.wikipedia.org/wiki/List_of_cult_films:_C')
    # print("Titles have been loaded. Printing titles")
    # print("========================================")
    # print("========================================")
    # print("========================================")
    # for year_title in my_titles:
    #     print(year_title)
