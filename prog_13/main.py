from books import Book, Fiction, NonFiction
from liberarians import Librarian
from info import Info
from borrowers import Borrower

if __name__ == "__main__":
    fiction_book = Fiction("The Great Gatsby", "F. Scott Fitzgerald", "1925-12-02")
    non_fiction_book = NonFiction("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "2011-02-12")

    i1 = Info("093393933", "sdas", "paylak.vagharshyan@gamil.com")
    i2 = Info("093393933", "sdas", "paylak.vagharshyan@gamil.com")
    borrower = Borrower("Alice", i1)
    librarian = Librarian("Librarian", i2)

    borrower.borrow_book(fiction_book)
    borrower.borrow_book(non_fiction_book)

    librarian.borrow_book(fiction_book)  # Librarian cannot borrow books

    borrower.return_book(fiction_book)
    librarian.return_book(fiction_book)  # Librarian cannot return books
