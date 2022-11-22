from enums.enum_lka_status import LkaStatus
from enums.enum_steer_direction import SteerDirection
from enums.enum_steering_override import SteeringOveride
from models.lane_model import LaneModel


def display_vehicle_state(speed: int, lka_status: LkaStatus, lane_coordinates: LaneModel, steer_override: SteeringOveride):
    """
    This functions displays the vehicle state to the user 
    on a diplay unit such as LCD, Heads-Up-Display.
    """
    print('Vehicle speed - ', speed, 'kmph')
    print('Vehicle LKA status - ', lka_status)
    print('Steering override status - ', steer_override)
    print('Lane coordinates \n\tLane 1=', lane_coordinates.x1,
          ', Lane 2=', lane_coordinates.x2)


def display_alert(message: str):
    """
    This functions displays the alerts to the user 
    on a diplay unit such as LCD, Heads-Up-Display.
    """
    print(message)
