from movies import Movie
from theaters import Theater
import utility

class Showtime:
    def __init__(self, movie: Movie, theater: Theater, datetime: str):
        self.movie = movie
        self.theater = theater
        self.datetime = datetime

    @property
    def movie(self) -> Movie:
        return self._movie

    @movie.setter
    @utility.type_checking(Movie)
    def movie(self, new_movie: Movie):
        self._movie = new_movie

    @property
    def theater(self) -> Theater:
        return self._theater

    @theater.setter
    @utility.type_checking(Theater)
    def theater(self, new_theater: Theater):
        self._theater = new_theater

    @property
    def datetime(self) -> str:
        return self._datetime

    @datetime.setter
    @utility.type_checking(str)
    def datetime(self, new_datetime: str):
        self._datetime = new_datetime
