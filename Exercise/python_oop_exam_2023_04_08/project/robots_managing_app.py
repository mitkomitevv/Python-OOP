from typing import List
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
    VALID_COMBINATIONS = {'MaleRobot': 'MainService', 'FemaleRobot': 'SecondaryService'}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        self.services.append(self.VALID_SERVICES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        self.robots.append(self.VALID_ROBOTS[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.get_robot(robot_name)
        service = self.get_service(service_name)

        robot_type = type(robot).__name__
        service_type = type(service).__name__

        if service_type != self.VALID_COMBINATIONS[robot_type]:
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.get_service(service_name)
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot[0])
        self.robots.append(robot[0])
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.get_service(service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.get_service(service_name)
        price = sum(r.price for r in service.robots)
        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        return '\n'.join(service.details() for service in self.services)

    def get_robot(self, robot_name):
        try:
            return next(filter(lambda r: r.name == robot_name, self.robots))
        except StopIteration:
            return None

    def get_service(self, service_name):
        try:
            return next(filter(lambda s: s.name == service_name, self.services))
        except StopIteration:
            return None
