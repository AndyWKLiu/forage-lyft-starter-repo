import unittest
from tire.carrigan_tire import CarriganTire 
from tire.octoprime_tire import OctoprimeTire 

class Test_CarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [0.1, 0.7, 0.8, 0.9] 
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.1, 0.3, 0.4, 0.5]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())

class Test_Octoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [0.9, 0.8, 0.7, 0.9]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.1, 0.2, 0.4, 0.3]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())