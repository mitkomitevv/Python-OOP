from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestRobots(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'Head', 100, 100)

    def test_init(self):
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual('Head', self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid Category"

        self.assertEqual(f"Category should be one of {self.robot.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_valid_category(self):
        self.robot.category = "Mountain"
        self.assertEqual("Mountain", self.robot.category)

    def test_get_used_capacity(self):
        software1 = {'name': 'Chrome', 'capacity_consumption': 30, 'memory_consumption': 65}
        software2 = {'name': 'DEX', 'capacity_consumption': 20, 'memory_consumption': 35}
        self.robot.installed_software = [software1, software2]
        self.assertEqual(50, self.robot.get_used_capacity())

    def test_get_available_capacity(self):
        self.robot.installed_software = [{'capacity_consumption': 20}]
        self.assertEqual(80, self.robot.get_available_capacity())

    def test_get_used_memory(self):
        software1 = {'name': 'Chrome', 'capacity_consumption': 30, 'memory_consumption': 65}
        software2 = {'name': 'DEX', 'capacity_consumption': 20, 'memory_consumption': 25}
        self.robot.installed_software = [software1, software2]
        self.assertEqual(90, self.robot.get_used_memory())

    def test_get_available_memory(self):
        self.robot.installed_software = [{'memory_consumption': 33}]
        self.assertEqual(67, self.robot.get_available_memory())

    def test_install_software_where_installation_possible(self):
        software = {'name': 'Software', 'capacity_consumption': 50, 'memory_consumption': 50}
        result = self.robot.install_software(software)

        self.assertEqual(f"Software 'Software' successfully installed on Mountain part.", result)
        self.assertEqual(self.robot.installed_software, [software])

    def test_install_software_where_capacity_consumption_equals_capacity(self):
        software = {'name': 'Software', 'capacity_consumption': 100, 'memory_consumption': 50}
        result = self.robot.install_software(software)

        self.assertEqual(f"Software 'Software' successfully installed on Mountain part.", result)
        self.assertEqual(self.robot.installed_software, [software])

    def test_install_software_where_memory_consumption_equals_memory(self):
        software = {'name': 'Software', 'capacity_consumption': 10, 'memory_consumption': 100}
        result = self.robot.install_software(software)

        self.assertEqual(f"Software 'Software' successfully installed on Mountain part.", result)
        self.assertEqual(self.robot.installed_software, [software])

    def test_install_software_when_needed_more_memory(self):
        software = {'name': 'Software', 'capacity_consumption': 120, 'memory_consumption': 50}
        result = self.robot.install_software(software)

        self.assertEqual(f"Software 'Software' cannot be installed on Mountain part.", result)

    def test_install_software_when_needed_more_capacity(self):
        software = {'name': 'Software', 'capacity_consumption': 50, 'memory_consumption': 150}
        result = self.robot.install_software(software)

        self.assertEqual(f"Software 'Software' cannot be installed on Mountain part.", result)

    def test_install_software_where_both_memory_and_capacity_not_enough(self):
        software = {'name': 'Software', 'capacity_consumption': 150, 'memory_consumption': 150}
        result = self.robot.install_software(software)

        self.assertEqual(f"Software 'Software' cannot be installed on Mountain part.", result)


if __name__ == '__main__':
    main()
