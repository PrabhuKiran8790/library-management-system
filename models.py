from typing import List, Optional
from pydantic import BaseModel


class BookModel(BaseModel):
    title: str
    author: str
    isbn: int
    file_format: Optional[str] = None


class Book:
    def __init__(self, title: str, author: str, isbn: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    class BookNotFound(Exception):
        pass

    class EmptyLibraryError(Exception):
        pass

    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)
        else:
            print(
                f"Book '{book.title}' by '{book.author}' already exists in the library.")

    def display_books(self) -> None:
        if not self.books:
            raise self.EmptyLibraryError("The library is empty.")
        for book in self.books:
            print(book.display_info())

    def search_by_title(self, title: str) -> Book:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise self.BookNotFound(f"No books found with title '{title}'")

    def delete_book_by_title(self, title: str) -> None:
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return
        raise self.BookNotFound(f"No books found with title '{title}'")


class Ebook(Book):
    def __init__(self, title: str, author: str, isbn: int, file_format: str) -> None:
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def display_info(self) -> str:
        book_info = super().display_info()
        return f"{book_info}, File Format: {self.file_format}"
