import json
import csv
import imdb
ia = imdb.IMDb()


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


def write_to_json(movie_obj):
    my_obj = dict()
    for key in movie_obj.keys():
        my_obj[key] = movie_obj[key]

    for key in my_obj.keys():
        if type(my_obj[key]) == list:
            for i, thing in enumerate(my_obj[key]):
                my_obj[key][i] = str(thing)

    with open('movies.json', 'a+') as fp:
        json.dump(my_obj, fp)


if __name__ == "__main__":
    with open('../csv/the_rest.csv', encoding='utf8') as csvfile:
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
                print("Failure.")
                continue
            else:
                movies = ia.search_movie(title)
                if len(movies):
                    movie = find_movie(movies, title, year)
                    ia.update(movie)

                    if 'movie' in movie['kind'] or movie['kind'] == 'short':
                        print("Writing to json: " + movie['title'])
                        write_to_json(movie)
                        print("Successful.")
                    else:
                        print("Couldn't find a movie for " + title)
                        print("Failure.")
                else:
                    print("Lost title:  " + title)
                    print("Failure.")
