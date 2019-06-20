"""
Script to gather information about a specific movie title
"""
import imdb
ia = imdb.IMDb()


def find_movie(movie_list, year):
    """
    Function to return the first instance of a movie that matches the year from wikipedia

    :param movie_list: A list of movies from imdb
    :param year: The year the movie was released according to wikipedia
    :return: The first instance of a movie that was released the same year as wikipedia's year
    """
    for curr_movie in movie_list:
        try:
            if curr_movie['kind'] == 'movie' and curr_movie['year'] == year:
                return curr_movie
        except KeyError:
            print("This maybe isn't a movie: ", curr_movie)


def fill_field(info, film, field, key):
    if field == 'director':
        info[field] = film[key][0]['name']
    elif field == 'plot':
        info[field] = film[key][0].split('::')[0]
    else:
        info[field] = film[key]


def get_movie_info(movie_title, year):
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
    :param year: year the movie was released in according to wikipedia
    :return: movie_title object
    """
    movies = ia.search_movie(movie_title)
    movie = find_movie(movies, year)
    try:
        ia.update(movie)
    except imdb._exceptions.IMDbError:
        print("Cannot find this movie on imdb: " + movie_title)

    movie_info = dict()
    try:
        fill_field(movie_info, movie, 'director', 'director')
        fill_field(movie_info, movie, 'poster', 'cover url')
        fill_field(movie_info, movie, 'genres', 'genres')
        fill_field(movie_info, movie, 'plot', 'plot')
        fill_field(movie_info, movie, 'year', 'year')
        fill_field(movie_info, movie, 'rating', 'rating')
    except:
        movie_info['director'] = 'did not work correctly'

    return movie_info


if __name__ == '__main__':
    print('Getting test information from movie "Akira"')
    my_movie = get_movie_info('Akira', 1988)
    print(my_movie['director'])
    print(my_movie['poster'])
    print(my_movie['plot'])
    print(my_movie['year'])
    # TODO: need to find a float model field vvv
    print(my_movie['rating'])

    # TODO: is there even a model field for lists? vvvv
    for genre in my_movie['genres']:
        print(genre)
