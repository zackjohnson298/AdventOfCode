import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    grid = []
    for line in lines:
        row = []
        for char in line:
            if char == '.':
                row.append(0)
            elif char == '|':
                row.append(1)
            elif char == '#':
                row.append(2)
        grid.append(row)
    return np.array(grid, dtype='int')


def get_neighbors(grid: np.array, point: (int, int)):
    neighbors = []
    r, c = point
    rows, cols = grid.shape
    for nr in [r-1, r, r+1]:
        for nc in [c-1, c, c+1]:
            if 0 <= nc < cols and 0 <= nr < rows and (nr, nc) != (r, c):
                neighbors.append((nr, nc))
    return neighbors


def get_new_grid(grid: np.array):
    rows, cols = grid.shape
    new_grid = grid.copy()

    for r in range(rows):
        for c in range(cols):
            points = []
            for neighbor in get_neighbors(grid, (r, c)):
                points.append(grid[neighbor])
            if grid[r, c] == 0:
                if points.count(1) >= 3:
                    new_grid[r, c] = 1
            elif grid[r, c] == 1:
                if points.count(2) >= 3:
                    new_grid[r, c] = 2
            elif grid[r, c] == 2:
                if points.count(2) < 1 or points.count(1) < 1:
                    new_grid[r, c] = 0
    return new_grid


def print_grid(grid):
    for row in grid:
        for value in row:
            if value == 0:
                print('.', end='')
            elif value == 1:
                print('|', end='')
            elif value == 2:
                print('#', end='')
        print()
    print()


def main():
    grid = get_input('input.txt')
    desired = 1000000000
    # print(grid.shape)
    # print(get_neighbors(grid, (5, 5)))
    # print_grid(grid)
    # _ = input()
    state = tuple([tuple(row) for row in grid])
    states = [state]
    index = 0
    for ii in range(desired):
        print(ii)
        grid = get_new_grid(grid)
        state = tuple([tuple(row) for row in grid])
        index += 1
        if state in states:
            print('Loop found', states.index(state))
            break
        states.append(state)
    first_index = states.index(state)
    second_index = index
    delta = (desired - first_index) % (second_index - first_index)
    grid = np.array(states[first_index + delta])
    print()
    print(sum(sum(grid == 1)) * sum(sum(grid == 2)))



main()
