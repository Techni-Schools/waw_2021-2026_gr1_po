import datetime
from datetime import date


class ReturnedBook:
    def __init__(self, when_rented: date, user_id: int):
        self.when_rented = when_rented
        self.when_returned = date.today()
        self.user_id = user_id

    def __repr__(self):
        return f"Returned book({self.when_rented},{self.when_returned}, {self.user_id})"

