from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation('Varna')

    def test_correct_init(self):
        self.assertEqual('Varna', self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_where_len_less_than_three(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'Ya'

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_where_len_equals_three(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'Yar'

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_appends_info(self):
        self.station.new_arrival_on_board("Train1")

        self.assertEqual(deque(["Train1"]), self.station.arrival_trains)

    def test_train_har_arrived_where_there_are_other_trains_to_arrive(self):
        self.station.arrival_trains = deque(["Train1", "Train2"])
        result = self.station.train_has_arrived("Train2")

        self.assertEqual("There are other trains to arrive before Train2.", result)
        self.assertEqual(deque(["Train1", "Train2"]), self.station.arrival_trains)

    def test_train_has_arrived_where_first_train_equals_arg(self):
        self.station.arrival_trains = deque(["Train1", "Train2"])
        result = self.station.train_has_arrived("Train1")

        self.assertEqual("Train1 is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(["Train2"]), self.station.arrival_trains)
        self.assertEqual(deque(["Train1"]), self.station.departure_trains)

    def test_train_has_left_where_first_train_equals_arg(self):
        self.station.departure_trains = deque(["Train1"])
        result = self.station.train_has_left("Train1")

        self.assertEqual(True, result)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_left_where_first_train_diff_than_arg(self):
        self.station.departure_trains = deque(["Train1", "Train2"])
        result = self.station.train_has_left("Train2")

        self.assertEqual(False, result)


if __name__ == '__main__':
    main()
