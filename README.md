# Source Code for a Movie Trailer website

## Overview

This is the source code for a basic movie trailer website, derived
from [my fork](https://github.com/careyjung/udacity_movie_site) of
Udacity's [starter
code](https://github.com/udacity/ud036_StarterCode).

My implementation is basically the same as presented in the Udacity
course, with one enhancement: instead of populating my 'database' of
favorite movies in-line in the code, I stored them all in a |-separated CSV file,
`favorite_movies.csv`, and I then use the Python `csv` module to read them
into memory.

The first row of my CSV file defines the field names for the file, as such:
```
title|poster|trailer|storyline
Schindler's List|...|...|...
Pulp Fiction|...|...|...
```

These field names match the parameter keywords of my `Movie` constructor:
```
def __init__(self, title, poster, trailer, storyline):
```

By reading the file with a `csv.DictReader`, I am thus able to create
new `Movie` objects very succinctly, by simply reading them into an `OrderedDict`
and unpacking it:

```
movies = list()
with open('favorite_movies.csv') as csvfile:
    moviereader = csv.DictReader(csvfile, delimiter='|')
    for row in moviereader:
        movies.append(media.Movie(**row))
```


The advantages of this approach:
* The CSV file is self-documenting
* I can lay out the fields in the CSV file in any order I choose
* CSV fieldnames and Movie constructor parameters are cross-checked: If they don't match, an exception is thrown
* My code becomes very succint: read a row, unpack it, repeat





