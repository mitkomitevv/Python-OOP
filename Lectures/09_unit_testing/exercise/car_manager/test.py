from unittest import TestCase, main
from car_manager import Car


class CarManagerTest(TestCase):

    def setUp(self):
        self.car = Car("Hyundai", "SantaFe", 10, 80)

    def test_init(self):
        self.assertEqual("Hyundai", self.car.make)
        self.assertEqual("SantaFe", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_or_lower(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_or_lower(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_or_lower(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_ok_amount(self):
        self.car.fuel_amount = 0
        self.car.refuel(1000)
        self.assertEqual(80, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel(self):
        self.car.fuel_amount = 5

        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.car.fuel_amount = 11
        self.car.drive(100)
        self.assertEqual(1, self.car.fuel_amount)


if __name__ == '__main__':
    main()
