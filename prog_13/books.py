from abc import ABC, abstractmethod
from typing import List, Union
import utility

class Book(ABC):
    def __init__(self, title: str, author: str, publication_date: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.available = True

    @abstractmethod
    def get_book_type(self) -> str:
        pass

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    @utility.type_checking(str)
    def title(self, title: str) -> None:
        self._title = title

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    @utility.type_checking(str)
    def author(self, author: str) -> None:
        self._author = author

    @property
    def publication_date(self) -> str:
        return self._publication_date

    @publication_date.setter
    @utility.type_checking(str)
    def publication_date(self, publication_date: str) -> None:
        utility.check_data(publication_date)
        self._publication_date = publication_date

    @property
    def available(self) -> bool:
        return self._available

    @available.setter
    @utility.type_checking(bool)
    def available(self, available: bool) -> None:
        self._available = available

class Fiction(Book):
    def get_book_type(self) -> str:
        return "Fiction"

class NonFiction(Book):
    def get_book_type(self) -> str:
        return "Non-Fiction"
