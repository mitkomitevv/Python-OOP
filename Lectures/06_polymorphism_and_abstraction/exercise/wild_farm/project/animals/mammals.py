from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def compatible_food(self):
        return [Fruit, Vegetable]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def compatible_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def compatible_food(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def compatible_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00
