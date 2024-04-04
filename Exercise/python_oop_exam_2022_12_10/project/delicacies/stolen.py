from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    PORTION_WEIGHT = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, self.PORTION_WEIGHT, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
