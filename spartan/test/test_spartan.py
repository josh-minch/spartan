import unittest
import spartan

class TestFood(unittest.TestCase):
    def test_get_selectable_units_without_amount_prefix(self):
        food = spartan.Food(1001)
        correct_units = [
            'g', 'oz (28.35 g)', 'lb (453.6 g)', 'pat (1" sq, 1/3" high) (5 g)',
            'tbsp (14.2 g)', 'cup (227 g)', 'stick (113 g)']
        self.assertEqual(food.get_selectable_units(), correct_units)

    def test_get_selectable_units_with_amount_prefix(self):
        food = spartan.Food(1090)
        correct_units = [
            'g', 'oz (28.35 g)', 'lb (453.6 g)', '0.25 cup (32 g)', 'cup (128 g)']
        self.assertEqual(food.get_selectable_units(), correct_units)

class TestSpartan(unittest.TestCase):
    """ Test classless Spartan functions"""
    def test_convert_quantity(self):
        self.assertEqual(spartan.convert_quantity(
            3.2, 'pat (1" sq, 1/3" high) (3.8 g)'), 12.16)


if __name__ == '__main__':
    unittest.main()
