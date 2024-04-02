from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_correct__init__(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected, self.store.toy_shelf)

    def test_add_toy_where_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('M', 'robot')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_where_toy_already_on_shelf(self):
        self.store.toy_shelf = {'M': 'robot'}
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('M', 'robot')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_where_shelf_is_not_empty(self):
        self.store.toy_shelf = {'M': 'robot', 'K': 'car'}
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('K', 'bike')

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_happy_path(self):
        self.store.toy_shelf = {'M': 'robot', 'K': 'car', 'P': None}
        result = self.store.add_toy('P', 'bike')

        self.assertEqual("Toy:bike placed successfully!", result)
        self.assertEqual({'M': 'robot', 'K': 'car', 'P': 'bike'}, self.store.toy_shelf)

    def test_remove_toy_where_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('M', 'bike')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_where_toy_not_on_shelf(self):
        self.store.toy_shelf = {'M': 'robot', 'K': 'car'}
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('M', 'bike')

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_happy_path(self):
        self.store.toy_shelf = {'M': 'robot', 'K': 'car'}
        result = self.store.remove_toy('M', 'robot')

        self.assertEqual("Remove toy:robot successfully!", result)
        self.assertEqual({'M': None, 'K': 'car'}, self.store.toy_shelf)


if __name__ == '__main__':
    main()
