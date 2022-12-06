# """
#     File contains test cases of display system
# """

# import io
# import sys
# import unittest

# from components.display_system import display_vehicle_state, display_alert
# from enums.enum_lka_status import LkaStatus
# from enums.enum_steering_override import SteeringOveride
# from models.lane_model import LaneModel


# class TestDisplaySystem(unittest.TestCase):
#     def test_display_vehicle_state(self):
#         """
#         This tests if the display_vehicle_state displays the correct output
#         """
#         laneCoordinates = LaneModel(35, 75)
#         lka_status = LkaStatus.ON
#         steer_override = SteeringOveride.NO
#         speed = 10

#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         display_vehicle_state(speed,
#                               lka_status,
#                               laneCoordinates,
#                               steer_override)
#         sys.stdout = sys.__stdout__
#         output = capturedOutput.getvalue()

#         expected = "Vehicle current speed = 10kmph\nVehicle LKA status = "
#         expected += "LkaStatus.ON\nSteering override status = SteeringOveride.NO\n"
#         expected += "Lane coordinates (from left of Sensor POV)\n\tLane 1 = 35 units, "
#         expected += "Lane 2 = 75 units\n"
#         self.assertEqual(output, expected)

#     def test_display_alert(self):
#         """
#         This tests if the display_alert displays the correct output
#         """
#         expected = "Hello World"
#         captured_output = io.StringIO()
#         sys.stdout = captured_output
#         display_alert(expected)
#         sys.stdout = sys.__stdout__
#         output = captured_output.getvalue().strip()
#         self.assertEqual(output, expected)
