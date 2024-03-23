from unittest import TestCase, main
from test_worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("Mitko", 1000, 10)

    def test_init_method(self):
        self.assertEqual("Mitko", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_without_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_with_enough_energy(self):
        expected_money = self.worker.salary
        expected_energy = 9

        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_when_resting(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_method_get_info(self):
        result = self.worker.get_info()
        expected = f'Mitko has saved 0 money.'
        self.worker.get_info()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
