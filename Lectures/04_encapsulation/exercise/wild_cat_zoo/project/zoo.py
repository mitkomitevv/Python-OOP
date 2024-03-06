class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        care_money = sum(c.money_for_care for c in self.animals)
        if self.__budget >= care_money:
            self.__budget -= care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        lions = list(filter(lambda l: l.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda t: t.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda c: c.__class__.__name__ == "Cheetah", self.animals))

        result.append(f"----- {len(lions)} Lions:")
        lions_repr = "\n".join([lion.__repr__() for lion in lions])
        result.append(lions_repr)
        result.append(f"----- {len(tigers)} Tigers:")
        tigers_repr = "\n".join([tiger.__repr__() for tiger in tigers])
        result.append(tigers_repr)
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        cheetahs_repr = "\n".join([cheetah.__repr__() for cheetah in cheetahs])
        result.append(cheetahs_repr)

        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        keepers = list(filter(lambda k: k.__class__.__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda c: c.__class__.__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda v: v.__class__.__name__ == "Vet", self.workers))

        result.append(f"----- {len(keepers)} Keepers:")
        keepers_repr = "\n".join([keeper.__repr__() for keeper in keepers])
        result.append(keepers_repr)
        result.append(f"----- {len(caretakers)} Caretakers:")
        caretakers_repr = "\n".join([caretaker.__repr__() for caretaker in caretakers])
        result.append(caretakers_repr)
        result.append(f"----- {len(vets)} Vets:")
        vets_repr = "\n".join([vet.__repr__() for vet in vets])
        result.append(vets_repr)

        return "\n".join(result)
