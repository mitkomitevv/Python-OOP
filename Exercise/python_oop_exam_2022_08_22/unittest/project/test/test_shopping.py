from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self):
        self.cart = ShoppingCart('Lidl', 100)
        self.cart2 = ShoppingCart('Billa', 50)

    def test__init__(self):
        self.assertEqual('Lidl', self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_incorrect_shop_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'lidl'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_incorrect_shop_name2_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = '22 '

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_with_price_higher_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('Bread', 100.01)

        self.assertEqual(f"Product Bread cost too much!", str(ve.exception))
        self.assertEqual({}, self.cart.products)

    def test_add_to_cart_happy_path(self):
        result = self.cart.add_to_cart('Bread', 99.99)

        self.assertEqual("Bread product was successfully added to the cart!", result)
        self.assertEqual({'Bread': 99.99}, self.cart.products)

    def test_remove_from_cart_where_product_does_not_exist(self):
        self.cart.products = {'Bread': 99.99, 'Butter': 60.99}
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('Ham')

        self.assertEqual("No product with name Ham in the cart!", str(ve.exception))
        self.assertEqual({'Bread': 99.99, 'Butter': 60.99}, self.cart.products)

    def test_remove_from_cart_happy_path(self):
        self.cart.products = {'Bread': 99.99, 'Butter': 60.99}
        result = self.cart.remove_from_cart('Bread')

        self.assertEqual("Product Bread was successfully removed from the cart!", result)
        self.assertEqual({'Butter': 60.99}, self.cart.products)

    def test__add__(self):
        self.cart.add_to_cart('Bread', 50)
        self.cart2.add_to_cart('Butter', 20)

        result = self.cart.__add__(self.cart2)

        self.assertEqual('LidlBilla', result.shop_name)
        self.assertEqual(150, result.budget)
        self.assertEqual({'Bread': 50, 'Butter': 20}, result.products)

    def test_buy_products_where_budget_not_enough(self):
        self.cart.products = {'Bread': 70, 'Butter': 30.01}
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 0.01lv!", str(ve.exception))

    def test_buy_products_successfully(self):
        self.cart.products = {'Bread': 70, 'Butter': 30.00}
        result = self.cart.buy_products()

        self.assertEqual('Products were successfully bought! Total cost: 100.00lv.', result)


if __name__ == '__main__':
    main()
