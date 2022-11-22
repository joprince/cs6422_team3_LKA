"""
    File contains function that emulates the steering system
"""

import random

from models.steering_model import SteeringModel
from enums.enum_steering_override import SteeringOveride


def get_random_steer_override() -> SteeringOveride:
    """
        Function return whether the steering system is overriden or not
    """
    return random.choices(
        population=[SteeringOveride.YES, SteeringOveride.NO],
        weights=[0.15, 0.85], k=1)[0]


def steer_vehicle(curr_steering_state: SteeringModel):
    """
        Function prints the vehicle print status
    """
    print('Vehicle steers to - ', curr_steering_state)
