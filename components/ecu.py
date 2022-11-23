"""
        File contains functions that emulates ECU system
"""

from enums.enum_lka_status import LkaStatus
import random

def get_random_lka_status() -> LkaStatus:
        return random.choices(population=[LkaStatus.ON, LkaStatus.OFF], weights=[0.85, 0.15], k=1)[0]

def get_random_speed() -> int:
        return random.choices(population=[random.randint(1, 4), random.randint(5, 120), random.randint(121, 130)], weights=[0.1, 0.8, 0.1], k=1)[0]