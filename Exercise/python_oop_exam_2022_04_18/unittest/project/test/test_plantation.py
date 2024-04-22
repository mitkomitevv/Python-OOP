from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test__init__(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_where_less_than_0_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_where_worker_already_exists(self):
        self.plantation.workers = ['Mitko', 'Ivan']

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Mitko')

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_happy_path(self):
        result = self.plantation.hire_worker('Mitko')

        self.assertEqual(['Mitko'], self.plantation.workers)
        self.assertEqual("Mitko successfully hired.", result)

    def test__len__(self):
        self.plantation.plants = {
            'Mitko': ['Plant1', 'Plant2', 'Plant3', 'Plant4', 'Plant5'],
            'Ivan': ['Plant6', 'Plant7', 'Plant8', 'Plant9', 'Plant10']
        }

        self.assertEqual(self.plantation.__len__(), 10)

    def test_planting_where_worker_does_not_exist(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Mitko', 'Plant')

        self.assertEqual("Worker with name Mitko is not hired!", str(ve.exception))

    def test_planting_where_size_insufficient(self):
        self.plantation.hire_worker('Mitko')
        self.plantation.plants = {
            'Mitko': ['Plant1', 'Plant2', 'Plant3', 'Plant4', 'Plant5'],
            'Ivan': ['Plant6', 'Plant7', 'Plant8', 'Plant9', 'Plant10']
        }

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Mitko', 'Plant')

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_where_worker_exists_in_plantation(self):
        self.plantation.workers = {'Mitko', 'Ivan'}
        self.plantation.plants = {
            'Mitko': ['Plant1', 'Plant2', 'Plant3', 'Plant4', 'Plant5']
        }

        result = self.plantation.planting('Mitko', 'Plant6')

        self.assertEqual("Mitko planted Plant6.", result)
        self.assertEqual({'Mitko': ['Plant1', 'Plant2', 'Plant3', 'Plant4', 'Plant5', 'Plant6']}, self.plantation.plants)

    def test_planting_where_worker_not_int_plantation(self):
        self.plantation.workers = {'Mitko', 'Ivan'}
        result = self.plantation.planting('Mitko', 'Plant9')

        self.assertEqual("Mitko planted it's first Plant9.", result)
        self.assertEqual({'Mitko': ['Plant9']}, self.plantation.plants)

    def test__str__(self):
        self.plantation.workers = ['Mitko', 'Ivan']
        self.plantation.plants = {
            'Mitko': ['Plant1', 'Plant2', 'Plant3'],
            'Ivan': ['Plant6', 'Plant7', 'Plant8']
        }

        expected_result = ("Plantation size: 10\n"
                           "Mitko, Ivan\n"
                           "Mitko planted: Plant1, Plant2, Plant3\n"
                           "Ivan planted: Plant6, Plant7, Plant8")

        self.assertEqual(expected_result, str(self.plantation))

    def test__repr__(self):
        self.plantation.workers = ['Mitko', 'Ivan']
        expected_result = ("Size: 10\n"
                           "Workers: Mitko, Ivan")

        self.assertEqual(expected_result, repr(self.plantation))


if __name__ == '__main__':
    main()
