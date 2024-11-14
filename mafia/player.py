from mafia.status import Status
from abc import abstractmethod

class Player:
    def __init__(self, username: str):
        self.username = username
        self.status = Status.Alive

    def is_alive(self):
        return self.status.value

    @abstractmethod
    def add_vote(self, nominated: dict[str, int]):
        pass