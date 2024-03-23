from unittest import TestCase, main
from test_cat import Cat


class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Tomi")

    def test_init(self):
        self.assertEqual("Tomi", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_if_cat_already_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_if_cat_is_not_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_sleep_if_cat_not_fed_and_not_sleepy(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_if_cat_fed_and_sleepy(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()