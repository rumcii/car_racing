import unittest

from car import Car
from driver import Driver


class TestDriver(unittest.TestCase):

    def setUp(self):
        Driver.nickname_list = []
        self.car = Car("opel", "astra", 160)
        self.driver = Driver("Rumen", "ruci1", self.car)

    def test_driver_equals(self):
        other_driver = Driver("Rumen", "ruci", self.car)
        other_driver_2 = Driver("Ciklama", "ciki1", self.car)

        self.assertEqual(self.driver, other_driver)
        self.assertNotEqual(self.driver, other_driver_2)

    def test_driver_instance(self):
        self.assertTrue(isinstance(self.driver, Driver))

if __name__ =='__main__':
    unittest.main()