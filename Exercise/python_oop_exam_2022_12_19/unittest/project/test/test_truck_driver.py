from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver("Driver", 10.0)

    def test_correct__init__(self):
        self.assertEqual("Driver", self.driver.name)
        self.assertEqual(10.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_where_value_less_than_0_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ve.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("Sofia", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer_where_cargo_already_in_available_cargoes_raises(self):
        self.driver.available_cargos = {"Varna": 100, "Dobrich": 50}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Varna", 20)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_where_valid_arg(self):
        self.driver.available_cargos = {"Varna": 100, "Dobrich": 50}
        result = self.driver.add_cargo_offer("Ruse", 150)

        self.assertEqual("Cargo for 150 to Ruse was added as an offer.", result)
        self.assertEqual({"Varna": 100, "Dobrich": 50, "Ruse": 150}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_where_no_cargoes_raises(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_happy_path(self):
        self.driver.add_cargo_offer("Varna", 20_000)
        self.driver.add_cargo_offer("Dobrich", 2_000)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("Driver is driving 20000 to Varna.", result)
        self.assertEqual(176000.0, self.driver.earned_money)
        self.assertEqual(20_000, self.driver.miles)

    def test_eat_where_decreasing_money(self):
        self.driver.earned_money = 40
        self.driver.eat(250)
        self.assertEqual(20, self.driver.earned_money)

    def test_sleep_where_decreasing_money(self):
        self.driver.earned_money = 50
        self.driver.sleep(1000)
        self.assertEqual(5, self.driver.earned_money)

    def test_pump_gas_where_decreasing_money(self):
        self.driver.earned_money = 501
        self.driver.pump_gas(1500)
        self.assertEqual(1, self.driver.earned_money)

    def test_repair_truck_where_decreasing_money(self):
        self.driver.earned_money = 8000
        self.driver.repair_truck(10_000)
        self.assertEqual(500, self.driver.earned_money)

    def test__repr__(self):
        expected_result = "Driver has 0 miles behind his back."
        self.assertEqual(expected_result, str(self.driver))

    def test__repr___with_changes(self):
        self.driver.available_cargos = {"Varna": 100, "Dobrich": 50}
        self.driver.drive_best_cargo_offer()
        self.assertEqual("Driver has 100 miles behind his back.", str(self.driver))


if __name__ == '__main__':
    main()
