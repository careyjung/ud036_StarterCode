import webbrowser


class Movie():
    """
    Simple Movie class to track favorite movies
    """

    # constructor
    def __init__(self, title, poster, trailer, storyline):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    # show the Youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)
