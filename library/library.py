from functools import *
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


class BookDoesNotRented(Exception):
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

    def return_book(self, book_id: int):
        for user_id, books_id in self.rented_books.items():
            if book_id in books_id:
                books_id.remove(book_id)

                if not books_id:
                    self.rented_books.pop(user_id)

                return

        raise BookDoesNotRented()

    def display_books_title_by_genre(self, genre: str):
        book_count = 0
        for title, books in self.books.items():
            if genre in map(lambda book: book.genre, books):
                book_count += 1
                print(title)

        if book_count == 0:
            print(f'Brak książek o gatunku {genre}')

    def print_genre_by_author(self, author:str):
        books = reduce(list.__add__, self.books.values())
        books = filter(lambda book: book.author == author, books)
        books = map(lambda book: book.genre, books)
        books = set(books)
        print(books)

    def add_books(self, *args: Book):
        for book in args:
            self.add_book(book)

    def add_users(self, *args: User):
        for user in args:
            self.add_user(user)



library = Library()
book_1 = Book("Zbrodnia Ikara", "Fiodor Dostojewski", "dramat", 2018)
book_2 = Book("Lalka", "Bolesław Prus", "sci-fi", 2018)
book_3 = Book("Adam Mickiewicz", "Pan Tadeusz", "fantastyka", 2018)
book_4 = Book("Hobbit", "JRR Tolkien", "fantastyka", 2018)
book_5 = Book("Mistrz Małgorzata", "Michal Buhałkow", "fantasy", 2018)
book_6 = Book("Adam Czynsz", "Pan Tadeusz", "fantastyka", 2018)
book_7 = Book("Adam Mickiewicz", "Pan Tadeusz", "fantasy", 2018)
book_8 = Book("Adam Mickiewicz", "Pan Tadeusz", "komedia", 2018)
library.add_books(book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8)
# print(library.books)

user_1 = User("Bartosz", "Rejs", "6969696969", "dupa@gmail.com")
user_2 = User("Adam", "Czyz", "6969696969", "dupa@gmail.com")
user_3 = User("Maks", "Wiewiora", "6969696969", "dupa@gmail.com")
library.add_users(user_1, user_2, user_3)
# print(library.users)
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

try:
    library.return_book(book_1.id)
except BookDoesNotRented:
    print("Book didn't rent")

# library.display_books_title_by_genre("fantastyka1")
library.print_genre_by_author("Pan Tadeusz")