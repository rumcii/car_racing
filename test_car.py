import unittest
from car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("opel", "astra", 160)

    def test_car_equals(self):
        car1 = Car("opel", "astra", 160)

        self.assertEqual(self.car, car1)
