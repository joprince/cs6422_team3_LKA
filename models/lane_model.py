"""

"""

class LaneModel:
    """
        Model class for lane model
    """
    def __init__(self, x1: int, x2: int) -> None:
        """
            Constructor function for Lane Model
        """
        self.x1 = x1
        self.x2 = x2

    def __str__(self) -> str:
        return f"x1: {self.x1}, x2: {self.x2}"
