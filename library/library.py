from user import User
from book import Book


class BookAlreadyExists(Exception):
    pass


class UserAlreadyExists(Exception):
    pass

class BookAlreadyRented(Exception):
    pass

class Library:
    def __init__(self):
        self.users: list[User] = []
        self.books: dict[str, list[Book]] = {}
        self.rented_books: dict[int, list[int]] = {}

    def add_book(self, book: Book):
        if self.books.get(book.title):
            books_of_title = self.books[book.title]
            if book not in books_of_title:
                books_of_title.append(book)
            else:
                raise BookAlreadyExists()
        else:
            self.books[book.title] = [book]

    def add_user(self, user: User):
        if user in self.users:
            raise UserAlreadyExists()
        else:
            self.users.append(user)

    def rent_book(self, user_id: int, book_id: int):
        for list_book in self.rented_books.values():
            for book in list_book:
                if book_id == book:
                    raise BookAlreadyRented()

library = Library()
book_1 = Book("Zbrodnia Ikara", "Fiodor Dostojewski", "dramat", 2018)
library.add_book(book_1)
print(library.books)

user_1 = User("Bartosz", "Prejs", "6969696969", "dupa@gmail.com")
library.add_user(user_1)
print(library.users)
