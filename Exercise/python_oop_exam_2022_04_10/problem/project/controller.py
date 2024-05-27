from typing import List
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    SUSTENANCE_TYPES = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args):
        added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name: str, sustenance_type: str):
        player = next(filter(lambda p: p.name == player_name, self.players), None)

        if sustenance_type in self.SUSTENANCE_TYPES:
            supply = next(filter(lambda s: type(s).__name__ == sustenance_type, self.supplies[::-1]), None)

            if sustenance_type == "Food" and not supply:
                raise Exception("There are no food supplies left!")
            if sustenance_type == "Drink" and not supply:
                raise Exception("There are no drink supplies left!")

            if player:
                if player.stamina < 100:
                    if player.stamina + supply.energy <= 100:
                        player.stamina += supply.energy
                    else:
                        player.stamina = 100
                else:
                    return f"{player_name} have enough stamina."

                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = next(filter(lambda p: p.name == first_player_name, self.players), None)
        player2 = next(filter(lambda p: p.name == second_player_name, self.players), None)

        if player1.stamina <= 0 and player2.stamina <= 0:
            return (f"Player {first_player_name} does not have enough stamina.\n"
                    f"Player {second_player_name} does not have enough stamina.")
        elif player1.stamina <= 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif player2.stamina <= 0:
            return f"Player {second_player_name} does not have enough stamina."
        else:
            attacker = player1 if player1.stamina < player2.stamina else player2
            defender = player1 if player1.stamina > player2.stamina else player2

            if defender.stamina - (attacker.stamina / 2) < 0:
                defender.stamina = 0
            else:
                defender.stamina -= (attacker.stamina / 2)

            if attacker.stamina - (defender.stamina / 2) < 0:
                attacker.stamina = 0
            else:
                attacker.stamina -= (defender.stamina / 2)

            if defender.stamina < attacker.stamina:
                return f"Winner: {attacker.name}"
            else:
                return f"Winner: {defender.name}"

    def next_day(self):
        for player in self.players:
            if (player.stamina - (player.age * 2)) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []

        for player in self.players:
            result.append(player.__str__())
        for supply in self.supplies:
            result.append(supply.details())

        return "\n".join(result)
