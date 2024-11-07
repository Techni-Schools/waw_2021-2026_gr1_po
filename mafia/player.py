from mafia.status import Status
from abc import abstractmethod

class Player:
    def __init__(self, username: str):
        self.username = username
        self.status = Status.Alive

    @abstractmethod
    def add_vote(self, nominated: dict[str, int]):
        pass