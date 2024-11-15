from citizen import Citizen
from mafia.status import Status
from mafioso import Mafioso
from police import Police
from doctor import Doctor, PlayerWasProtected
from player import Player
from typing import Type, TypeVar
import random

T = TypeVar('T')


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

    @staticmethod
    def count_votes(nominated: dict[str, int], alive_players: list[Player]) -> None:
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
            killed_player = list(
                filter(lambda player_to_kill: player_to_kill.username == max_num_votes_username, alive_players)
            )[0]
            killed_player.status = Status.Dead
        else:
            print("Nobody was eliminated")

    def get_alive_players(self) -> list[Player]:
        return list(filter(lambda player: player.is_alive(), self.players))

    def get_special_citizen(self, class_name: type[T]) -> T:
        return list(map(class_name, filter(lambda player: isinstance(player, class_name), self.players)))[0]

    def kill_player(self) -> Citizen:
        return list(
            filter(lambda player: isinstance(player, Citizen) and player.is_alive(), self.get_alive_players())
        )[0]

    def start(self):
        def is_not_finished():
            return self.num_citizens > self.num_mafiosos > 0

        while is_not_finished():
            alive_players = self.get_alive_players()
            random.shuffle(alive_players)

            nominated = {player.username: 0 for player in alive_players[:3]}

            self.count_votes(nominated, alive_players)

            if (doctor := self.get_special_citizen(Doctor)).is_alive():
                alive_players = self.get_alive_players()
                protected_player: Player = random.choice(alive_players)

                try:
                    doctor.choose_protected_player(protected_player.username)
                except PlayerWasProtected:
                    alive_players.remove(protected_player)

                    protected_player: Player = random.choice(alive_players)
                    doctor.choose_protected_player(protected_player.username)

            if (police := self.get_special_citizen(Police)).is_alive():
                checked_players: list[str] = list(police.checked_players.keys())
                left_players: list[Player] = list(filter(lambda
                                                             player: player.username not in checked_players and player.is_alive() and player.username != police.username,
                                                         self.get_alive_players()))
                police.check_player(random.choice(left_players))

            chosen_player = self.kill_player()
            if chosen_player.username == doctor.last_protected:
                print("Nobody was killed")
            else:
                print(f"Player {chosen_player.username} was killed at night")

        if not self.num_mafiosos:
            print("Citizens won")
            return

        print("Mafiosos won")
