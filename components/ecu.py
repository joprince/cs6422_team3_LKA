from enums.enum_lka_status import LkaStatus
import random


def get_random_lka_status() -> LkaStatus:
    return random.choices(population=[LkaStatus.ON, LkaStatus.OFF], weights=[0.9, 0.1], k=1)[0]

def get_random_speed(current_speed: int) -> int:
    initial_speed = current_speed
    factor = random.randint(1, 5)

    if current_speed > 120:
        operation = 'sub'
    elif current_speed < 5:
        operation = 'add'
    else:
        operation = random.choices(
            population=['add', 'sub'], weights=[0.7, 0.3])[0]
    if operation == 'add':
        current_speed += factor
    else:
        current_speed -= factor
        
    return current_speed
