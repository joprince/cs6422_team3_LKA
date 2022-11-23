"""
    File contains tests for steering system
"""
from unittest import TestCase, mock


from models.steering_model import SteeringModel
from enums.enum_steer_direction import SteerDirection
from enums.enum_steering_override import SteeringOveride
from components.steering_system import get_random_steer_override

class TestSteeringSystem(TestCase):
    """
        Test cases for steering system
    """
    @staticmethod
    def mock_steering_override_no(**kwargs):
        return [SteeringOveride.NO]

    @staticmethod
    def mock_steering_override_yes(**kwargs):
        return [SteeringOveride.YES]

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



    def test_get_random_steer_override(self):
        """
            Test for get_random_steer_override
        """
        override_status = get_random_steer_override()
        self.assertIn(override_status, [SteeringOveride.YES, SteeringOveride.NO])
