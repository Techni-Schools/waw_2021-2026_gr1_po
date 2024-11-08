from mafia.citizen import Citizen


class Police(Citizen):
    def __init__(self, username: str):
        super().__init__(username)
        self.checked_players = {}

    def add_vote(self, nominated: dict[str, int]):
        for username in nominated.keys():
            checked_player = self.checked_players.get(username)
            if checked_player:
                nominated[username] += 1
            #TODO
