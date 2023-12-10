from typing import List, Optional, Tuple
import numpy as np


DIRECTIONS = {
    'N': np.array([0, 1]).T,
    'E': np.array([1, 0]).T,
    'S': np.array([0, -1]).T,
    'W': np.array([-1, 0]).T
}

DIRECTION_LIST = ['N', 'E', 'S', 'W']


class Ship:
    def __init__(self):
        self.position = np.array([0, 0]).T
        self.direction = 'E'

    @property
    def manhattan(self) -> int:
        return abs(self.position[0]) + abs(self.position[1])

    def navigate(self, instruction: Tuple[str, int]):
        direction, value = instruction
        direction_vec = DIRECTIONS.get(direction)
        if direction_vec is not None:
            self.position += value * direction_vec
            return
        elif direction == 'R':
            self.direction = DIRECTION_LIST[(DIRECTION_LIST.index(self.direction) + (value // 90)) % 4]
        elif direction == 'L':
            self.direction = DIRECTION_LIST[(DIRECTION_LIST.index(self.direction) - (value // 90)) % 4]
        elif direction == 'F':
            self.position += DIRECTIONS[self.direction] * value
        else:
            raise Exception(f'Unhandled instruction: {instruction}')


def get_input(filename) -> List[Tuple[str, int]]:
    with open(filename) as file:
        lines = file.read().splitlines()
    return [(line[0], int(line[1:])) for line in lines]


def main():
    steps = get_input('input.txt')
    ship = Ship()
    for step in steps:
        ship.navigate(step)
    print(ship.manhattan)


main()
