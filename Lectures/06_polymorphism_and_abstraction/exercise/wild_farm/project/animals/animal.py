from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @property
    @abstractmethod
    def compatible_food(self):
        pass

    @property
    @abstractmethod
    def gained_weight(self):
        pass

    def feed(self, food: Food):
        if type(food) not in self.compatible_food:
            return f"{type(self).__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.gained_weight * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
