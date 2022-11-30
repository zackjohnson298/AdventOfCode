import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = [[int(value) for value in line] for line in lines]
    return np.array(grid)


def find_flashes(grid):
    rows, cols = grid.shape
    points = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] > 9:
                points.append([r, c])
    return points


def update_grid(grid):
    new_grid = grid.copy()
    new_grid += np.ones(new_grid.shape, dtype='int')
    rows, cols = new_grid.shape
    flash_points = find_flashes(new_grid)
    flashes = []
    while len(flash_points) > 0:
        for r, c in flash_points:
            new_grid[r, c] = 0
            flashes.append([r, c])
            for nr in [r-1, r, r+1]:
                for nc in [c-1, c, c+1]:
                    if nr not in [-1, rows] and nc not in [-1, cols] and [nr, nc] not in flashes:
                        new_grid[nr, nc] += 1
        flash_points = find_flashes(new_grid)
    return len(flashes), new_grid


def main():
    grid = get_input('input.txt')
    steps = 100
    total_flashes = 0
    for step in range(steps):
        # print(f'Step {step}, flashes {total_flashes}:')
        # print(grid)
        # print()
        flashes, grid = update_grid(grid)
        total_flashes += flashes
    print(total_flashes)

main()
