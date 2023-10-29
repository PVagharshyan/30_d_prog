from liberary_member import LibraryMember
from typing import List, Union
from info import Info
from books import Book
import utility

class Librarian(LibraryMember):
    def __init__(self, name: str, contact_info: Info):
        self.name = name
        self.contact_info = contact_info

    @utility.type_checking(str)
    def search_book(self, title: str) -> Union[Book, None]:
        pass

    @utility.type_checking(Book)
    def borrow_book(self, book: Book) -> None:
        print("Librarians cannot borrow books.")

    @utility.type_checking(Book)
    def return_book(self, book: Book) -> None:
        print("Librarians do not borrow books, so they cannot return them.")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self) -> Info:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(Info)
    def contact_info(self, value: Info):
        self._contact_info = value
