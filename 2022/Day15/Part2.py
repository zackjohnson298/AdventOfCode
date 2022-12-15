import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    paths = []
    for line in lines:
        corners = []
        for string in line.split(' -> '):
            a, b = string.split(',')
            corners.append((int(a), int(b)))
        paths.append(corners)
    return paths


def get_grid_size(paths):
    max_x = 0
    max_y = 0
    for path in paths:
        for x, y in path:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    return max_x+1, max_y+1


def get_next_edge(current, next_pos):
    next_x = (next_pos[0] - current[0]) / abs(current[0] - next_pos[0]) if current[0] != next_pos[0] else 0
    next_y = (next_pos[1] - current[1]) / abs(current[1] - next_pos[1]) if current[1] != next_pos[1] else 0
    return np.array((int(next_x), int(next_y)))


def create_grid(paths):
    grid = np.zeros(get_grid_size(paths))
    for path in paths:
        for ii in range(1, len(path)):
            current = np.array(path[ii-1])
            next_corner = np.array(path[ii])
            grid[tuple(current)] = 1
            while np.linalg.norm(current - next_corner) > 0.01:
                current += get_next_edge(current, next_corner)
                grid[tuple(current)] = 1
    return grid


def print_grid(grid):
    for row in grid.T:
        for value in row:
            if value == 1:
                print('#', end='')
            elif value == 2:
                print('o', end='')
            else:
                print('.', end='')
        print()
    print()


def get_next_pos(grid, current_pos):
    directions = [
        np.array((0, 1)),
        np.array((-1, 1)),
        np.array((1, 1))
    ]
    max_x, max_y = grid.shape
    for direction in directions:
        next_pos = current_pos + direction
        if 0 <= next_pos[0] < max_x and 0 <= next_pos[1] < max_y:
            if grid[tuple(next_pos)] == 0:
                return next_pos, True
        else:
            return None, False
    return None, True


def add_grain(grid, current=(500, 0)):
    next_pos, is_valid = get_next_pos(grid, current)
    while next_pos is not None and is_valid:
        current = next_pos
        next_pos, is_valid = get_next_pos(grid, current)
    if is_valid:
        grid[tuple(current)] = 2
    return is_valid


def main():
    paths = get_input('input.txt')
    _, max_y = get_grid_size(paths)

    paths.append([(500-(max_y+2), (max_y+1)), (500+(max_y+2), (max_y+1))])
    grid = create_grid(paths)
    while grid[500, 0] != 2:
        add_grain(grid)
    print(sum(sum(grid == 2)))


main()
