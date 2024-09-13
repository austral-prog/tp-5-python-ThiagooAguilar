from typing import Dict, List
from src.Book import Book
from src.User import User

class Library:
    def __init__(self) -> None:
        self.__books: Dict[str, Book] = {}
        self.__users: Dict[int, User] = {}
        self.__checked_out_books: List[str] = []
        self.__checked_in_books: List[str] = []

    # Getters
    def get_books(self) -> List[Book]:
        return [self.__books[isbn] for isbn in self.__books]

    def get_users(self) -> List[User]:
        return list(self.__users.values())

    def get_checked_out_books(self) -> List[str]:
        return self.__checked_out_books

    def get_checked_in_books(self) -> List[str]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        if isbn not in self.__books:
            self.__books[isbn] = Book(isbn, title, author)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books.values():
            print(book)

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        if isbn not in self.__books:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI {dni}"
        if dni not in self.__users:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI {dni}"
        book = self.__books[isbn]
        person = self.__users[dni]
        if book.is_available():
            book.set_available(False)
            self.__checked_out_books.append(isbn)
            person.increment_checkouts()
            return f"User {dni} checked out book {isbn}"
        else:
            return f"Book {isbn} is not available"

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        if isbn not in self.__books:
            return f"Book {isbn} is not available"

        if isbn not in self.__checked_out_books:
            return f"Book {isbn} is not checked out"

        if dni not in self.__users:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI {dni}"

        book = self.__books[isbn]
        book.set_available(True)
        self.__checked_out_books.remove(isbn)
        self.__checked_in_books.append(isbn)
        user = self.__users[dni]
        user.increment_checkouts()
        return f"Book {isbn} checked in by user {dni}"

    # Utils
    def add_user(self, dni: int, name: str) -> None:
        if dni not in self.__users:
            self.__users[dni] = User(dni, name)


