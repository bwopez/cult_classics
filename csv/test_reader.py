# TODO: probably split the 'everything_except_zatoichi.csv' file into alphabetized lists to prevent throttling
import csv
import imdb
ia = imdb.IMDb()


def encode_to_utf8(string_to_encode):
    return string_to_encode.encode('utf8')


# def write_to_file(file_name, string):
#     f = open(file_name, 'ab+')
#     f.write(encode_to_utf8(string))
#     f.write(encode_to_utf8('\n'))
#     f.close()


def find_movie(movie_list, correct_title, correct_year):
    for return_movie in movie_list:
        if ('movie' in return_movie['kind'] or return_movie['kind'] == 'short') and 'year' in return_movie.keys():
            if 'akas' in return_movie.keys():
                if int(correct_year) == return_movie['year'] or correct_title in return_movie['akas']:
                    return return_movie
            else:
                if int(correct_year) == return_movie['year']:
                    return return_movie

    print("Couldn't find a good fit, returning the first title.")
    for return_movie in movie_list:
        if 'movie' in return_movie['kind']:
            return return_movie


if __name__ == "__main__":
    with open('test.csv', encoding="utf8") as csvfile:
        readcsv = csv.reader(csvfile, delimiter='|')
        for row in readcsv:
            title = row[0]
            year = row[1]

            # tv show
            show_titles = [
                "Ironiya Sudby, ili S Lyogkim Parom!",
                "Dekalog",
                "The Firm",
                "Kite",
            ]

            # porn
            porn_titles = [
                "No Skin Off My Ass",
                "Alice in Wonderland: An X-Rated Musical Fantasy",
                "Behind the Green Door",
                "Café Flesh",
                "Deep Throat",
                "Thundercrack!",
            ]
            if title in show_titles or title in porn_titles:
                print("passing this one: " + title)
                continue
            else:
                movies = ia.search_movie(title)
                if len(movies):
                    movie = find_movie(movies, title, year)
                    ia.update(movie)

                    if 'movie' in movie['kind'] or movie['kind'] == 'short':
                        print(movie['title'] + "|" + str(movie['year']) + "|" + movie['directors'][0]['name'])
                    else:
                        print("Couldn't find a movie for " + title)
                else:
                    print("Lost title:  " + title)