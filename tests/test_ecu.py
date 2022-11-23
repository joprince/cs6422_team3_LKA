"""
    File contains test cases for ecu unit
"""

import unittest

from components.ecu import get_random_lka_status,get_random_speed
from enums.enum_lka_status import LkaStatus

class TestECU(unittest.TestCase):
    """
        Test cases for ECU system
    """
    def test_status(self):
        """
            Test for function randomizing lka status
        """
        status = get_random_lka_status()
        self.assertIn(status, [LkaStatus.ON, LkaStatus.OFF])

    def test_speed_range(self):
        """
            Test for function randomizing vehicle speed
        """
        speed = get_random_speed()
        self.assertGreater(speed,0)
        self.assertLess(speed,131)
