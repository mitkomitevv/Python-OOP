from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Gabriel", "Lion", "ROAR")

    def test_init(self):
        self.assertEqual("Gabriel", self.mammal.name)
        self.assertEqual("Lion", self.mammal.type)
        self.assertEqual("ROAR", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Gabriel makes ROAR", self.mammal.make_sound())

    def test_info(self):
        self.assertEqual("Gabriel is of type Lion", self.mammal.info())


if __name__ == '__main__':
    main()
