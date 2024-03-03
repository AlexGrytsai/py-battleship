from __future__ import annotations

import random

from app.main import Battleship


class Player:
    def __init__(self, name: str, fleet: list[tuple[tuple, tuple]]) -> None:
        self.name = name
        self.battleship = Battleship(fleet)

    def fire_to_enemy(self, location: tuple[int, int], enemy: Player) -> None:
        list_of_fire = {"miss": [], "hit": []}
        fire = enemy.battleship.fire(location)
        if fire == "Miss!":
            list_of_fire["miss"].append(location)
        else:
            list_of_fire["hit"].append(location)
        self._print_field_fires(list_of_fire)

    @staticmethod
    def _print_field_fires(location: dict[str, list]) -> None:
        game_field = [["\U0001F7E6"] * 10 for _ in range(10)]
        for row, col in location["miss"]:
            game_field[row][col] = "\u274C"
        for row, col in location["hit"]:
            game_field[row][col] = "\U0001F4A5"
        for row in game_field:
            print(*row)


class Pirate(Player):
    def __init__(self, fleet: list[tuple[tuple, tuple]]) -> None:
        pirate_names = [
            "Captain Jack Sparrow", "Captain Hector Barbossa",
            "Davy Jones", "Captain Edward Teague"
        ]
        self.name = random.choice(pirate_names)
        self.battleship = Battleship(fleet)
