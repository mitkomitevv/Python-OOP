from typing import List
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if self.get_delicacy(name):
            raise Exception(f"{name} already exists!")

        self.delicacies.append(self.VALID_DELICACIES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        if self.get_booth(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        self.booths.append(self.VALID_BOOTHS[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            booth = next(filter(lambda b: not b.is_reserved and b.capacity >= number_of_people, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.get_booth(booth_number)
        delicacy = self.get_delicacy(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.get_booth(booth_number)

        bill = sum(d.price for d in booth.delicacy_orders) + booth.price_for_reservation
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return (f"Booth {booth_number}:\n"
                f"Bill: {bill:.2f}lv.")

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def get_delicacy(self, name: str):
        try:
            return next(filter(lambda d: d.name == name, self.delicacies))
        except StopIteration:
            return None

    def get_booth(self, booth_number: int):
        try:
            return next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            return None
