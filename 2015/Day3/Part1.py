import numpy as np


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [char for char in line]


def main():
    steps = get_input('input.txt')
    # steps = '^>v<'
    directions = {
        '>': np.array((1, 0), dtype='int'),
        '<': np.array((-1, 0), dtype='int'),
        '^': np.array((0, 1), dtype='int'),
        'v': np.array((0, -1), dtype='int'),
    }
    pos = (0, 0)
    houses = [pos]
    for step in steps:
        pos = tuple(np.array(pos, dtype='int') + directions[step])
        if pos not in houses:
            houses.append(pos)
    print(len(houses))


main()
