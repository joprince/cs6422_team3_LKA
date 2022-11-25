"""
    File contains model class for steering model
"""

from enums.enum_steer_direction import SteerDirection

class SteeringModel:
    """
        Model class for steering model
    """
    def __init__(
        self, direction: SteerDirection,
        steer_angle: float, distance_from_center: int) -> None:
        """
            Constructor function
        """
        self.direction = direction
        self.angle = steer_angle
        self.horizontal_distance_centre = distance_from_center

    def __str__(self) -> str:
        return f"direction: {self.direction}, angle: {round(abs(self.angle), 2)}"
