import numpy as np


DIRECTIONS = [
    np.array((0, 0, -1), dtype='int'),  # D
    np.array((0, 0, 1), dtype='int'),   # U
    np.array((0, -1, 0), dtype='int'),  # L
    np.array((0, 1, 0), dtype='int'),   # R
    np.array((-1, 0, 0), dtype='int'),  # B
    np.array((1, 0, 0), dtype='int')    # F
]


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [tuple([int(value) for value in line.split(',')]) for line in lines]


def are_neighbors(point_a: (int, int, int), point_b: (int, int, int)):
    equal_list = [a == b for a, b in zip(point_a, point_b)]
    if sum(equal_list) == 2:
        index = equal_list.index(False)
        if abs(point_a[index] - point_b[index]) == 1:
            return True
    return False


def populate_neighbors(points: [(int, int, int)]):
    neighbors = {point: [] for point in points}
    for point_a in points:
        for point_b in points:
            if point_a == point_b or point_a in neighbors[point_b]:
                continue
            if are_neighbors(point_a, point_b):
                neighbors[point_a].append(point_b)
                neighbors[point_b].append(point_a)
    return neighbors


def on_boundary(grid, point):
    x_size, y_size, z_size = grid.shape
    if point[0] == 0 or point[0] == x_size - 1:
        return True
    if point[1] == 0 or point[1] == y_size - 1:
        return True
    if point[2] == 0 or point[2] == z_size - 1:
        return True
    return False


def is_enclosed(grid: np.array, point: (int, int, int), visited: {(int, int, int): bool}):
    visited[point] = True
    if on_boundary(grid, point):
        visited[point] = False
        return False
    for direction in DIRECTIONS:
        new_point = tuple(np.array(point, dtype='int') + direction)
        if not grid[new_point]:
            if visited.get(new_point) is False or (new_point not in visited and not is_enclosed(grid, new_point, visited)):
                visited[point] = False
                return False
    return True


def main():
    points = get_input('input.txt')
    grid_size = tuple([max([point[ii] for point in points]) + 1 for ii in range(3)])
    grid = np.zeros(grid_size, dtype='bool')
    for point in points:
        grid[point] = True
    x_size, y_size, z_size = grid.shape
    print('Finding Enclosed points')
    enclosed_count = 0
    enclosed = {}
    for x in range(x_size):
        for y in range(y_size):
            for z in range(z_size):
                if not grid[x, y, z] and (x, y, z):
                    if is_enclosed(grid, (x, y, z), enclosed):
                        enclosed_count += 1
                        points.append((x, y, z))
    print(f'Found {enclosed_count} enclosed points, calculating surface area...')
    neighbors = populate_neighbors(points)
    total = 6*len(points)
    for key, value in neighbors.items():
        total -= len(value)
    print()
    print(total)


main()
