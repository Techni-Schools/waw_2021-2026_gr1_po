import datetime
from datetime import date


class ReturnedBook:
    cost_per_day = 1

    def __init__(self, when_rented: date, user_id: int, when_returned: date = date.today()):
        self.when_rented = when_rented
        self.when_returned = when_returned
        self.user_id = user_id

    def fee(self) -> int:
        return max(0, ((self.when_returned - self.when_rented).days - 30) * ReturnedBook.cost_per_day)

    def __repr__(self):
        return f"Returned book({self.when_rented},{self.when_returned}, {self.user_id})"
