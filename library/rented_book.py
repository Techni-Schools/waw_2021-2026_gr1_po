from datetime import date


class RentedBook:
    def __init__(self, book_id: int):
        self.book_id: int = book_id
        self.when_rented: date = date.today()

    def __repr__(self):
        return f"Rented book({self.book_id},{self.when_rented})"
