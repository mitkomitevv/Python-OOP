from typing import List
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {'Appaloosa': Appaloosa, 'Thoroughbred': Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.VALID_HORSE_TYPES:
            if self.get_first_horse(horse_name):
                raise Exception(f"Horse {horse_name} has been already added!")

            horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.get_jockey(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.get_jockey(jockey_name)
        horse = self.get_last_horse(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if not horse.is_taken and jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        for horse in reversed(self.horses):
            if type(horse).__name__ == horse_type:
                if not horse.is_taken:
                    jockey.horse = horse
                    horse.is_taken = True
                    return f"Jockey {jockey_name} will ride the horse {horse.name}."

        raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.get_race(race_type)
        jockey = self.get_jockey(jockey_name)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.get_race(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        jockey_name = None
        horse_name = None

        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                jockey_name = jockey.name
                horse_name = jockey.horse.name

        return (f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}! "
                f"Winner's horse: {horse_name}.")

    def get_first_horse(self, horse_name: str):
        return next(filter(lambda h: h.name == horse_name, self.horses), None)

    def get_last_horse(self, horse_type: str):
        return next((h for h in reversed(self.horses) if type(h).__name__ == horse_type), None)

    def get_jockey(self, jockey_name: str):
        return next(filter(lambda j: j.name == jockey_name, self.jockeys), None)

    def get_race(self, race_type: str):
        return next(filter(lambda r: r.race_type == race_type, self.horse_races), None)
