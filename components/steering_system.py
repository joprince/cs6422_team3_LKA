"""
    File contains function that emulates the steering system
"""

import random

from models.steering_model import SteeringModel
from enums.enum_steering_override import SteeringOveride
from enums.enum_steer_direction import SteerDirection


def get_random_steer_override() -> SteeringOveride:
    """
        Function return whether the steering system is overriden or not
    """
    return random.choices(
        population=[SteeringOveride.YES, SteeringOveride.NO],
        weights=[0.1, 0.9], k=1)[0]


def steer_vehicle(curr_steering_state: SteeringModel):
    """
        Function prints the vehicle print status
    """
    if curr_steering_state.direction == SteerDirection.CENTER:
        print('\nVehicle is in the center of the lane')
    else:
        print(
            f"\nLane Keep Assist steers vehicle to {curr_steering_state.direction} by {curr_steering_state.angle} degrees")
