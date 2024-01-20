import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class Test_NubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.datetime(2020, 10, 4)
        last_service_date = datetime.datetime(2005, 6, 10)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(2024, 1, 18)
        last_service_date = datetime.datetime(2022, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class Test_SpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.datetime(2022, 2, 14)
        last_service_date = datetime.datetime(2018, 4, 6)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(2023, 7, 8)
        last_service_date = datetime.datetime(2022, 8, 9)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())