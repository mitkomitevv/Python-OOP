from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        self.loans.append(self.VALID_LOANS[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        self.clients.append(self.VALID_CLIENTS[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = self.get_loan(loan_type)
        client = self.get_client(client_id)

        if type(client).__name__ == "Student" and loan.type != "StudentLoan":
            raise Exception("Inappropriate loan type!")
        if type(client).__name__ == "Adult" and loan.type != "MortgageLoan":
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.get_client(client_id)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        count_increased_loans = len([l.increase_interest_rate() for l in self.loans if l.type == loan_type])
        return f"Successfully changed {count_increased_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        count_client_rates = len([c.increase_clients_interest() for c in self.clients if c.interest < min_rate])
        return f"Number of clients affected: {count_client_rates}."

    def get_statistics(self):
        clients_income = sum(c.income for c in self.clients)
        granted_loans = sum(len(c.loans) for c in self.clients)
        granted_sum = sum(l.amount for client in self.clients for l in client.loans)
        not_granted_sum = sum(l.amount for l in self.loans)
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0

        result = (f"Active Clients: {len(self.clients)}\n"
                  f"Total Income: {clients_income:.2f}\n"
                  f"Granted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}\n"
                  f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

        return result

    def get_loan(self, loan_type: str):
        try:
            return next(filter(lambda l: l.type == loan_type, self.loans))
        except StopIteration:
            return None

    def get_client(self, client_id: str):
        try:
            return next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            return None
