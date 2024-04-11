from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):

    def setUp(self):
        self.store = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_book_limit(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_len(self):
        self.store.availability_in_store_by_book_titles = {'Red Rising': 2, 'Ashes of Man': 7}
        result = self.store.__len__()

        self.assertEqual(9, result)

    def test_receive_book_where_not_enough_space(self):
        self.store.availability_in_store_by_book_titles = {'Red Rising': 2, 'Ashes of Man': 7}
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Empire of the Damned', 2)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_books_up_to_limit(self):
        self.store.receive_book("At The Limit", 10)
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Beyond The Limit", 1)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book(self):
        result1 = self.store.receive_book("Red God", 5)
        self.assertEqual("5 copies of Red God are available in the bookstore.", result1)

        result2 = self.store.receive_book("Red God", 5)
        self.assertEqual("10 copies of Red God are available in the bookstore.", result2)
        self.assertEqual({"Red God": 10}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_where_enough_space_book_already_in_store(self):
        self.store.availability_in_store_by_book_titles = {'Red Rising': 2, 'Ashes of Man': 5}
        result = self.store.receive_book('Red Rising', 3)

        self.assertEqual("5 copies of Red Rising are available in the bookstore.", result)
        self.assertEqual({'Red Rising': 5, 'Ashes of Man': 5}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_where_enough_space_book_not_in_store(self):
        self.store.availability_in_store_by_book_titles = {'Red Rising': 2, 'Ashes of Man': 5}
        result = self.store.receive_book('Empire of the Damned', 3)

        self.assertEqual("3 copies of Empire of the Damned are available in the bookstore.", result)
        self.assertEqual({'Red Rising': 2, 'Ashes of Man': 5, 'Empire of the Damned': 3}, self.store.availability_in_store_by_book_titles)

    def test_sell_book_where_book_not_in_store(self):
        self.store.availability_in_store_by_book_titles = {'Red Rising': 2, 'Ashes of Man': 5, 'Empire of the Damned': 3}
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Soldiers Live', 3)

        self.assertEqual("Book Soldiers Live doesn't exist!", str(ex.exception))

    def test_sell_book_where_not_enough_copies(self):
        self.store.availability_in_store_by_book_titles = {'Red Rising': 2, 'Ashes of Man': 5, 'Empire of the Damned': 3}
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Ashes of Man', 6)

        self.assertEqual("Ashes of Man has not enough copies to sell. Left: 5", str(ex.exception))

    def test_sell_book_happy_path(self):
        self.store.availability_in_store_by_book_titles = {'Red Rising': 2, 'Ashes of Man': 5, 'Empire of the Damned': 3}
        result = self.store.sell_book('Ashes of Man', 3)

        self.assertEqual("Sold 3 copies of Ashes of Man", result)
        self.assertEqual({'Red Rising': 2, 'Ashes of Man': 2, 'Empire of the Damned': 3}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(3, self.store.total_sold_books)

    def test_str(self):
        self.store.availability_in_store_by_book_titles = {'Red Rising': 2, 'Ashes of Man': 5, 'Empire of the Damned': 3}
        result = self.store.__str__()
        expected_result = ("Total sold books: 0\n"
                           "Current availability: 10\n"
                           " - Red Rising: 2 copies\n"
                           " - Ashes of Man: 5 copies\n"
                           " - Empire of the Damned: 3 copies")

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
