from models.lane_model import LaneModel
import random

def get_random_lane() -> LaneModel:
    random_x1 = random.randint(-10, 100)
    random_lane_width = random.choices(population=[30, 40, 50, 60])[0]
    random_x2 = random_x1 + random_lane_width
    return LaneModel(random_x1, random_x2)