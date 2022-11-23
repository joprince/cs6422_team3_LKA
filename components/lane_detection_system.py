"""
    File contains functions that emulates lane detectio system
"""

from models.lane_model import LaneModel
from models.steering_model import SteeringModel
from enums.enum_steer_direction import SteerDirection
import random


def get_random_lane() -> LaneModel:
    random_x1 = random.randint(-10, 100)
    random_lane_width = random.choices(population=[30, 40, 50, 60])[0]
    random_x2 = random_x1 + random_lane_width
    return LaneModel(random_x1, random_x2)


def get_lane_data(steer_wheel_direction: SteeringModel, current_lane_state: LaneModel, new_state: bool) -> LaneModel:
    if new_state:
        new_dir = random.choices(
            [SteerDirection.RIGHT, SteerDirection.LEFT])[0]
        factor = random.randint(1, 5)
        if new_dir == SteerDirection.RIGHT:
            return LaneModel(current_lane_state.x1 + factor, current_lane_state.x2 + factor)
        else:
            return LaneModel(current_lane_state.x1 - factor, current_lane_state.x2 - factor)
    elif steer_wheel_direction.direction == SteerDirection.CENTER and steer_wheel_direction.angle == 0:
        return current_lane_state
    elif steer_wheel_direction.direction == SteerDirection.RIGHT:
        steer_wheel_direction.horizontal_distance_centre -= 1
        return LaneModel(int(current_lane_state.x1 - 1), int(current_lane_state.x2 - 1))
    else:
        steer_wheel_direction.horizontal_distance_centre -= 1
        return LaneModel(int(current_lane_state.x1 + 1), int(current_lane_state.x2 + 1))
