from project.services.base_service import BaseService


class MainService(BaseService):
    MAIN_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.MAIN_CAPACITY)

    def details(self):
        return (f"{self.name} Main Service:\n"
                f"Robots: {' '.join(r.name for r in self.robots) if self.robots else 'none'}")
