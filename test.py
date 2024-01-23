from models import Library, Book, Ebook

library = Library()

book1 = Book("The Python Programming Language",
             "Guido van Rossum", 9780134076430)
book2 = Book("Introduction to Machine Learning", "Andrew Ng", 9781119545560)

ebook1 = Ebook("Learn Python the Hard Way", "Zed Shaw", 9780321884916, "PDF")
ebook2 = Ebook("Dive into Python 3", "Mark Pilgrim", 9781590593561, "EPUB")

library.add_book(book1)
library.add_book(book2)
library.add_book(ebook1)
library.add_book(ebook2)

library.display_books()

book_titles = [
    "Automate the Boring Stuff with Python",
    "Dive into Python 3"
]

for title in book_titles:
    try:
        found_book = library.search_by_title(title)
        print(f"Found Book \n{found_book.display_info()}")
    except Library.BookNotFound as e:
        print("Not Found \n", e)
