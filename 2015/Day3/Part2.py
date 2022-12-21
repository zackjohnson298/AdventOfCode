import numpy as np


def get_input(filename):
    with open(filename) as file:
        line = file.readline()
    return [char for char in line]


def main():
    steps = get_input('input.txt')
    directions = {
        '>': np.array((1, 0), dtype='int'),
        '<': np.array((-1, 0), dtype='int'),
        '^': np.array((0, 1), dtype='int'),
        'v': np.array((0, -1), dtype='int'),
    }
    pos1 = (0, 0)
    pos2 = (0, 0)
    houses = [pos1]
    for ii, step in enumerate(steps):
        if ii % 2 == 0:
            pos1 = tuple(np.array(pos1, dtype='int') + directions[step])
            pos = pos1
        else:
            pos2 = tuple(np.array(pos2, dtype='int') + directions[step])
            pos = pos2
        if pos not in houses:
            houses.append(pos)
    print(len(houses))


main()
