import random

from mafia.citizen import Citizen
from mafia.mafioso import Mafioso
from mafia.player import Player


class Police(Citizen):
    def __init__(self, username: str):
        super().__init__(username)
        self.checked_players:dict[str, bool] = {}

    def add_vote(self, nominated: dict[str, int]):
        for username in nominated.keys():
            if username is self.username:
                continue
            checked_player = self.checked_players.get(username)
            if checked_player is None:
                if random.randint(0, 1) == 1:
                    nominated[username] += 1
            elif checked_player == 1:
                nominated[username] +=1

    def check_player(self, player: Player):
        self.checked_players[player.username] = isinstance(player, Mafioso)