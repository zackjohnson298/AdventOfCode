import numpy as np
import json


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    data = [[int(value) for value in line] for line in lines]
    return np.array(data)


def get_local_gradient(grid, r, c):
    rows, cols = grid.shape
    min_pos = np.array([r, c])
    min_value = grid[r, c]
    for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
        if nr not in [-1, rows] and nc not in [-1, cols]:
            if grid[nr, nc] < min_value:
                min_value = grid[nr, nc]
                min_pos = np.array([nr, nc])
    return min_pos - np.array([r, c])


def get_gradient(grid):
    gradient = []
    rows, cols = grid.shape
    for r in range(rows):
        row = []
        for c in range(cols):
            if grid[r, c] == 9:
                row.append(None)
            else:
                local_gradient = get_local_gradient(grid, r, c)
                row.append(local_gradient)
        gradient.append(row)
    return gradient


def find_low_points(grid):
    rows, cols = grid.shape
    low_points = []
    for r in range(rows):
        for c in range(cols):
            for nr, nc in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                if nr not in [-1, rows] and nc not in [-1, cols]:
                    if grid[r, c] >= grid[nr, nc]:
                        break
            else:
                low_points.append((r, c))
    return low_points


def main():
    grid = get_input('input.txt')
    gradient = get_gradient(grid)
    basins = {low_point: [] for low_point in find_low_points(grid)}
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            local_gradient = gradient[r][c]
            if local_gradient is not None:
                pos = np.array([r, c])
                while np.linalg.norm(local_gradient) > 0.1:
                    pos += local_gradient
                    local_gradient = gradient[pos[0]][pos[1]]
                basins[(pos[0], pos[1])].append([r, c])
    sizes = [len(points) for points in basins.values()]
    print(np.prod(sorted(sizes)[-3:]))

main()
