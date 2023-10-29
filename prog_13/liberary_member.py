from abc import ABC, abstractmethod
from typing import List, Union
from books import Book

class LibraryMember(ABC):
    @abstractmethod
    def search_book(self, title: str) -> Union[Book, None]:
        pass

    @abstractmethod
    def borrow_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def return_book(self, book: Book) -> None:
        pass
