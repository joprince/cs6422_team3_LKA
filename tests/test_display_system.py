import io
import sys
import unittest
from components.display_system import display_vehicle_state
from enums.enum_lka_status import LkaStatus
from enums.enum_steering_override import SteeringOveride
from models.lane_model import LaneModel

class TestDisplaySystem(unittest.TestCase):

    def test_display_system(self):
        laneCoordinates = LaneModel(35,75)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        display_vehicle_state(10,
                            LkaStatus.ON,
                            laneCoordinates,
                            SteeringOveride.NO)
        print(sys.getsizeof(capturedOutput.getvalue))
        sys.stdout = sys.__stdout__
        self.assertEquals(sys.getsizeof(capturedOutput.getvalue()),241)