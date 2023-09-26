import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = np.array([[int(value) for value in line] for line in lines])
    return grid


def get_scenic_score(grid, pos):
    if 0 in pos:
        return 0
    row, col = pos
    rows, cols = grid.shape
    # Right
    right = 1
    for c in range(col+1, cols-1):
        if grid[row, c] < grid[row, col]:
            right += 1
        else:
            break
    # Left
    left = 1
    for c in reversed(range(1, col)):
        if grid[row, c] < grid[row, col]:
            left += 1
        else:
            break
    # Down
    down = 1
    for r in range(row + 1, rows-1):
        if grid[r, col] < grid[row, col]:
            down += 1
        else:
            break
    # Up
    up = 1
    for r in reversed(range(1, row)):
        if grid[r, col] < grid[row, col]:
            up += 1
        else:
            break
    return up*down*left*right


def main():
    grid = get_input('input.txt')
    rows, cols = grid.shape
    sizes = {}
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            sizes[(row, col)] = get_scenic_score(grid, (row, col))
    for key, value in sizes.items():
        print(key, value)

    print()
    print(max(sizes.values()))


main()
