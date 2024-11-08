from mafia.player import Player
import random

class Citizen(Player):
    def add_vote(self, nominated: dict[str, int]):
        for username in nominated.keys():
            if username is not self.username and random.randint(0, 1) == 1:
                nominated[username] += 1
