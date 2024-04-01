from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        musician = self.get_musician(name)
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError(f"Invalid musician type!")
        if musician:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(self.VALID_MUSICIANS[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self.get_band(name)
        if band:
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.get_concert(place)
        if concert:
            # check later
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.get_musician(musician_name)
        band = self.get_band(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.get_band(band_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        # check later
        member = [m for m in band.members if m.name == musician_name]
        if not member:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(member[0])
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.get_band(band_name)
        concert = self.get_concert(concert_place)

        for musician_type in self.VALID_MUSICIANS.keys():
            if not any(filter(lambda m: m.TYPE == musician_type, band.members)):
                raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for member in band.members:
                if member.TYPE == 'Drummer' and \
                         "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.TYPE == 'Singer' and "sing high pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.TYPE == 'Guitarist' and "play rock" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for member in band.members:
                if member.TYPE == 'Drummer' and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.TYPE == 'Singer' and "sing low pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.TYPE == 'Guitarist' and "play metal" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for member in band.members:
                if member.TYPE == 'Drummer' \
                        and "play the drums with drum brushes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.TYPE == 'Singer' \
                        and ("sing low pitch notes" not in member.skills
                             or "sing high pitch notes" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.TYPE == 'Guitarist' and "play jazz" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def get_musician(self, musician_name: str):
        try:
            return next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            return None

    def get_band(self, band_name: str):
        try:
            return next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            return None

    def get_concert(self, place: str):
        try:
            return next(filter(lambda c: c.place == place, self.concerts))
        except StopIteration:
            return None
