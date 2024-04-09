from typing import List
from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = {"Starter": Starter, 'MainDish': MainDish, 'Dessert': Dessert}
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        meals_to_order = []
        bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal_name == meal.name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.bill += bill
        client.shopping_cart.extend(meals_to_order)

        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += quantity

            for meal in self.menu:
                if meal_name == meal.name:
                    meal.quantity -= quantity

        client_cart = ', '.join(m.name for m in client.shopping_cart)
        return (f"Client {client_phone_number} "
                f"successfully ordered {client_cart} "
                f"for {client.bill:.2f}lv.")

        # for meal_name, quantity in meal_names_and_quantities.items():
        #     try:
        #         meal = next(filter(lambda m: m.name == meal_name, self.menu))
        #     except StopIteration:
        #         raise Exception(f"{meal_name} is not on the menu!")
        #
        #     if meal.quantity < quantity:
        #         raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
        #
        #     meal.quantity -= quantity
        #     client.bill += meal.price * quantity
        #     cart_meal = next(filter(lambda m: m.name == meal_name, client.shopping_cart), None)
        #     if cart_meal:
        #         cart_meal.quantity += quantity
        #     else:
        #         client.shopping_cart.append(self.VALID_MEALS[type(meal).__name__](meal_name, meal.price, quantity))
        #
        # client_cart = ', '.join(m.name for m in client.shopping_cart)
        # return (f"Client {client_phone_number} "
        #         f"successfully ordered {client_cart} "
        #         f"for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity

        client.ordered_meals = {}
        client.shopping_cart = []
        client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid = client.bill
        client.shopping_cart = []
        client.bill = 0
        self.receipt_id += 1
        return (f"Receipt #{self.receipt_id} with total amount of {total_paid:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
