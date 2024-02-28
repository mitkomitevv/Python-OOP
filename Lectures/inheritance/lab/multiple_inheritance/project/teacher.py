from employee import Employee
from person import Person


class Teacher(Person, Employee):

    @staticmethod
    def teach():
        return "teaching..."
