"""
Script that will fill csv files with cult classic films from the wikipedia page
"""
from string import ascii_uppercase
import movie_titles


def encode_to_utf8(string_to_encode):
    """
    Encodes a string that is passed in

    :param string_to_encode: the string that needs to be 'utf-8' encoded
    :return: the string that is 'utf-8' encoded
    """
    return string_to_encode.encode('utf8')


def write_to_file(file_name, string):
    """
    This appends the string as a line to a file

    :param file_name: the file that you would like to write to
    :param string: the line that you would like to append to file
    :return: no return
    """
    f = open(file_name, 'ab+')
    f.write(encode_to_utf8(string))
    f.write(encode_to_utf8('\n'))
    f.close()


if "__name__" == "__main__":
    base_link = 'https://en.wikipedia.org/wiki/List_of_cult_films:_'
    titles = []
    for char in ascii_uppercase:
        webpage = base_link + char
        titles.append(movie_titles.get_titles(webpage))

    for movie_obj in titles:
        for title in movie_obj:
            if len(title['year']) == 4:
                file = 'csv/almost_all_titles.csv'
                movie_string = title['name'].strip() + "," + title['year'].strip() + "," + title['directors'].strip()
                write_to_file(file, movie_string)
                print(movie_string)
            else:
                file = 'csv/troublesome_titles.csv'
                movie_string = title['name'].strip() + "," + title['year'].strip() + "," + title['directors'].strip()
                write_to_file(file, movie_string)
