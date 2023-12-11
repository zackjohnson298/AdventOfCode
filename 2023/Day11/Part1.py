from typing import List, Tuple, Dict
import numpy as np


def get_input(filename) -> np.array:
    with open(filename) as file:
        lines = file.read().splitlines()
    return np.array([[char for char in line] for line in lines])


def expand(grid: np.array) -> np.array:
    new_grid = np.copy(grid)
    rows, cols = grid.shape
    for r in reversed(range(rows)):
        row = grid[r, :]
        if not any([val == '#' for val in row]):
            new_grid = np.insert(new_grid, [r], np.array([['.' * cols]]), axis=0)
    rows, _ = new_grid.shape
    for c in reversed(range(cols)):
        col = grid[:, c]
        if not any([val == '#' for val in col]):
            new_grid = np.insert(new_grid, [c], np.array([['.' * rows]]).T, axis=1)
    return new_grid


def print_grid(grid: np.array):
    for row in grid:
        print(''.join(row))
    print()


def get_points(grid: np.array) -> List[Tuple[int, int]]:
    rows, cols = grid.shape
    output = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == '#':
                output.append((r, c))
    return output


def main():
    grid = get_input('input.txt')
    grid = expand(grid)
    points = get_points(grid)
    total = 0
    for ii in range(len(points)-1):
        r1, c1 = points[ii]
        for jj in range(ii+1, len(points)):
            r2, c2 = points[jj]
            total += abs(r1-r2) + abs(c1-c2)
    print(total)


main()
