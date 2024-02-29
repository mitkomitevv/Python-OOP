class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str):
        if Vet.space:
            Vet.space -= 1
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name: str):
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
