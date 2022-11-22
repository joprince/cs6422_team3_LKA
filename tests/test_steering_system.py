"""
    File contains tests for steering system
"""
import unittest

from components.steering_system import steer_vehicle
from models.steering_model import SteeringModel
from enums.enum_steer_direction import SteerDirection


class TestSteeringSystem(unittest.TestCase):
    """
        Test cases for steering system
    """
    def test_steer_vehicle(self):
        """
            Test for function printing steering status
        """
        steering = SteeringModel(
            SteerDirection.CENTER,
            15,
            5
        )
        assert steering.__str__() == \
            "direction: SteerDirection.CENTER, angle: 15",\
                 "Output should be direction: SteerDirection.CENTER, angle: 15"
