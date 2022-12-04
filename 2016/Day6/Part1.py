import numpy as np
from statistics import mode


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = np.array([[char for char in line] for line in lines])
    return grid


def main():
    grid = get_input('input.txt')
    rows, cols = grid.shape
    code = ''
    for col in range(cols):
        code += mode(grid[:, col])
    print(code)


main()
