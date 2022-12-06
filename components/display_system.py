"""
    File contains functions that emulates display sytem
"""


from enums.enum_lka_status import LkaStatus
from enums.enum_steer_direction import SteerDirection
from enums.enum_steering_override import SteeringOveride
from models.lane_model import LaneModel
import math


def display_vehicle_state(speed: int, lka_status: LkaStatus, lane_coordinates: LaneModel, steer_override: SteeringOveride):
    """
    This functions displays the vehicle state to the user
    on a diplay unit such as LCD, Heads-Up-Display.
    """
    print(f"Vehicle current speed = {speed}kmph")
    print(f"Vehicle LKA status = {lka_status}")
    print(f"Steering override status = {steer_override}")
    print(
        f'Lane coordinates (from left of Sensor POV)\n\tLane 1 = {lane_coordinates.x1} units, Lane 2 = {lane_coordinates.x2} units')


def display_alert(message: str):
    """
    This functions displays the alerts to the user
    on a diplay unit such as LCD, Heads-Up-Display.
    """
    print(message)


def display_status_message(message: str):
    """
    This functions returns the formatted status message.
    """
    tab = ' ' * 8
    max_width = 54
    fixed_padding = 9  # * and 8 spaces
    available_width = max_width - fixed_padding * 2
    num_lines = int(math.ceil(len(message) / available_width))
    output = ''
    output += '*' * 54
    output += f"\n*{' ' * 52}*"
    for num in range(0, num_lines):
        start = num * available_width
        end = (num * available_width) + available_width
        message_to_display = message[start: end]
        output += f'\n*{tab}{message[start: end]}{" " * (8 + available_width - len(message_to_display))}*'
    output += f"\n*{' ' * 52}*\n"
    output += '*' * 54

    return output
