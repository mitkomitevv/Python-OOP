from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    oxygen_regen = 540

    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch: int):
        oxygen_reduce = round(time_to_catch * 0.3)
        if self.oxygen_level < oxygen_reduce:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= oxygen_reduce

    def renew_oxy(self):
        self.oxygen_level = self.oxygen_regen
