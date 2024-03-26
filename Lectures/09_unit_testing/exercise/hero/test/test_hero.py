from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Darrow", 1, 100, 100)
        self.enemy = Hero("Lysander", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("Darrow", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_same_name(self):
        self.enemy.username = "Darrow"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_less_than_zero(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_less_than_zero(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight Lysander. He needs to rest", str(ve.exception))

    def test_battle_to_a_draw(self):
        self.enemy.level = 3
        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)

    def test_battle_enemy_wins(self):
        self.hero, self.enemy = self.enemy, self.hero

        expected_level = self.enemy.level + 1
        expected_health = self.enemy.health - self.hero.damage + 5
        expected_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_battle_hero_wins(self):
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_correct__str__(self):
        result = f"Hero Darrow: 1 lvl\n" \
                 f"Health: 100\n" \
                 f"Damage: 100\n"

        self.assertEqual(result, str(self.hero))


if __name__ == '__main__':
    main()
