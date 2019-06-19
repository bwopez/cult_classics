"""
Script to gather information about a specific movie title
"""
import imdb
ia = imdb.IMDb()


def get_movie_info(movie_title):
    """
    Function that gathers all information needed for the database that I was creating.
    The movie_info object has a few keys that will be used to fill each column in the database.

    ['director']    - the director of the movie
    ['description'] - the imdb description of the movie (may contain spoilers)
    ['poster']      - the movie poster image on imdb
    ['genres']      - a list of genres listed on imdb
    ['plot']        - a fan made single sentence plot description
    ['year']        - year released
    ['rating']      - star rating out of 10

    :param movie_title: title of the movie to be searched on imdb

    :return: movie_title object

    """
    movie = ia.search_movie(movie_title)[0]
    ia.update(movie)

    movie_info = dict()
    movie_info['director'] = movie['director'][0]['name']
    movie_info['description'] = movie['plot outline']
    movie_info['poster'] = movie['cover url']
    movie_info['genres'] = movie['genres']
    movie_info['plot'] = movie['plot'][0].split('::')[0]
    movie_info['year'] = movie['year']
    movie_info['rating'] = movie['rating']

    return movie_info


if __name__ == '__main__':
    print('Getting test information from movie "Akira"')
    my_movie = get_movie_info('Akira')
    print(my_movie['director'])
    print(my_movie['poster'])
    print(my_movie['plot'])
    # TODO: need to parse this into an int to compare vvv
    print(my_movie['year'])
    # TODO: need to find a float model field vvv
    print(my_movie['rating'])

    # TODO: is there even a model field for lists? vvvv
    for genre in my_movie['genres']:
        print(genre)
