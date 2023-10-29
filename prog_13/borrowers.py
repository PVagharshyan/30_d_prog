from liberary_member import LibraryMember
from books import Book
from typing import List, Union
from info import Info
import utility
import copy

class Borrower(LibraryMember):
    def __init__(self, name: str, contact_info: Info):
        self.name = name
        self.contact_info = contact_info
        self._borrowing_history: List[Book] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, name: str) -> None:
        self._name = name

    @property
    def contact_info(self) -> Info:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(Info)
    def contact_info(self, contact_info: Info) -> None:
        self._contact_info = contact_info

    @property
    def borrowing_history(self) -> List[Book]:
        return copy.deepcopy(self._borrowing_history)

    @utility.type_checking(str)
    def search_book(self, title: str) -> Union[Book, None]:
        pass

    @utility.type_checking(Book)
    def borrow_book(self, book: Book) -> None:
        if book.available:
            book.available = False
            self._borrowing_history.append(book)
            print(f"{self.name} has borrowed the book: {book.title}")
        else:
            print(f"Sorry, the book {book.title} is not available for borrowing.")

    @utility.type_checking(Book)
    def return_book(self, book: Book) -> None:
        if book in self.borrowing_history:
            book.available = True
            self._borrowing_history.remove(book)
            print(f"{self.name} has returned the book: {book.title}")
        else:
            print(f"{self.name} did not borrow the book: {book.title}")

