from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("Hyundai", "SUV", 200_000, 10_000)
        self.car2 = SecondHandCar("Hyundai", "Sedan", 200_000, 9_999)

    def test_correct_init(self):
        self.assertEqual("Hyundai", self.car.model)
        self.assertEqual("SUV", self.car.car_type)
        self.assertEqual(200_000, self.car.mileage)
        self.assertEqual(10_000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_where_price_below_one(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_price_where_price_above_one(self):
        self.car.price = 1.01
        self.assertEqual(1.01, self.car.price)

    def test_mileage_when_equals_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_mileage_when_above_hundred(self):
        self.car.mileage = 101
        self.assertEqual(101, self.car.mileage)

    def test_set_promotional_price_where_new_price_more_than_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(11_000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_when_success(self):
        result = self.car.set_promotional_price(9_000)
        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(9_000, self.car.price)

    def test_need_repair_when_repair_price_more_than_half_of_car_price(self):
        result = self.car.need_repair(5001, "Engine")
        self.assertEqual('Repair is impossible!', result)

    def test_repair_when_repair_price_valid(self):
        result = self.car.need_repair(4999, "Engine")

        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(14999, self.car.price)
        self.assertEqual(["Engine"], self.car.repairs)

    def test__gt__when_car_types_difference(self):
        result = self.car.__gt__(self.car2)
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test__gt__when_car_types_same(self):
        self.car2.car_type = "SUV"
        result = self.car.__gt__(self.car2)
        self.assertEqual(True, result)

    def test__str__(self):
        expected_result = ("Model Hyundai | Type SUV | Milage 200000km\n"
                           "Current price: 10000.00 | Number of Repairs: 0")

        self.assertEqual(expected_result, str(self.car))

    def test__str__with_more_than_one_repairs(self):
        self.car.need_repair(1000, "Engine")
        self.car.need_repair(5000, "Clutch")

        expected_result = ("Model Hyundai | Type SUV | Milage 200000km\n"
                           "Current price: 16000.00 | Number of Repairs: 2")

        self.assertEqual(expected_result, str(self.car))


if __name__ == '__main__':
    main()
