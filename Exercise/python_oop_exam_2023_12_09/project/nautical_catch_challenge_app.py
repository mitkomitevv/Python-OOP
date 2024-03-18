from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVERS_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVERS_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if self.diver_validation(diver_name):
            return f"{diver_name} is already a participant."

        self.divers.append(self.DIVERS_TYPES[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self.fish_validation(fish_name):
            return f"{fish_name} is already permitted."

        self.fish_list.append(self.FISH_TYPES[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.diver_validation(diver_name)
        fish = self.fish_validation(fish_name)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        return self.oxygen_check(diver, fish, is_lucky)

    @staticmethod
    def oxygen_check(diver, fish, is_lucky):
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver.name} missed a good {fish.name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver.name} hits a {fish.points:.1f}pt. {fish.name}."

            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver.name} missed a good {fish.name}."

        else:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver.name} hits a {fish.points:.1f}pt. {fish.name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self.diver_validation(diver_name)
        result = [f"**{diver.name} Catch Report**"] + ['\n'.join(fish.fish_details() for fish in diver.catch)]
        return '\n'.join(result)

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]

        sorted_divers = sorted(healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = ["**Nautical Catch Challenge Statistics**"] + ['\n'.join(str(d) for d in sorted_divers)]

        return '\n'.join(result)

    def diver_validation(self, diver_name: str):
        try:
            return next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return None

    def fish_validation(self, fish_name: str):
        try:
            return next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return None
