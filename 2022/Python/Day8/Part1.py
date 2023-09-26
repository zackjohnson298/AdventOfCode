import json
import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = np.array([[int(value) for value in line] for line in lines])
    return grid


def get_visible_edges(grid):
    rows, cols = grid.shape
    visible_trees = [[0, col] for col in range(cols)]
    visible_trees.extend([[rows - 1, col] for col in range(cols)])
    visible_trees.extend([[row, 0] for row in range(1, rows-1)])
    visible_trees.extend([[row, cols - 1] for row in range(1, rows-1)])
    return visible_trees


def main():
    grid = get_input('input.txt')
    rows, cols = grid.shape
    visible_trees = get_visible_edges(grid)
    print('edges', visible_trees, len(visible_trees))
    # Down
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if [row, col] not in visible_trees:
                sub_col = grid[:row+1, col].tolist()
                if grid[row, col] == max(grid[:row+1, col]) and sub_col.count(grid[row, col]) == 1:
                    visible_trees.append([row, col])
    print('down ', visible_trees)
    # Up
    for row in reversed(range(1, rows - 1)):
        for col in range(1, cols - 1):
            if [row, col] not in visible_trees:
                sub_col = grid[row:, col].tolist()
                if grid[row, col] == max(sub_col) and sub_col.count(grid[row, col]) == 1:
                    visible_trees.append([row, col])
    print('up   ', visible_trees)
    # Left
    for col in range(1, cols - 1):
        for row in range(1, rows - 1):
            if [row, col] not in visible_trees:
                sub_row = grid[row, :col+1].tolist()
                if grid[row, col] == max(sub_row) and sub_row.count(grid[row, col]) == 1:
                    visible_trees.append([row, col])
    print('left ', visible_trees)
    # Right
    for row in range(1, rows - 1):
        for col in reversed(range(1, cols - 1)):
            if [row, col] not in visible_trees:
                sub_row = grid[row, col:].tolist()
                if grid[row, col] == max(sub_row) and sub_row.count(grid[row, col]) == 1:
                    visible_trees.append([row, col])
    print('right', visible_trees)
    print()
    print(len(visible_trees))


main()
