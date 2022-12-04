import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    steps = []
    for line in lines:
        lst = line.split()
        step = []
        if lst[0] == 'rect':
            x, y = [int(char) for char in lst[1].split('x')]
            step = ['rect', x, y]
        else:
            step = [lst[1], int(lst[2][2:]), int(lst[-1])]
        steps.append(step)
    return steps


def main():
    steps = get_input('input.txt')
    grid = np.zeros((50, 6))
    for instruction, a, b in steps:
        if instruction == 'rect':
            grid[:a, :b] = np.ones((a, b))
        elif instruction == 'column':
            new_col = np.array(grid[a, -b:].tolist() + grid[a, :-b].tolist()).T
            grid[a, :] = new_col
        elif instruction == 'row':
            new_row = np.array(grid[-b:, a].tolist() + grid[:-b, a].tolist()).T
            grid[:, a] = new_row

    print(int(sum(sum(grid))))


main()
