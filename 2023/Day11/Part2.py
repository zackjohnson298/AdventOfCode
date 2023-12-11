from typing import List, Tuple, Dict
import numpy as np


def get_input(filename) -> np.array:
    with open(filename) as file:
        lines = file.read().splitlines()
    return np.array([[char for char in line] for line in lines])


def get_points(grid: np.array) -> List[List[int]]:
    rows, cols = grid.shape
    output = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == '#':
                output.append([r, c])
    return output


def find_empty_rows_and_cols(grid: np.array) -> Tuple[List[int], List[int]]:
    rows, cols = grid.shape
    empty_rows = []
    empty_cols = []
    for r in range(rows):
        row = grid[r, :]
        if not any([val == '#' for val in row]):
            empty_rows.append(r)
    for c in range(cols):
        col = grid[:, c]
        if not any([val == '#' for val in col]):
            empty_cols.append(c)
    return empty_rows, empty_cols


def main():
    grid = get_input('input.txt')
    delta = 1000000
    points = get_points(grid)
    empty_rows, empty_cols = find_empty_rows_and_cols(grid)
    for point in points:
        r, c = point
        skipped_rows = sum([1 if r >= val else 0 for val in empty_rows])
        skipped_cols = sum([1 if c >= val else 0 for val in empty_cols])
        point[0] += (delta-1) * skipped_rows
        point[1] += (delta-1) * skipped_cols
    total = 0
    for ii in range(len(points)-1):
        r1, c1 = points[ii]
        for jj in range(ii+1, len(points)):
            r2, c2 = points[jj]
            total += abs(r1-r2) + abs(c1-c2)
    print(total)



main()
