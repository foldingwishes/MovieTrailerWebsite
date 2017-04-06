"""Holds the Movie class, used to hold data pertinent to a film."""

import webbrowser


class Movie:
    """Movie object that holds data regarding a particular film."""

    def __init__(self, title, image, movie_tagline="", trailer_url=""):
        """Init an instance of Movie.

        Args:
            title: Title of the movie.
            image: Full url of the movie's poster image.
            movie_tagline: The plot summary of the movie.
            trailer_url: The url for the movie's trailer on Youtube.
        """
        self.title = title
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url
        self.storyline = movie_tagline

    def show_trailer(self):
        """Open the movie's trailer in a new browser."""
        webbrowser.open(self.trailer_youtube_url)

    def debug_print(self):
        """Print to the console the instance's attributes.

        Used to conveniently check the values of each attribute.
        Include title, storyline, poster_image_url and
        trailer_youtube_url.
        """
        print self.title
        print self.storyline
        print self.poster_image_url
        print self.trailer_youtube_url
        print "------"
