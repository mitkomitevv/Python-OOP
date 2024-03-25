from unittest import TestCase, main
from int_list import IntegerList


class ListTests(TestCase):

    def setUp(self):
        self.int_list = IntegerList(1, 2, 3, 7.3, "Astrid")

    def test_init_if_arg_not_integer(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_el_to_list_if_el_not_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add("Patience")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_el_if_el_integer(self):
        expected_list = self.int_list.get_data().copy() + [5]
        self.int_list.add(5)

        self.assertEqual(expected_list, self.int_list.get_data())

    def test_remove_index_if_index_bigger_or_equal_to_list(self):
        with self.assertRaises(IndexError) as ve:
            self.int_list.remove_index(1000)

        self.assertEqual("Index is out of range", str(ve.exception))

    def test_remove_index_if_index_ok(self):
        self.int_list.remove_index(1)
        self.assertEqual([1, 3], self.int_list.get_data())

    def test_get_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ve:
            self.int_list.get(1000)

        self.assertEqual("Index is out of range", str(ve.exception))

    def test_get_with_ok_index(self):
        self.assertEqual(3, self.int_list.get(2))

    def test_insert_with_index_out_of_range(self):
        with self.assertRaises(IndexError) as ve:
            self.int_list.insert(1000, 5)

        self.assertEqual("Index is out of range", str(ve.exception))

    def test_insert_with_non_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, 3.3)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_with_ok_params(self):
        expected_list = self.int_list.get_data().copy()

        expected_list.insert(1, 5)
        self.int_list.insert(1, 5)

        self.assertEqual(expected_list, self.int_list.get_data())

    def test_get_biggest(self):
        self.assertEqual(3, self.int_list.get_biggest())

    def test_get_index(self):
        self.assertEqual(2, self.int_list.get_index(3))


if __name__ == "__main__":
    main()
