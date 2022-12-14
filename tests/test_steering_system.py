"""
    File contains tests for steering system
"""
import io
import sys
from unittest import TestCase


from models.steering_model import SteeringModel
from enums.enum_steer_direction import SteerDirection
from enums.enum_steering_override import SteeringOveride
from components.steering_system import get_random_steer_override, steer_vehicle


class TestSteeringSystem(TestCase):
    """
        Test cases for steering system
    """

    def test_get_random_steer_override(self):
        """
            Test for get_random_steer_override
        """
        override_status = get_random_steer_override()
        self.assertIn(override_status, [
                      SteeringOveride.YES, SteeringOveride.NO])

    def test_steer_system_left(self):
        """
            Test case for steer_vehicle function with direction left
        """
        steering_model = SteeringModel(
            SteerDirection.LEFT,
            25,
            50
        )

        expected = "Lane Keep Assist steers vehicle to SteerDirection.LEFT by 25 degrees"
        output = steer_vehicle(steering_model)
        self.assertEqual(output, expected)

    def test_steer_system_right(self):
        """
            Test case for steer_vehicle function with direction right
        """
        steering_model = SteeringModel(
            SteerDirection.RIGHT,
            25,
            50
        )

        expected = "Lane Keep Assist steers vehicle to SteerDirection.RIGHT by 25 degrees"
        output = steer_vehicle(steering_model)
        self.assertEqual(output, expected)

    def test_steer_system_center(self):
        """
            Test case for steer_vehicle function with direction center
        """
        steering_model = SteeringModel(
            SteerDirection.CENTER,
            25,
            50
        )

        expected = "Vehicle is in the center of the lane"
        output = steer_vehicle(steering_model)
        self.assertEqual(output, expected)

    def test_steering_model(self):
        """
            Test case for steering model
        """
        steering_model = SteeringModel(
            SteerDirection.CENTER,
            25,
            50
        )
        expected = "direction: SteerDirection.CENTER, angle: 25"
        output = steering_model.__str__()
        self.assertEqual(output, expected)
