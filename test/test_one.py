import math
import unittest

from module_one.one import Circle

class TestCircle( unittest.TestCase ):
    def test_create_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(-1)

    def test_area(self):
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.area(), math.pi * 2.5*2.5)

    def test_color(self):
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.colorPrice("blue"), 1)

if __name__ == '__main__':
    unittest.main()


