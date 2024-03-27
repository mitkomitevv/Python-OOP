from project.clients.base_client import BaseClient


class Student(BaseClient):
    INT_RATE = 2.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INT_RATE)

    def increase_clients_interest(self):
        self.interest += 1.0
