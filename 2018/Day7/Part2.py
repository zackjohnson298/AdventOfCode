
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


def get_total_distance(points: {int: (int, int)}, point: (int, int)):
    total = sum([get_distance(point, point_a) for point_a in points.values()])
    return total


def main():
    points = get_input('input.txt')
    max_distance = 10000
    min_x = min([point[0] for point in points.values()])
    min_y = min([point[1] for point in points.values()])
    max_x = max([point[0] for point in points.values()])
    max_y = max([point[1] for point in points.values()])

    count = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            total_distance = get_total_distance(points, (x, y))
            if total_distance < max_distance:
                count += 1
    print(count)



main()
