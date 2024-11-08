from citizen import Citizen
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
        self.num_mafiosos = self.num_players//3
        self.players: list[Player] = [Doctor(usernames[0]),
                                      Police(usernames[1]),
                                      *[Mafioso(usernames[i]) for i in range(2, self.num_mafiosos+2)],
                                      *[Citizen(usernames[i]) for i in range(self.num_mafiosos+2, self.num_players)]]
        self.num_citizens = self.num_players - self.num_mafiosos

    def start(self):
        while self.num_citizens > self.num_mafiosos > 0:


        if self.num_mafiosos == 0:
            print("Citizens won")
        else:
            print("Mafiosos won")

