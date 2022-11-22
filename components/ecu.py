from enums.enum_lka_status import LkaStatus
import random

def get_random_lka_status() -> LkaStatus:
        return random.choices(population=[LkaStatus.ON, LkaStatus.OFF], weights=[0.85, 0.15], k=1)[0]

def get_random_speed() -> int:
        return random.choices(population=[random.randint(1, 4), 5, random.randint(6, 119), random.randint(120, 130)], weights=[0.1, 0.1, 0.7, 0.1], k=1)[0]