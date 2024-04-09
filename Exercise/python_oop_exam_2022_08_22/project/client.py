from typing import List
from project.meals.meal import Meal


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill: float = 0.0
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.startswith('0'):
            raise ValueError("Invalid phone number!")
        if len(value) != 10:
            raise ValueError("Invalid phone number!")
        if not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
