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
        self.waypoint = np.array([10, 1]).T

    @property
    def manhattan(self) -> int:
        return abs(self.position[0]) + abs(self.position[1])

    def rotate_waypoint_right(self):
        a, b = self.waypoint
        self.waypoint[0] = b
        self.waypoint[1] = -a

    def rotate_waypoint_left(self):
        a, b = self.waypoint
        self.waypoint[0] = -b
        self.waypoint[1] = a

    def navigate(self, instruction: Tuple[str, int]):
        direction, value = instruction
        direction_vec = DIRECTIONS.get(direction)
        if direction_vec is not None:
            self.waypoint += value * direction_vec
            return
        elif direction == 'R':
            for _ in range(value // 90):
                self.rotate_waypoint_right()
        elif direction == 'L':
            for _ in range(value // 90):
                self.rotate_waypoint_left()
        elif direction == 'F':
            self.position += value * self.waypoint
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
