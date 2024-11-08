from mafia.citizen import Citizen

class PlayerWasProtected(Exception):
    pass
class Doctor(Citizen):

    def add_vote(self, nominated: dict[str, int]):
        super().add_vote(nominated)

    def __init__(self, username: str):
        super().__init__(username)
        self.last_protected: str | None = None

    def choose_protected_player(self, username: str):
        if username == self.last_protected:
            raise PlayerWasProtected()

        self.last_protected = username




