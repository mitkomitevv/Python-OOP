from typing import List
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.VALID_EQUIPMENT[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.VALID_TEAMS[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self.get_team(team_name)

        equipment = [e for e in self.equipment if e.type == equipment_type][-1]
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.get_team(team_name)

        if not team:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count_changed_pcs = len([e.increase_price() for e in self.equipment if e.type == equipment_type])
        return f"Successfully changed {count_changed_pcs}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self.get_team(team_name1)
        team2 = self.get_team(team_name2)

        if team1.TYPE != team2.TYPE:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_sum = team1.advantage + sum(x.protection for x in team1.equipment)
        team2_sum = team2.advantage + sum(x.protection for x in team2.equipment)

        if team1_sum == team2_sum:
            return "No winner in this game."

        winner = team1 if team1_sum > team2_sum else team2
        winner.win()

        return f"The winner is {winner.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        team_statistics = '\n'.join(team.get_statistics() for team in sorted_teams)

        result = (f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:\n"
                  f"{team_statistics}")

        return result

    def get_team(self, team_name):
        try:
            return next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            return None
