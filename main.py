from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Book, Library, Ebook, BookModel

app = FastAPI()

library = Library()


@app.post("/books/", response_model=BookModel)
def create_book(book: BookModel):
    if not book.file_format:
        new_book = Book(title=book.title, author=book.author,
                        isbn=book.isbn)
        library.add_book(new_book)
        return {"title": new_book.title, "author": new_book.author, "isbn": new_book.isbn}
    else:
        new_book = Ebook(title=book.title, author=book.author,
                         isbn=book.isbn, file_format=book.file_format)
        library.add_book(new_book)
        return {"title": new_book.title, "author": new_book.author, "isbn": new_book.isbn, "file_format": new_book.file_format}


@app.get("/books/", response_model=List[BookModel])
def get_books():
    try:
        return [{"title": book.title, "author": book.author, "isbn": book.isbn, "file_format": getattr(book, 'file_format', None)} for book in library.books]
    except library.EmptyLibraryError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/books/{title}", response_model=BookModel)
def get_book_by_title(title: str):
    try:
        book = library.search_by_title(title)
        return {"title": book.title, "author": book.author, "isbn": book.isbn, "file_format": getattr(book, 'file_format', None)}
    except library.BookNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.delete("/books/{title}")
def delete_book_by_title(title: str):
    try:
        library.delete_book_by_title(title)
        return {"detail": f"Book '{title}' deleted successfully"}
    except library.BookNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
