import utility
from abc import ABC, abstractmethod

class GenreType(ABC):
    @abstractmethod
    def display(self) -> str:
        ...

class ACTION(GenreType):
    def display(self) -> str:
        return "ACTION"

class COMEDY(GenreType):
    def display(self) -> str:
        return "COMEDY"

class DRAMA(GenreType):
    def display(self) -> str:
        return "DRAMA"

class Movie:
    def __init__(self, title: str, genre: GenreType, rating: int) -> None:
        self.title = title
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"title: {self.title}, genre: {self.genre.display()}, rating: {self.rating}"

    def __eq__(self, other):
        return (
            self.title == other.title and
            self.genre.display() == other.genre.display() and
            self.rating == other.rating
        )

    @property
    def title(self):
        return self._title

    @title.setter
    @utility.check_str_data
    def title(self, new_title):
        self._title = new_title

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, new_genre):
        if isinstance(new_genre, GenreType):
            self._genre = new_genre
        else:
            raise ValueError("Genre must be a GenreType")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, int) and 0 <= new_rating <= 10:
            self._rating = new_rating
        else:
            raise ValueError("Rating must be an integer between 0 and 10")

def main():
    type_m = ACTION()
    m = Movie("ddd", type_m, 5)
    print(m)

if __name__ == "__main__":
    main()

