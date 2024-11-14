from citizen import Citizen
from mafia.status import Status
from mafioso import Mafioso
from police import Police
from doctor import Doctor
from player import Player
import random


class Game:
    def __init__(self, usernames: list[str]):
        self.is_playing = True
        random.shuffle(usernames)
        self.num_players = len(usernames)
        self.num_mafiosos = self.num_players // 3
        self.players: list[Player] = [Doctor(usernames[0]),
                                      Police(usernames[1]),
                                      *[Mafioso(usernames[i]) for i in range(2, self.num_mafiosos + 2)],
                                      *[Citizen(usernames[i]) for i in range(self.num_mafiosos + 2, self.num_players)]]
        Mafioso.mafiosos = usernames[2:self.num_mafiosos + 2]
        self.num_citizens = self.num_players - self.num_mafiosos

    def start(self):
        def is_not_finished():
            return self.num_citizens > self.num_mafiosos > 0
        while is_not_finished():
            alive_players: list[Player] = list(filter(lambda player: player.is_alive(), self.players))
            random.shuffle(alive_players)
            nominated = {alive_players[0].username: 0, alive_players[1].username: 0, alive_players[2].username: 0}
            for player in alive_players:
                player.add_vote(nominated)
            max_num_votes = 0
            max_num_votes_username = ""
            is_unique = True
            for username, value in nominated.items():
                if value > max_num_votes:
                    max_num_votes = value
                    max_num_votes_username = username
                    is_unique = True
                elif value == max_num_votes:
                    is_unique = False
            if is_unique and max_num_votes > len(alive_players) / 2:
                print(f"Player {max_num_votes_username} is eliminated")
                list(filter(lambda player: player.username == max_num_votes_username, alive_players))[0].status = Status.Dead
            else:
                print("Nobody was eliminated")

            doctor = list(filter(lambda player: isinstance(player, Doctor), self.players))[0]
            if doctor.is_alive():
                pass
                # TODO


        if self.num_mafiosos == 0:
            print("Citizens won")
        else:
            print("Mafiosos won")
