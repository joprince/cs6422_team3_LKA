from enums.enum_lka_status import LkaStatus
import random

def get_random_lka_status() -> LkaStatus:
        return random.choices(population=[LkaStatus.ON, LkaStatus.OFF], weights=[0.85, 0.15], k=1)[0]

def get_random_speed(current_speed : int) -> int:
    initial_speed = current_speed
    while True:
        factor = random.randint(1, 5)
        operation = random.choices(population=['add', 'sub'])[0]
        if operation == 'add':
            current_speed += factor
        else:
            current_speed -= factor

        if current_speed > 0:
            break
        current_speed = initial_speed
    return current_speed