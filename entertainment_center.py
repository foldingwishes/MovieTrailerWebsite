"""Generate a website based on a list of favorite movies.

Args:
    movielist: A list of movie titles represented as strings.
    KEY: Holds authorization key to access YouTube's data API
"""

import json
from urllib2 import Request, URLError, urlopen

import fresh_tomatoes

import media


movielist = ["Back to the Future",
             "The Girl who Leapt Through TIme",
             "Scott Pilgrim vs. the World",
             "Treasure Planet",
             "To Kill a Mockingbird",
             "Rope",
             "Sunset Boulevard",
             "It's a Wonderful Life",
             "Easy A",
             "Nonexistent Movie",
             "La La Land",
             "Le Grand Chef"]

KEY = "AIzaSyBxeJgtp2KTy-dWTC1mcFW3AlwHg0WUYvc"


def populate_list(movies, debug_on=False):
    """Init an instance of Movie.

    By iterating over the array of strings in argument movies
        a new array of Movie object instances is generated.
        For each movie, the OMDB (Open Movie DataBase) and YouTube
        are called to pull the needed data. If the data is not found,
        a default substitute is used for the item instead.

    Args:
        movies: A list of movie titles represented as strings.
        debug_on: Whether the console should print the collected
            data for each instantiated Movie object.

    Returns:
        An array of instances of class Movie.

    Raises:
        URLError: HTTP request for a webpage did not go through.
        DataError: Requested object not found on web server.
    """
    global KEY
    movie_objects = []

    # Go through each title to find and generate each movie instance.
    for i in range(0, len(movies)):
        query = movies[i].replace(" ", "+")
        movie_exists = False

        # Search OMDB site to obtain data and initialize Movie object.
        request = Request('http://www.omdbapi.com/?t=%s' % query)
        try:
            response = urlopen(request)
            data = json.loads(response.read())
            # if data obtained successfully, initialize with data.
            if data.get("Title"):
                movie_objects.append(
                    media.Movie(data["Title"],
                                data["Poster"],
                                data["Plot"])
                )
                movie_exists = True
            # On failure to retrieve data,
            # initialize Movie object with set default values.
            else:
                movie_objects.append(
                    media.Movie(
                        movies[i],
                        "images/notFound.png",
                        "Movie Data not found: %s" % movies[i],
                        "https://www.youtube.com/watch?v=GfAnyT9QitU"
                    )
                )
                print ('DataError: could not find movie "%s" in database'
                       % movies[i])
        # On failure to connect to the OMDB site,
        # initialize Movie object with set default values
        # and notify of URL error.
        except URLError, e:
            movie_objects.append(
                media.Movie(
                    movies[i],
                    "images/notFound.png",
                    "Movie Data not found: %s" % movies[i],
                    "https://www.youtube.com/watch?v=GfAnyT9QitU"
                )
            )
            print 'URLError: could not access site.', e

        # If the data was collected successfully,
        # proceed with collection of trailer url.
        if movie_exists:
            video = Request(
                'https://www.googleapis.com/youtube/v3/search?part=id&q=' +
                query +
                '+trailer&max-results=1&key=' + KEY)
            # Search YouTube to obtain trailer url.
            try:
                response = urlopen(video)
                vid_data = json.loads(response.read())
                video = vid_data['items'][0]
                movie_objects[i].trailer_youtube_url = (
                    "https://www.youtube.com/watch?v=" +
                    video['id']['videoId'])
            # On failure to connect to YouTube,
            # set trailer url to default.
            except URLError, e:
                movie_objects[i].trailer_youtube_url = (
                    "https://www.youtube.com/watch?v=GfAnyT9QitU")
                print ('URLError: Could not access site'
                       'to retrieve video:', e)

        # If debug flag set to True,
        # print the new Movie instance's data to console.
        if debug_on:
            movie_objects[i].debug_print()

    return movie_objects


def print_movielist():
    """Print out all of the movie titles currently stored."""
    global movielist
    print "Movies: "
    for title in movielist:
            print "- %s" % title
    print "------------------------"


def generate_site(movies, debug=False):
    """Generate a website based on a list of movies.

    Args:
        movies: A list of movie titles represented as strings.
        debug: Whether the console should print the collected
            data for each instantiated Movie object.
    """
    site_data = populate_list(movies, debug)
    fresh_tomatoes.open_movies_page(site_data)


# -------------------------------------------
# Uncomment last line and run module to generate site.

# generate_site(movielist, True)
