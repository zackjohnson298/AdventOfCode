import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    points = []
    steps = []
    line = lines.pop(0)
    while len(line) > 0:
        points.append(list(reversed([int(value) for value in line.split(',')])))
        line = lines.pop(0)
    for line in lines:
        step = []
        if 'x' in line:
            step.append('left')
        else:
            step.append('up')
        step.append(int(line.split('=')[1]))
        steps.append(step)
    return points, steps


def update_grid(grid, instruction):
    direction, value = instruction
    print(instruction, grid.shape)
    if direction == 'left':
        new_grid = grid[:, :value] + np.fliplr(grid[:, value+1:])
    else:
        new_grid = grid[:value, :] + np.flipud(grid[value+1:, :])
    return new_grid


def print_grid(grid):
    for row in grid:
        for value in row:
            if value > 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def main():
    points, steps = get_input('input.txt')
    max_x = max([point[0] for point in points]) + 1
    max_y = max([point[1] for point in points]) + 1
    if max_x % 2 == 0:
        max_x += 1
    if max_y % 2 == 0:
        max_y += 1
    grid = np.zeros((max_x, max_y))
    for x, y in points:
        grid[x, y] = 1

    grid = update_grid(grid, steps[0])
    print(sum(sum(grid > 0)))


main()
