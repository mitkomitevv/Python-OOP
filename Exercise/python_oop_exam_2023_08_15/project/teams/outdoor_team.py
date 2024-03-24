from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    TYPE = "OutdoorTeam"
    ADV_INCREASE = 115

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=1000.0)

    def win(self):
        self.advantage += self.ADV_INCREASE
        self.wins += 1
