from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self.get_user(driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self.get_vehicle(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        try:
            route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point][0]
        except IndexError:
            route = None

        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.length > length:
                route.is_locked = True

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self.get_user(driving_license_number)
        vehicle = self.get_vehicle(license_plate_number)
        route = self.get_route(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        ordered_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))[:count]
        for vehicle in ordered_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = vehicle.MAX_BATTERY_CAPACITY

        return f"{len(ordered_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        result.append(('\n'.join(str(u) for u in sorted_users)))
        return '\n'.join(result)

    def get_user(self, driving_license_number):
        try:
            return next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        except StopIteration:
            return None

    def get_vehicle(self, license_plate_number):
        try:
            return next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        except StopIteration:
            return None

    def get_route(self, route_id):
        try:
            return next(filter(lambda r: r.route_id == route_id, self.routes))
        except StopIteration:
            return None
