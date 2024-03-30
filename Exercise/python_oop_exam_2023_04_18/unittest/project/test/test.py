from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot('Lucky', 'Military', 10, 1_000)
        self.robot2 = Robot('Brethren', 'Entertainment', 5, 100)

    def test_correct__init__(self):
        self.assertEqual('Lucky', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(1_000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_when_invalid_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "WarRobot"

        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_where_less_than_0_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_where_upgrade_already_done(self):
        self.robot.hardware_upgrades = ["Gun", "Gun2"]
        result = self.robot.upgrade("Gun", 100)

        self.assertEqual("Robot Lucky was not upgraded.", result)

    def test_upgrade_when_upgrade_possible(self):
        self.robot.hardware_upgrades = ["Gun", "Gun2"]
        result = self.robot.upgrade("Gun3", 1000)

        self.assertEqual('Robot Lucky was upgraded with Gun3.', result)
        self.assertEqual(["Gun", "Gun2", "Gun3"], self.robot.hardware_upgrades)
        self.assertEqual(2500.0, self.robot.price)

    def test_update_happy_path(self):
        result = self.robot.update(1.0, 5)

        self.assertEqual('Robot Lucky was updated to version 1.0.', result)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual([1.0], self.robot.software_updates)

    def test_update_happy_path_needed_capacity_equals_available(self):
        result = self.robot.update(1.0, 10)

        self.assertEqual('Robot Lucky was updated to version 1.0.', result)
        self.assertEqual(0, self.robot.available_capacity)
        self.assertEqual([1.0], self.robot.software_updates)

    def test_update_where_version_equals_current_version(self):
        self.robot.software_updates = [1.0, 2.0]
        result = self.robot.update(2.0, 9)

        self.assertEqual("Robot Lucky was not updated.", result)

    def test_update_where_not_enough_capacity(self):
        result = self.robot.update(1.0, 11)

        self.assertEqual("Robot Lucky was not updated.", result)

    def test__gt__where_first_robot_more_expensive(self):
        result = self.robot.__gt__(self.robot2)
        self.assertEqual('Robot with ID Lucky is more expensive than Robot with ID Brethren.', result)

    def test__gt__where_robot_prices_equal(self):
        self.robot2.price = 1_000
        result = self.robot.__gt__(self.robot2)

        self.assertEqual('Robot with ID Lucky costs equal to Robot with ID Brethren.', result)

    def test__gt__where_second_robot_more_expensive(self):
        self.robot2.price = 1001
        result = self.robot.__gt__(self.robot2)

        self.assertEqual(f'Robot with ID Lucky is cheaper than Robot with ID Brethren.', result)


if __name__ == '__main__':
    main()
