from datetime import date
from functools import *

from returned_book import ReturnedBook
from user import User
from book import Book
from rented_book import RentedBook



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
        self.rented_books: dict[int, list[RentedBook]] = {}
        self.returned_books: dict[int, list[ReturnedBook]] = {}
        self.debts: dict[int, int] = {}

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

        if self.rented_books.values() and book.id in map(lambda rented_book: rented_book.book_id,
                                                         reduce(list.__add__, self.rented_books.values())):
            raise BookAlreadyRented()

        if self.rented_books.get(user_id):
            self.rented_books[user_id].append(RentedBook(book.id))
        else:
            self.rented_books[user_id] = [RentedBook(book.id)]


    def return_book(self, book_id: int, when_returned: date = date.today()):
        for user_id, rented_books in self.rented_books.items():
            if book_id in map(lambda rented_book: rented_book.book_id, rented_books):
                returned_book: list[RentedBook] = list(filter(lambda rented_book: rented_book.book_id == book_id, rented_books))
                rb = ReturnedBook(returned_book[0].when_rented, user_id, when_returned)
                debt = rb.fee()
                if debt > 0:
                    if self.debts.get(user_id): self.debts[user_id] += debt
                    else: self.debts[user_id] = debt
                if self.returned_books.get(book_id):
                    self.returned_books[book_id].append(rb)
                else:
                    self.returned_books[book_id] = [rb]
                remaining_books: list[RentedBook] = list(filter(lambda rented_book: rented_book.book_id != book_id,
                                                                rented_books))

                if remaining_books:
                    self.rented_books[user_id] = remaining_books
                else:
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

    def print_genre_by_author(self, author: str):
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

    def get_book(self, book_id: int):
        books = reduce(list.__add__, self.books.values())
        filtered_books = list(filter(lambda book: book.id == book_id, books))

        if not filtered_books:
            raise BookDoesNotExists()

        return filtered_books[0]





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

library.rent_book(0, book_1)
library.rent_book(0, book_2)
library.return_book(0, date(2024, 12, 26))
print(library.debts)
library.return_book(1, date(2024, 12, 29))
print(library.debts)


while True:
    print("1 - dodaj użytkownika")
    print("2 - dodaj książkę")
    print("3 - wypisz należności wybranego użytkownika")
    print("4 - wypisz listę wypożyczonych książęk wybranego użytkownika")
    print("5 - wypozycz ksiazke dla uzytkownika")
    print("@ - zakończ program")
    operation = input("Wybierz opcję: ")
    match operation:
        case "1":
            name = input("podaj imię: ")
            surname = input("podaj nazwisko: ")
            library.add_user(User(name, surname))
        case "2":
            title = input("podaj tytuł: ")
            author = input("podaj autora: ")
            year = int(input("podaj rok wydania: "))
            genre = input("podaj gatunek: ")
            library.add_book(Book(title=title, author=author, genre=genre, year=year))
        case "3":
            user_id = int(input("Podaj id użytkownika: "))

            if library.debts.get(user_id):
                print(library.debts[user_id])
            else:
                print(0)
        case "4":
            user_id = int(input("Podaj id użytkownika: "))
            if library.rented_books.get(user_id):
                print(list(map(lambda rented_book: rented_book.book_id, library.rented_books[user_id])))
            else:
                print([])

        case "5":
            user_id = int(input("Podaj id użytkownika: "))
            book_id = int(input("Podaj id ksiazki: "))
            library.rent_book(user_id, library.get_book(book_id))

        case "@":
            break

        case _:
            print("Nie wybrano prawidłowej opcji.")

