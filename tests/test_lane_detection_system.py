import unittest
from models.lane_model import LaneModel
import components.lane_detection_system


class TestLaneDetectionSystem(unittest.TestCase):

    def test_lane_model(self):
        lanemodel = LaneModel(
            35,
            75
        )
        self.assertEqual(lanemodel.__str__(), "x1: 35, x2: 75")

    def test_get_random_lane(self):
        lane_state = components.lane_detection_system.get_random_lane();
        self.assertIn(lane_state.x1, range(-10, 100))
        self.assertIn(lane_state.x2, range(-10, 160))
        width_list = [30, 40, 50, 60]
        assert lane_state.x2 - lane_state.x1 in width_list
        self.assertLess(lane_state.x1, lane_state.x2)
