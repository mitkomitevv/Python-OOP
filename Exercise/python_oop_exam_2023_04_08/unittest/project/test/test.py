from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer("Grigor", 32, 3000)
        self.player2 = TennisPlayer("Sinner", 22, 6000)

    def test_correct__init__(self):
        self.assertEqual("Grigor", self.player.name)
        self.assertEqual(32, self.player.age)
        self.assertEqual(3000, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name__where_name_equals_or_less_than_2_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Gr'

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_where_age_less_than_18_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_when_tournament_exists(self):
        self.player.wins = ["Miami", "Toronto"]
        result = self.player.add_new_win("Miami")

        self.assertEqual("Miami has been already added to the list of wins!", result)

    def test_add_new_win_when_tournament_does_not_exist(self):
        self.player.wins = ["Miami", "Toronto"]
        self.player.add_new_win("Sofia")

        self.assertEqual(["Miami", "Toronto", "Sofia"], self.player.wins)

    def test__lt__when_other_is_better(self):
        result = self.player.__lt__(self.player2)
        self.assertEqual('Sinner is a top seeded player and he/she is better than Grigor', result)

    def test__lt__when_player_is_better(self):
        self.player2.points = 2999
        result = self.player.__lt__(self.player2)

        self.assertEqual('Grigor is a better player than Sinner', result)

    def test__str__(self):
        self.player.wins = ["Miami", "Toronto", "Sofia"]

        expected_result = (f"Tennis Player: Grigor\n"
                           f"Age: 32\n"
                           f"Points: 3000.0\n"
                           f"Tournaments won: Miami, Toronto, Sofia")

        self.assertEqual(expected_result, str(self.player))


if __name__ == '__main__':
    main()
