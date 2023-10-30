from abc import ABC, abstractmethod
from typing import List
from showtimes import Showtime
from movies import Movie

class MovieTheater(ABC):
    @abstractmethod
    def browse_movies(self):
        pass

    @abstractmethod
    def browse_showtimes(self):
        pass

    @abstractmethod
    def reserve_seats(self, showtime: Showtime, seats: List[int]):
        pass

    @abstractmethod
    def purchase_tickets(self, showtime: Showtime, seats: List[int]):
        pass

class MovieTheaterSystem(MovieTheater):
    def __init__(self):
        self._movies: List[Movie] = []
        self._showtimes: List[Showtime] = []

    def browse_movies(self):
        return self._movies

    def browse_showtimes(self):
        return self._showtimes

    def reserve_seats(self, showtime: Showtime, seats: List[int]):
        pass

    def purchase_tickets(self, showtime: Showtime, seats: List[int]):
        pass

