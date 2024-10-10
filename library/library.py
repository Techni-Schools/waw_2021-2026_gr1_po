from user import User
from book import Book


class BookAlreadyExists(Exception):
    pass


class UserAlreadyExists(Exception):
    pass

class BookAlreadyRented(Exception):
    pass

class UserDoesNotExists(Exception):
    pass

class BookTitleNotExists(Exception):
    pass

class BookDoesNotExists(Exception):
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

    def rent_book(self, user_id: int, book: Book):
        if user_id not in map(lambda user: user.id, self.users):
            raise UserDoesNotExists()

        if not self.books.get(book.title):
            raise BookTitleNotExists()

        if book not in self.books[book.title]:
            raise BookDoesNotExists()

        for book_ids in self.rented_books.values():
            for book_id in book_ids:
                if book.id == book_id:
                    raise BookAlreadyRented()

        if self.rented_books.get(user_id):
            self.rented_books[user_id].append(book.id)
        else:
            self.rented_books[user_id] = [book.id]


library = Library()
book_1 = Book("Zbrodnia Ikara", "Fiodor Dostojewski", "dramat", 2018)
library.add_book(book_1)
print(library.books)

user_1 = User("Bartosz", "Prejs", "6969696969", "dupa@gmail.com")
library.add_user(user_1)
print(library.users)
try:
    library.rent_book(user_1.id, book_1)
except UserDoesNotExists:
    print("User does not exist")
except BookTitleNotExists:
    print("Book title does not exist")
except BookDoesNotExists:
    print("Book does not exist")
except BookAlreadyRented:
    print("Book is already rented")