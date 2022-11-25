"""
    This file contains test case for calculate steer angle function
"""

from components.lane_keep_assist import calculate_steer_angle
from models.lane_model import LaneModel
from models.steering_model import SteeringModel,SteerDirection
import math
import unittest

class TestCalculateSteerAngle(unittest.TestCase):

    def test_steer_angle_center(self) -> None:
        """
            IF
                Lane coordinates are indicating to stay in the CENTER
            THEN
                Steer direction should be CENTER
                Turn angle should be matching the expected degree of turn
                Horizontal distance from center should be center of the car minus the mid value 
        """

        laneCoordinates = LaneModel(25, 75)
        steerAngle = calculate_steer_angle(laneCoordinates)
        expectedOutput = SteeringModel(SteerDirection.CENTER, 0, 0)
        self.assertEqual(steerAngle.angle, expectedOutput.angle)
        self.assertEqual(steerAngle.direction, expectedOutput.direction)
        self.assertEqual(steerAngle.horizontal_distance_centre, expectedOutput.horizontal_distance_centre)

    def test_steer_angle_right(self) -> None:
        """
            IF
                Lane coordinates are indicating turn to RIGHT
            THEN
                Steer direction should be RIGHT
                Turn angle should be matching the expected degree of turn
                Horizontal distance from center should be center of the car minus the mid value 
        """
        laneCoordinates = LaneModel(26, 76)
        steerAngle = calculate_steer_angle(laneCoordinates)
        mid = laneCoordinates.x1 + (laneCoordinates.x2 - laneCoordinates.x1) / 2
        angle = math.atan2(25-0, mid-50)
        expectedOutput = SteeringModel(SteerDirection.RIGHT, angle, 1)
        self.assertEqual(steerAngle.angle, round(abs(90 - math.degrees(expectedOutput.angle)),2))
        self.assertEqual(steerAngle.direction, expectedOutput.direction)
        self.assertEqual(steerAngle.horizontal_distance_centre, expectedOutput.horizontal_distance_centre)

    def test_steer_angle_left(self) -> None:
        """
            IF
                Lane coordinates are indicating turn to LEFT
            THEN
                Steer direction should be LEFT
                Turn angle should be matching the expected degree of turn
                Horizontal distance from center should be center of the car minus the mid value
        """

        laneCoordinates = LaneModel(24, 74)
        steerAngle = calculate_steer_angle(laneCoordinates)
        mid = laneCoordinates.x1 + (laneCoordinates.x2 - laneCoordinates.x1) / 2
        angle = math.atan2(25-0, mid-50)
        expectedOutput = SteeringModel(SteerDirection.LEFT, angle, 1)
        self.assertEqual(steerAngle.angle, round(abs(90 - math.degrees(expectedOutput.angle)),2))
        self.assertEqual(steerAngle.direction, expectedOutput.direction)
        self.assertEqual(steerAngle.horizontal_distance_centre, expectedOutput.horizontal_distance_centre)