from components.steering_system import get_random_steer_override
from components.lane_detection_system import get_lane_data, get_random_lane
from components.ecu import get_random_lka_status, get_random_speed
from models.lane_model import LaneModel
from models.steering_model import SteeringModel
from enums.enum_steer_direction import SteerDirection
from enums.enum_steering_override import SteeringOveride
from enums.enum_lka_status import LkaStatus
from components.display_system import display_vehicle_state, display_speed, display_status_message, display_lane, print_there, display_steering_override_status, display_LKA_status
from components.alert_system import alert_user
from components.lane_keep_assist import calculate_steer_angle
from components.steering_system import steer_vehicle
import time
import os


def main():
    """
        Main Function
    """
    curr_steering_state = SteeringModel(SteerDirection.CENTER, 0, 0)
    curr_lane_state = get_random_lane()
    force_ctr = 0
    speed = 0

    while(True):
        os.system('clear')
        steer_override = get_random_steer_override()
        speed = get_random_speed(speed)
        lka_status = get_random_lka_status()

        print_there(0, 0, display_speed(speed))
        print_there(3, 0, display_LKA_status(lka_status))
        print_there(5, 0, display_steering_override_status(steer_override))
        print_there(8, 20, display_lane(curr_lane_state))

        if steer_override == SteeringOveride.YES:
            print_there(0, 60, display_status_message(
                'Driver is steering the vehicle manually'))
        else:
            if speed < 5 or speed > 120:
                print_there(0, 60, display_status_message(
                    'Lane Keep Assist does not work in the current the speed'))
            else:
                if lka_status == LkaStatus.OFF:
                    print_there(0, 60, display_status_message(
                        'Lane Keep Assist is turned off'))
                else:
                    if curr_lane_state.x2 < curr_lane_state.x1 or curr_lane_state.x1 < 0 or curr_lane_state.x2 < 0 or curr_lane_state.x1 > 100 or curr_lane_state.x2 > 100:
                        print_there(0, 60, display_status_message(
                            'Invalid lane coordinates'))
                        curr_lane_state = get_random_lane()
                    else:
                        curr_steering_state = calculate_steer_angle(
                            curr_lane_state)
                        print_there(0, 60, display_status_message(
                            steer_vehicle(curr_steering_state)))

                        if force_ctr >= 1:
                            force_ctr = 0

                        if curr_steering_state.direction == SteerDirection.CENTER:
                            force_ctr += 1

                        curr_lane_state = get_lane_data(
                            curr_steering_state, curr_lane_state, force_ctr >= 1)

        time.sleep(2)


if __name__ == "__main__":
    main()
