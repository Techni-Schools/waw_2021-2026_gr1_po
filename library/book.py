class Book:
    book_counter = 0

    def __init__(self, title: str, author: str, genre: str, year: int):
        self.id = Book.book_counter
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        Book.book_counter += 1

    def __repr__(self):
        return f"({self.id},{self.genre}, {self.author})"