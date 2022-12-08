import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[char for char in line] for line in lines]


def main():
    instructions = get_input('input.txt')
    code = ''
    grid = [
        'XXXXX',
        'X123X',
        'X456X',
        'X789X',
        'XXXXX'
    ]
    directions = {
        'U': np.array([-1, 0]),
        'D': np.array([1, 0]),
        'L': np.array([0, -1]),
        'R': np.array([0, 1])
    }
    pos = np.array([2, 2])
    grid = np.array([[char for char in row] for row in grid])
    code = ''
    for steps in instructions:
        value = grid[tuple(pos)]
        for step in steps:
            new_pos = pos + directions[step]
            if grid[tuple(new_pos)] != 'X':
                pos = new_pos
                value = grid[tuple(new_pos)]
        code = code + value
    print(code)


main()
