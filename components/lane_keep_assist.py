from models.lane_model import LaneModel
from models.steering_model import SteeringModel
from enums.enum_steer_direction import SteerDirection
import math


def calculate_steer_angle(lane_coordinates: LaneModel) -> SteeringModel:
    mid = lane_coordinates.x1 + (lane_coordinates.x2 - lane_coordinates.x1) / 2
    angle_radians = math.atan2(25-0, mid-50)
    dir = SteerDirection.CENTER
    if abs(mid) > 50:
        dir = SteerDirection.RIGHT
    elif abs(mid) < 50:
        dir = SteerDirection.LEFT
    return SteeringModel(dir, round(abs(90 - math.degrees(angle_radians)), 2), abs(50 - mid))
