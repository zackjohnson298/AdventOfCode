import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    points = {}
    for ii, line in enumerate(lines, start=1):
        x, y = [int(value) for value in line.split(', ')]
        points[ii] = (x, y)
    return points


def get_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def find_closest_point(points: {int: (int, int)}, point: (int, int)):
    point_ids = sorted(points.keys())
    distances = []
    for point_id in point_ids:
        distance = get_distance(point, points[point_id])
        distances.append(distance)
    min_distance = min(distances)
    if distances.count(min_distance) > 1:
        return None
    return point_ids[distances.index(min_distance)]


def main():
    points = get_input('input.txt')
    min_x = min([point[0] for point in points.values()])
    min_y = min([point[1] for point in points.values()])
    max_x = max([point[0] for point in points.values()])
    max_y = max([point[1] for point in points.values()])

    grid = np.zeros((max_x, max_y), dtype='int')

    point_counts = {point_id: 0 for point_id in points}
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            closest_point_id = find_closest_point(points, (x, y))
            if closest_point_id is not None:
                point_counts[closest_point_id] += 1
                grid[x, y] = closest_point_id
    infinite_point_ids = grid[:, min_y].tolist() + grid[:, max_y-1].tolist() + grid[min_x, :].tolist() + grid[max_x-1, :].tolist()
    infinite_point_ids = set(infinite_point_ids)
    print(max([count for point_id, count in point_counts.items() if point_id not in infinite_point_ids]))


main()
