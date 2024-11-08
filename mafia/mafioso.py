from mafia.player import Player


class Mafioso(Player):
    mafiosos = []

    def add_vote(self, nominated: dict[str, int]):
        for username in nominated.keys():
            if username not in self.mafiosos:
                nominated[username] += 1