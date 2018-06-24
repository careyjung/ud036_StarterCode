import csv
import fresh_tomatoes
import media

# read my favorite movies in from a '|'-separated csv file
movies = list()
with open('favorite_movies.csv') as csvfile:

    # DictReader treats first row as fieldnames. Result is an ordered dict.
    moviereader = csv.DictReader(csvfile, delimiter='|')
    for row in moviereader:
        movies.append(media.Movie(**row))

fresh_tomatoes.open_movies_page(movies)
