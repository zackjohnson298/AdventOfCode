import numpy as np


def get_steps(word):
    steps = []
    number_str = ''
    for char in word:
        if char.isdigit():
            number_str = number_str + char
        else:
            steps.append(int(number_str))
            steps.append(char)
            number_str = ''
    if number_str.isdigit():
        steps.append(int(number_str))
    return steps


def rot_z(angle):
    angle = np.pi * angle / 180
    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ], dtype='int')


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = []
    steps = get_steps(lines.pop())
    lines.pop()
    max_width = max([len(line) for line in lines])

    for line in lines:
        row = []
        line = line + ' '*(max_width - len(line))
        for char in line:
            if char == '.':
                row.append(0)
            elif char == '#':
                row.append(1)
            elif char == ' ':
                row.append(2)
        grid.append(row)
    return np.array(grid, dtype='int'), steps


def draw_grid(grid):
    for row in grid.T:
        for value in row:
            if value == 0:
                print('.', end='')
            if value == 1:
                print('#', end='')
            if value == 2:
                print(' ', end='')
        print()
    print()


def get_next_pos(grid, pos, direction):
    next_pos = (pos + direction) % grid.shape
    while grid[tuple(next_pos)] == 2:
        next_pos = (next_pos + direction) % grid.shape
    if grid[tuple(next_pos)] == 1:
        return pos
        # next_pos -= direction
        # next_pos = next_pos % grid.shape
    return next_pos


def main():
    grid, steps = get_input('input.txt')
    rows, cols = grid.shape
    direction = np.array((0, 1)).T                 # To the right
    pos = None
    for c in range(cols):
        if grid[0, c] == 0:
            pos = np.array((0, c)).T
            break

    for step in steps:
        if type(step) == int:
            for _ in range(step):
                pos = get_next_pos(grid, pos, direction)
        elif step == 'R':
            direction = rot_z(-90) @ direction
        elif step == 'L':
            direction = rot_z(90) @ direction
        else:
            print(f'unhandled step: {step}')

    row, col = pos + np.array((1, 1)).T
    if (direction == np.array((0, 1)).T).all():
        facing = 0
    if (direction == np.array((1, 0)).T).all():
        facing = 1
    if (direction == np.array((0, -1)).T).all():
        facing = 2
    if (direction == np.array((-1, 0)).T).all():
        facing = 3

    print(row, col, facing)
    print(1000 * row + 4 * col + facing)

main()
