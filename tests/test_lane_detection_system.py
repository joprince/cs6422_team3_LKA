"""
    File contains the test cases for lane detection
"""

import unittest

from enums.enum_steer_direction import SteerDirection
from models.lane_model import LaneModel
from models.steering_model import SteeringModel
from components.lane_detection_system import get_lane_data
from models.lane_model import LaneModel
from components.lane_detection_system import get_random_lane


class TestLaneDetectionSystem(unittest.TestCase):
    """

        Class containing the test cases for display system
    """

    def test_get_lane_data(self) -> None:
        """
        If
            the steer direction is CENTER
            new state is NOT requested
        then
            lane coordinates should return the same
            horizontal distance of steering model should remain the same
        """
        current_lane = LaneModel(25, 75)
        steer_direction = SteeringModel(SteerDirection.CENTER, 0, 0)
        new_state = False

        output = get_lane_data(steer_direction, current_lane, new_state)
        expected = current_lane
        self.assertEqual(output, expected)
        self.assertEqual(
            steer_direction.horizontal_distance_centre,
            steer_direction.horizontal_distance_centre
        )

    def test_get_lane_data_steerright(self) -> None:
        """
        If
            the steer direction is RIGHT
            new state is NOT requested
        then
            lane coordinates should reduce by 1 unit
            horizontal distance of steering model should reduce by 1 unit
        """
        current_lane = LaneModel(25, 75)
        steer_direction = SteeringModel(SteerDirection.RIGHT, 0, 1)
        new_state = False

        output = get_lane_data(steer_direction, current_lane, new_state)
        expected = LaneModel(24, 74)
        self.assertEqual(output.x1, expected.x1)
        self.assertEqual(output.x2, expected.x2)
        self.assertEqual(steer_direction.horizontal_distance_centre, 0)

    def test_get_lane_data_turnleft(self) -> None:
        """
        If
            the steer direction is LEFT
            new state is NOT requested
        then
            lane coordinates should increase by 1 unit
            horizontal distance of steering model should reduce by 1 unit
        """
        current_lane = LaneModel(25, 75)
        steer_direction = SteeringModel(SteerDirection.LEFT, 0, 1)
        new_state = False

        output = get_lane_data(steer_direction, current_lane, new_state)
        expected = LaneModel(26, 76)
        self.assertEqual(output.x1, expected.x1)
        self.assertEqual(output.x2, expected.x2)
        self.assertEqual(steer_direction.horizontal_distance_centre, 0)

    def test_get_lane_data_newstate(self) -> None:
        """
        If
            new state is requested
        then
            New lane coordinates should be generated
        """
        current_lane = LaneModel(25, 75)
        steer_direction = SteeringModel(SteerDirection.LEFT, 0, 1)
        new_state = True

        output = get_lane_data(steer_direction, current_lane, new_state)
        self.assertNotEqual(output.x1, current_lane.x1)
        self.assertNotEqual(output.x2, current_lane.x2)

    def test_get_lane_data_newstate_units(self) -> None:
        """
        If
            new state is requested
        then
            New lane coordinates should be generated
            and the difference should not exceed 5 units
        """
        current_lane = LaneModel(25, 75)
        steer_direction = SteeringModel(SteerDirection.LEFT, 0, 1)
        new_state = True

        output = get_lane_data(steer_direction, current_lane, new_state)
        lane1_diff = abs(current_lane.x1 - output.x1)
        lane2_diff = abs(current_lane.x2 - output.x2)
        self.assertLessEqual(lane1_diff, 5)
        self.assertLessEqual(lane2_diff, 5)

    def test_lane_model(self) -> None:
        """
            Test case for lane model class
        """
        lanemodel = LaneModel(
            35, 75
        )
        self.assertEqual(lanemodel.__str__(), "x1: 35, x2: 75")

    def test_get_random_lane(self) -> None:
        """
            Twest case for get_random_lane  function
        """
        lane_state = get_random_lane()
        self.assertIn(lane_state.x1, range(-10, 100))
        self.assertIn(lane_state.x2, range(-10, 160))
        width_list = [30, 40, 50, 60]
        assert lane_state.x2 - lane_state.x1 in width_list
        self.assertLess(lane_state.x1, lane_state.x2)
